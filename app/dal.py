


def convert_objectId_to_string(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

def convert_objectId_to_string_of_all_docs(docs):
    return [convert_objectId_to_string(doc) for doc in docs]




def get_engineering_high_salary_employees(conn):
    pass

def get_employees_by_age_and_role(conn):
    pass

def get_top_seniority_employees_excluding_hr(conn):
    pass

def get_employees_by_age_or_seniority(conn):
    pass

def get_managers_excluding_departments(conn):
    pass


def get_employees_by_lastname_and_age(conn):
    pass