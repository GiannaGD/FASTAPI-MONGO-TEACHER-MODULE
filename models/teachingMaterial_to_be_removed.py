from pydantic import BaseModel

class ManageClasses(BaseModel):
    teacher_id: str
    doc: str
    description: str