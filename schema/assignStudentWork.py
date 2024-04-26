def individual_serial(assignStudent) -> dict:
    return {
        "id": str(assignStudent["_id"]),
        "teacher_id": assignStudent["teacher_id"],        
        "student_id": assignStudent["student_id"],
        "document_id": assignStudent["document_id"],
        "marks_obtained": assignStudent["marks_obtained"],
        "teacher_feedback": assignStudent["teacher_feedback"]
    }

def list_serial(assignStudents) -> list:
    return[individual_serial(assignStudent) for assignStudent in assignStudents]