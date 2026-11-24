from fastapi import FastAPI, APIRouter

app = FastAPI()

employee_router = APIRouter(prefix="/employees/{emp_id}", tags=["Employees"])


@employee_router.get("/")
def get_employee(dept_id: int, team_id: int, emp_id: int):
    return f"This is employee {emp_id} in team {team_id}, department {dept_id}"


team_router = APIRouter(prefix="/teams/{team_id}", tags=["Teams"])

team_router.include_router(employee_router)


@team_router.get("/")
def get_team(dept_id: int, team_id: int):
    return f"This is team {team_id} in department {dept_id}"


department_router = APIRouter(prefix="/departments/{dept_id}", tags=["Departments"])

department_router.include_router(team_router)


@department_router.get("/")
def get_department(dept_id: int):
    return f"This is department {dept_id}"


company_router = APIRouter(prefix="/company", tags=["Company"])

company_router.include_router(department_router)


@company_router.get("/")
def get_company():
    return "This is the company level"


app.include_router(company_router, prefix="/api")
