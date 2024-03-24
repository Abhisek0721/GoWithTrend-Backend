from pydantic import BaseModel

class ChangePasswordSchema(BaseModel):
    currentPassword: str
    newPassword: str

