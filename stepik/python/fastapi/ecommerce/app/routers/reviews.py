from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.db_depends import get_async_db
from app.models.products import Product
from app.models.reviews import Review as ReviewModel
from app.models.users import User as UserModel
from app.schemas import ReviewCreate, Review as ReviewSchema

router = APIRouter(prefix="/reviews", tags=["reviews"])


async def _update_product_rating(db: AsyncSession, product_id: int) -> None:
    """Пересчитывает средний рейтинг товара на основе активных отзывов."""
    result = await db.execute(
        select(func.coalesce(func.avg(ReviewModel.grade), 0.0))
        .where(ReviewModel.product_id == product_id, ReviewModel.is_active.is_(True))
    )
    avg_rating = result.scalar_one()
    product = await db.get(Product, product_id)
    if product:
        product.rating = float(avg_rating)
        await db.commit()


@router.get("/", response_model=list[ReviewSchema])
async def get_all_reviews(db: AsyncSession = Depends(get_async_db)):
    """
    Получение всех активных отзывов.
    Доступен всем пользователям без аутентификации.
    """
    result = await db.execute(
        select(ReviewModel).where(ReviewModel.is_active.is_(True))
    )
    return result.scalars().all()


@router.post("/", response_model=ReviewSchema, status_code=status.HTTP_201_CREATED)
async def create_review(
    review_data: ReviewCreate,
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """
    Создание нового отзыва о товаре.
    Доступно только для пользователей с ролью 'buyer'.
    """
    if current_user.role != "buyer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only buyers can create reviews",
        )

    product = await db.get(Product, review_data.product_id)
    if product is None or not product.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product not found or inactive",
        )

    existing = await db.execute(
        select(ReviewModel)
        .where(
            ReviewModel.user_id == current_user.id,
            ReviewModel.product_id == review_data.product_id,
            ReviewModel.is_active.is_(True),
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="You have already reviewed this product",
        )

    new_review = ReviewModel(
        user_id=current_user.id,
        product_id=review_data.product_id,
        comment=review_data.comment or "",
        grade=review_data.grade,
    )
    db.add(new_review)
    await db.commit()
    await db.refresh(new_review)

    await _update_product_rating(db, review_data.product_id)

    return new_review


@router.delete("/{review_id}", response_model=dict)
async def delete_review(
    review_id: int,
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_async_db),
):
    """
    Мягкое удаление отзыва (установка is_active = False).
    Доступно автору отзыва или пользователям с ролью 'admin'.
    """
    review = await db.get(ReviewModel, review_id)
    if review is None or not review.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found or already deleted",
        )

    if review.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only the review author or admin can delete this review",
        )

    review.is_active = False
    await db.commit()

    await _update_product_rating(db, review.product_id)

    return {"message": "Review deleted"}
