def individual_serial(manageClass) -> dict:
    return {
        "id": str(manageClass["_id"]),
        "teacher_id": manageClass["teacher_id"],
        "class_id": manageClass["class_id"],
        "student_id": manageClass["student_id"]
    }

def list_serial(manageClasses) -> list:
    return[individual_serial(manageClass) for manageClass in manageClasses]