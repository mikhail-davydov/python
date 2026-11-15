from datetime import date, datetime

from sqlalchemy import String, ForeignKey, Text, Table, Column, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# task 4 (many-to-many)
class Participation(Base):
    __tablename__ = "participations"

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"), primary_key=True
    )
    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id"), primary_key=True
    )
    role: Mapped[str] = mapped_column(String(50), nullable=False)

    project: Mapped["Project"] = relationship(back_populates="participations")
    employee: Mapped["Employee"] = relationship(back_populates="participations")


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    start_date: Mapped[date] = mapped_column(nullable=False)

    participations: Mapped[list["Participation"]] = relationship(
        back_populates="project",
        single_parent=True,
    )

    employees: Mapped[list["Employee"]] = relationship(
        "Employee",
        secondary="participations",
        back_populates="projects",
        viewonly=True,
    )


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)

    participations: Mapped[list["Participation"]] = relationship(
        back_populates="employee",
        single_parent=True,
    )

    projects: Mapped[list["Project"]] = relationship(
        "Project",
        secondary="participations",
        back_populates="employees",
        viewonly=True,
    )


# task 3 (many-to-many)
article_tags = Table(
    "article_tags",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("articles.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    tags: Mapped[list["Tag"]] = relationship(
        "Tag",
        secondary=article_tags,
        back_populates="articles"
    )


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    articles: Mapped[list["Article"]] = relationship(
        "Article",
        secondary=article_tags,
        back_populates="tags"
    )


# task 2 (1-to-many)
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, default=datetime.now
    )

    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="post",
        cascade="all, delete-orphan"
    )


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, default=datetime.now
    )
    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id"),
        nullable=False,
        index=True
    )

    post: Mapped["Post"] = relationship(
        "Post",
        back_populates="comments"
    )


# task 1 (1-to-many)
class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    student_number: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)

    grades: Mapped[list["Grade"]] = relationship(
        "Grade",
        back_populates="student",
        cascade="all, delete-orphan"
    )


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[int] = mapped_column(nullable=False)
    subject: Mapped[str] = mapped_column(String(50), nullable=False)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    student: Mapped["Student"] = relationship(
        "Student",
        back_populates="grades"
    )
