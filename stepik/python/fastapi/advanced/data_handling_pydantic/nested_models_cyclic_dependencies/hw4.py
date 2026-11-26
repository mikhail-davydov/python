from pydantic import BaseModel


class Student(BaseModel):
    name: str
    grade: int


class Classroom(BaseModel):
    room_number: str
    students: list['Student']  # Строковая аннотация


class School(BaseModel):
    school_name: str
    classrooms: list['Classroom']  # Строковая аннотация
