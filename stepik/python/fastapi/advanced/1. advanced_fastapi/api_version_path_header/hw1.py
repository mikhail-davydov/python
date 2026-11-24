from fastapi import APIRouter, FastAPI, HTTPException

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1", tags=["v1 Tasks"])
v2_router = APIRouter(prefix="/api/v2", tags=["v2 Tasks"])


def parse_task_id(task_id: str) -> int:
    if not task_id.isdigit() or int(task_id) <= 0:
        raise HTTPException(status_code=400, detail="Invalid task ID")
    return int(task_id)


@v1_router.get("/tasks")
def get_tasks_v1() -> str:
    return "Tasks in v1: Task 1, Task 2"


@v1_router.get("/tasks/{task_id}")
def get_task_v1(task_id: str) -> str:
    task = parse_task_id(task_id)
    return f"Task {task} in v1"


@v2_router.get("/tasks")
def get_tasks_v2() -> str:
    return "Tasks in v2: Task 1 (open), Task 2 (closed)"


@v2_router.get("/tasks/count")
def get_tasks_count_v2() -> str:
    return "Total tasks in v2: 2"


@v2_router.get("/tasks/{task_id}")
def get_task_v2(task_id: str) -> str:
    task = parse_task_id(task_id)
    return f"Task {task} in v2 with status: open"


app.include_router(v1_router)
app.include_router(v2_router)
