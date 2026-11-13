import datetime
from decimal import Decimal

from sqlalchemy import String, Numeric, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Recipe(Base):
    __tablename__ = 'recipes'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    cooking_time: Mapped[int] = mapped_column(nullable=False)
    ingredients: Mapped[str] = mapped_column(Text, nullable=False)
    calories: Mapped[int | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        nullable=False, default=datetime.datetime.now
    )


class Car(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(50), nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    is_available: Mapped[bool] = mapped_column(nullable=False, default=True)


class Event(Base):
    __tablename__ = 'events'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    start_time: Mapped[datetime.datetime] = mapped_column(nullable=False)
    end_time: Mapped[datetime.datetime | None] = mapped_column(nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)


class Movie(Base):
    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    duration: Mapped[int] = mapped_column(nullable=False)
    release_date: Mapped[datetime.date | None] = mapped_column(nullable=True)


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    stock_quantity: Mapped[int] = mapped_column(default=0, nullable=False)


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    is_completed: Mapped[bool] = mapped_column(nullable=False, default=False)


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)


if __name__ == "__main__":
    from sqlalchemy.schema import CreateTable

    print(CreateTable(Recipe.__table__))
    print(CreateTable(Car.__table__))
    print(CreateTable(Event.__table__))
    print(CreateTable(Movie.__table__))
    print(CreateTable(Product.__table__))
    print(CreateTable(Task.__table__))
    print(CreateTable(Category.__table__))
