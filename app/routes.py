from fastapi import APIRouter
from connection import get_con_db
from dal import *

route = APIRouter(prefix="/employees")


@route.get("/engineering/high-salary")
def engineering_high_salary_employees():
    conn = get_con_db()
    return get_engineering_high_salary_employees(conn)

@route.get("/by-age-and-role")
def employees_by_age_and_role():
    conn = get_con_db()
    return get_employees_by_age_and_role(conn)


@route.get("/top-seniority")
def top_seniority_employees_excluding_hr():
    conn = get_con_db()
    return get_top_seniority_employees_excluding_hr(conn)

@route.get("/age-or-seniority")
def employees_by_age_or_seniority():
    conn = get_con_db()
    return get_employees_by_age_or_seniority(conn)

@route.get("/managers/excluding-departments")
def managers_excluding_departments():
    conn = get_con_db()
    return get_managers_excluding_departments(conn)

@route.get("/by-lastname-and-age")
def employees_by_lastname_and_age():
    conn = get_con_db()
    return get_employees_by_lastname_and_age(conn)






