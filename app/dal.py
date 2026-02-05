def convert_objectId_to_string(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

def convert_objectId_to_string_of_all_docs(docs):
    return [convert_objectId_to_string(doc) for doc in docs]





def get_engineering_high_salary_employees(conn):
    data = []
    for item in conn.find({"job_role.department":"Engineering","salary":{"$gt":65000}},{"_id":0,"employee_id":1,"name":1,"salary":1}):
        data.append(convert_objectId_to_string(item))
    return data


def get_employees_by_age_and_role(conn):
    data = []
    for item in conn.find({"$or":[{"job_role.title":"Engineer"},{"job_role.title":"Specialist"}],"age":{"$gt":29,"$lt":46}}):
        data.append(convert_objectId_to_string(item))
    return data


def get_top_seniority_employees_excluding_hr(conn):
    data = []
    for item in conn.find({"job_role.department":{"$ne":"HR"}}).sort("years_at_company", -1).limit(7):
        data.append(convert_objectId_to_string(item))
    return data




def get_employees_by_age_or_seniority(conn):
    data = []
    for item in conn.find({"$or":[{"age":{"$gt":50}},{"years_at_company":{"$lt":3}}]},{"_id":0,"employee_id":1,"name":1,"age":1,"years_at_company":1}):
        data.append(convert_objectId_to_string(item))
    return data



def get_managers_excluding_departments(conn):
    data = []
    for item in conn.find({"job_role.title":"Manager","job_role.department":{"$nin":["Marketing","Sales"]}}):
        data.append(convert_objectId_to_string(item))
    return data




def get_employees_by_lastname_and_age(conn):
    data = []
    for item in conn.find({"$or": [{"name":{"$regex":"Nelson$"}}, {"name":{"$regex":"Wright$"}}],"age":{"$lt":35}},{"_id": 0,"name": 1, "age": 1, "job_role.department": 1}):
        data.append(convert_objectId_to_string(item))
    return data

