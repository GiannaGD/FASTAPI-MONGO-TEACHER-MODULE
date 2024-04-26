from pydantic import BaseModel

class ManageClasses(BaseModel):
    teacher_id: str
    class_id: str
    student_id: str