from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from app.db_depends import get_db
from app.models.categories import Category as CategoryModel
from app.models.products import Product as ProductModel
from app.schemas import Product as ProductSchema, ProductCreate

# Создаём маршрутизатор для товаров
router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("/")
async def get_all_products(db: Session = Depends(get_db)):
    """
    Возвращает список всех активных товаров.
    """
    stmt = select(ProductModel).where(ProductModel.is_active == True)
    products = db.scalars(stmt).all()
    return products


@router.post("/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Создаёт новый товар.
    """
    # Проверка существования активной категории
    stmt = select(CategoryModel).where(
        CategoryModel.id == product.category_id,
        CategoryModel.is_active == True,
    )
    category = db.scalars(stmt).first()
    if category is None:
        raise HTTPException(
            status_code=400,
            detail="Category not found or inactive",
        )

    # Создание нового товара
    db_product = ProductModel(**product.model_dump(), is_active=True)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/category/{category_id}")
async def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    """
    Возвращает список активных товаров в указанной категории.
    """
    # Проверка существования активной категории
    stmt = select(CategoryModel).where(
        CategoryModel.id == category_id,
        CategoryModel.is_active == True,
    )
    category = db.scalars(stmt).first()
    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found or inactive",
        )

    # Получение активных товаров категории
    stmt = select(ProductModel).where(
        ProductModel.category_id == category_id,
        ProductModel.is_active == True,
    )
    products = db.scalars(stmt).all()
    return products


@router.get("/{product_id}")
async def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Возвращает детальную информацию о товаре.
    """
    # Проверка существования активного товара
    stmt = select(ProductModel).where(
        ProductModel.id == product_id,
        ProductModel.is_active == True,
    )
    product = db.scalars(stmt).first()
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found or inactive",
        )

    # Проверка существования активной категории товара
    cat_stmt = select(CategoryModel).where(
        CategoryModel.id == product.category_id,
        CategoryModel.is_active == True,
    )
    category = db.scalars(cat_stmt).first()
    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Category not found or inactive",
        )

    return product


@router.put("/{product_id}", response_model=ProductSchema)
async def update_product(
        product_id: int, product: ProductCreate, db: Session = Depends(get_db)
):
    """
    Обновляет существующий товар.
    """
    # Проверка существования активного товара
    stmt = select(ProductModel).where(
        ProductModel.id == product_id,
        ProductModel.is_active == True,
    )
    db_product = db.scalars(stmt).first()
    if db_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found or inactive",
        )

    # Проверка существования активной категории
    cat_stmt = select(CategoryModel).where(
        CategoryModel.id == product.category_id,
        CategoryModel.is_active == True,
    )
    category = db.scalars(cat_stmt).first()
    if category is None:
        raise HTTPException(
            status_code=400,
            detail="Category not found or inactive",
        )

    # Обновление товара
    db.execute(
        update(ProductModel)
        .where(ProductModel.id == product_id)
        .values(**product.model_dump())
    )
    db.commit()
    db.refresh(db_product)
    return db_product


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Логически удаляет товар, устанавливая is_active=False.
    """
    # Проверка существования активного товара
    stmt = select(ProductModel).where(
        ProductModel.id == product_id,
        ProductModel.is_active == True,
    )
    product = db.scalars(stmt).first()
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found or inactive",
        )

    # Логическое удаление
    db.execute(
        update(ProductModel)
        .where(ProductModel.id == product_id)
        .values(is_active=False)
    )
    db.commit()

    return {"status": "success", "message": "Product marked as inactive"}
