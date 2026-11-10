from fastapi import FastAPI, HTTPException, Body
from starlette import status

app = FastAPI()

notes_db = {0: "Study FastAPI", 1: "I like FastAPI"}
tasks_db = {0: "Study FastAPI", 1: "I like FastAPI"}
reminders_db = {}

quotes_db = {0: "FastAPI lets you build APIs fast with type hints",
             1: "Auto docs at /docs and /redoc with OpenAPI",
             2: "Pydantic validates your data",
             3: "Depends gives clean Dependency Injection",
             4: "Use async def and await for concurrency"}

goals_db = {0: "Learn FastAPI basics",
            1: "Build CRUD app",
            2: "Write tests with TestClient",
            3: "Add authentication",
            4: "Deploy to production"}

comments_db = {0: "First comment in FastAPI"}


@app.get("/comments")
async def read_comments() -> dict:
    return comments_db


@app.get("/comments/{comment_id}")
async def read_comment(comment_id: int) -> str:
    try:
        return comments_db[comment_id]
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )


@app.post("/comments", status_code=status.HTTP_201_CREATED)
async def create_comment(message: str = Body(...)) -> str:
    current_index = max(comments_db) + 1 if comments_db else 0
    comments_db[current_index] = message
    return "Comment created!"


@app.put("/comments/{comment_id}", status_code=status.HTTP_200_OK)
async def update_comment(comment_id: int, message: str = Body(...)) -> str:
    if comment_id not in comments_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )
    comments_db[comment_id] = message
    return "Comment updated!"


@app.delete("/comments/{comment_id}", status_code=status.HTTP_200_OK)
async def delete_comment(comment_id: int) -> str:
    if comment_id not in comments_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    comments_db.pop(comment_id)
    return f"Comment deleted!"


#


@app.delete("/goals/{goal_id}", status_code=status.HTTP_200_OK)
async def delete_goal(goal_id: int) -> str:
    if goal_id not in goals_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goal not found")
    goals_db.pop(goal_id)
    return "Goal deleted!"


@app.put("/quotes/{quote_id}", status_code=status.HTTP_200_OK)
async def update_quote(quote_id: int, body: str = Body(...)) -> str:
    if quote_id not in quotes_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Quote not found")

    quotes_db[quote_id] = body
    return "Quote updated!"


@app.post("/reminders", status_code=status.HTTP_201_CREATED)
async def create_reminder(body: str = Body(...)) -> str:
    reminder_id = max(reminders_db) + 1 if reminders_db else 0
    reminders_db[reminder_id] = body
    return "Reminder created!"


@app.get("/tasks/{task_id}")
async def get_task(task_id: int) -> str:
    try:
        return tasks_db[task_id]
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )


@app.get("/notes")
async def get_notes() -> dict:
    return notes_db
