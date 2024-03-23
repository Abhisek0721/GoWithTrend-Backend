from pydantic import BaseModel

class SignupSchema(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str