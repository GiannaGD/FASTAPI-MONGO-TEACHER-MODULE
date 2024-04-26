from pydantic import BaseModel

class TeacherMaterials(BaseModel):
    teacher_id: str
    filename: str
    uploadDate: str