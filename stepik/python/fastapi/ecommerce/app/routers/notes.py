from fastapi import APIRouter

router = APIRouter(
    prefix="/notes",
    tags=["notes"]
)


@router.get("/")
async def get_all_notes():
    """
    Возвращает список всех категорий товаров.
    """
    return "Notes API is working"
