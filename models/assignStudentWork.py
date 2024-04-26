from pydantic import BaseModel

class AssignStudentWork(BaseModel):
    teacher_id: str    
    student_id: str
    document_id: str
    marks_obtained: str
    teacher_feedback: str