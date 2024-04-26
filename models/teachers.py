from pydantic import BaseModel

class Teacher(BaseModel):
    name: str
    address: str
    status: bool