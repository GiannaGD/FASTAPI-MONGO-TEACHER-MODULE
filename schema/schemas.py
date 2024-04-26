def individual_serial(teacher) -> dict:
    return {
        "id": str(teacher["_id"]),
        "name": teacher["name"],
        "address": teacher["address"],
        "status": teacher["status"]
    }

def list_serial(teachers) -> list:
    return[individual_serial(teacher) for teacher in teachers]