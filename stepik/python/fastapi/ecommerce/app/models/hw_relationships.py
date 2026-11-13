from decimal import Decimal

from sqlalchemy import String, ForeignKey, Text, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# 1-to-many
class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)

    orders: Mapped[list["Order"]] = relationship(
        "Order",
        back_populates="customer",
        lazy="joined",
        cascade="all, delete-orphan"
    )


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_number: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id"),
        nullable=False,
        index=True
    )

    customer: Mapped["Customer"] = relationship(
        "Customer",
        back_populates="orders"
    )


# 1-to-many
class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="category",
        lazy="joined",
        cascade="all, delete-orphan"
    )


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"),
        nullable=False,
        index=True
    )

    category: Mapped["Category"] = relationship(
        "Category",
        back_populates="products"
    )


# 1-to-1
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    profile: Mapped["Profile"] = relationship(
        "Profile",
        uselist=False,
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="profile"
    )


# 1-to-many
class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    books: Mapped[list["Book"]] = relationship(
        "Book",
        back_populates="author",
        cascade='all, delete-orphan'
    )


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=False, index=True)
    author: Mapped["Author"] = relationship(
        "Author",
        back_populates="books"
    )
