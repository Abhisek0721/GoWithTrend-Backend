from pydantic import BaseModel

class UpdateUserSchema(BaseModel):
    firstName: str
    lastName: str

