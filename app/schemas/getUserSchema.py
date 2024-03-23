from pydantic import BaseModel

class GetUserSchema(BaseModel):
    userId:str
    firstName:str
    lastName:str
    email: str