from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from typing import Annotated, TypedDict


# === Состояние ===
class State(TypedDict):
    messages: Annotated[list, add_messages]
    task_id: str


# === Инструменты ===
@tool
def create_task() -> str:
    """Создаёт задачу и возвращает её ID."""
    return "TASK-123"


@tool
def add_comment(task_id: str, comment: str) -> str:
    """Добавляет комментарий к задаче по ID."""
    return f'Комментарий "{comment}" успешно добавлен к задаче с ID {task_id}.'


tools = [create_task, add_comment]
tool_node = ToolNode(tools)

# === LLM ===
llm = ChatOllama(model="qwen2.5", temperature=0)
llm_with_tools = llm.bind_tools(tools)


# === Узел агента ===
def call_model(state: State):
    system = SystemMessage(
        content=f"Ты — агент управления задачами. Текущий task_id: {state['task_id'] or 'не задан'}. "
                "Если задача не создана — сначала вызови create_task. Не выдумывай ID."
    )
    messages = [system] + state["messages"]
    return {"messages": [llm_with_tools.invoke(messages)]}


# === Узел обновления состояния ===
def update_task_id(state: State):
    for msg in reversed(state["messages"]):
        if isinstance(msg, ToolMessage) and msg.name == "create_task":
            return {"task_id": msg.content}
    return {"task_id": state["task_id"]}


# === Сборка графа ===
workflow = StateGraph(State)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.add_node("update", update_task_id)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    lambda state: "tools" if state["messages"][-1].tool_calls else "__end__"
)
workflow.add_edge("tools", "update")
workflow.add_edge("update", "agent")

app = workflow.compile()

# === Запуск с пошаговым выводом ===
if __name__ == "__main__":
    state = {"messages": [], "task_id": ""}

    # Шаг 1: создание задачи
    print("---- Шаг 1: Создание задачи ----")
    state = app.invoke({
        **state,
        "messages": [HumanMessage(content="Создай задачу: проверка подписки")]
    }
    )
    print(f"Состояние после шага 1: task_id = '{state['task_id']}'")

    # Шаг 2: добавление комментария
    print("\n---- Шаг 2: Добавление комментария ----")
    state = app.invoke({
        **state,
        "messages": [HumanMessage(content="Добавь комментарий: протестировано")]
    }
    )
    print(f"Состояние после шага 2: task_id = '{state['task_id']}'")

    # Финальный ответ
    last_msg = state["messages"][-1]

    print("\n---- Финальный ответ ----")
    print(last_msg.content)
