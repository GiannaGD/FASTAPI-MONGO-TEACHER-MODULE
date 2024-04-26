def individual_serial(teachingMaterial) -> dict:
    return {
        "id": str(teachingMaterial["_id"]),
        "teacher_id": teachingMaterial["teacher_id"],
        "doc": teachingMaterial["doc"],
        "description": teachingMaterial["description"]
    }

def list_serial(teachingMaterials) -> list:
    return[individual_serial(teachingMaterial) for teachingMaterial in teachingMaterials]