from fastapi import FastAPI, APIRouter

app = FastAPI()

# --- 1. Маршрутизатор для блогов ---
# Этот роутер будет содержать только маршруты для блогов
# У него нет тегов на уровне APIRouter.
blog_router = APIRouter(prefix="/blogs")


@blog_router.get("/", summary="List all blogs", tags=["Blogs"])
async def list_blogs():
    """Получить список всех доступных блогов."""
    return [{"blog_id": 1, "title": "My Tech Blog"}, {"blog_id": 2, "title": "Travel Blog"}]


@blog_router.get("/{blog_id}", summary="Get a specific blog by ID", tags=["Blogs"])
async def get_blog(blog_id: int):
    """Получить детали конкретного блога по его уникальному идентификатору."""
    return {"blog_id": blog_id, "title": f"Blog {blog_id}"}


# --- 2. Маршрутизатор для постов ---
# Этот роутер будет содержать только маршруты для постов.
# У него нет тегов на уровне APIRouter.
post_router = APIRouter(prefix="/{blog_id}/posts")


@post_router.get("/", summary="List posts for a specific blog", tags=["Posts"])
async def list_posts(blog_id: int):
    """Получить список постов, принадлежащих конкретному блогу."""
    return [{"post_id": 1, "blog_id": blog_id, "title": "Post 1"},
            {"post_id": 2, "blog_id": blog_id, "title": "Post 2"}]


@post_router.get("/{post_id}", summary="Get a specific post by ID", tags=["Posts"])
async def get_post(blog_id: int, post_id: int):
    """Получить детали одного поста внутри конкретного блога."""
    return {"post_id": post_id, "blog_id": blog_id, "title": f"Post {post_id}"}


# --- 3. Маршрутизатор для комментариев ---
# Этот роутер будет содержать только маршруты для комментариев.
# У него нет тегов на уровне APIRouter.
comment_router = APIRouter(prefix="/{post_id}/comments")


@comment_router.get("/", summary="List comments for a specific post", tags=["Comments"])
async def list_comments(blog_id: int, post_id: int):
    """Получить список комментариев, связанных с конкретным постом."""
    return [{"comment_id": 1, "post_id": post_id, "text": "Comment 1"},
            {"comment_id": 2, "post_id": post_id, "text": "Comment 2"}]


@comment_router.get("/{comment_id}", summary="Get a specific comment by ID", tags=["Comments"])
async def get_comment(blog_id: int, post_id: int, comment_id: int):
    """Получить детали одного комментария внутри конкретного поста."""
    return {"comment_id": comment_id, "post_id": post_id,
            "text": f"Comment {comment_id} on post {post_id}"}


# --- Сборка маршрутизаторов ---
post_router.include_router(comment_router)

blog_router.include_router(post_router)

app.include_router(blog_router)
