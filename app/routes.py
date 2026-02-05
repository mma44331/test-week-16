from fastapi import APIRouter
from connection import get_con_db
from dal import *

route = APIRouter(prefix="/employees")


@route.get("/engineering/high-salary")
def get_all():
    conn = get_con_db()
    return get_engineering_high_salary_employees(conn)

@route.get("/by-age-and-role")
def get_all():
    conn = get_con_db()
    return get_employees_by_age_and_role(conn)


@route.get("/top-seniority")
def get_all():
    conn = get_con_db()
    return get_top_seniority_employees_excluding_hr(conn)

@route.get("/age-or-seniority")
def get_all():
    conn = get_con_db()
    return get_employees_by_age_or_seniority(conn)

@route.get("/managers/excluding-departments")
def get_all():
    conn = get_con_db()
    return get_managers_excluding_departments(conn)

@route.get("/by-lastname-and-age")
def get_all():
    conn = get_con_db()
    return get_employees_by_lastname_and_age(conn)






