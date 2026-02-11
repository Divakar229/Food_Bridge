from pydantic import BaseModel,EmailStr


class AdminCreate(BaseModel):
    email:EmailStr
    password:str

class AdminResponse(BaseModel):
    id:int
    email:EmailStr

    class config:
        from_attributes=True

class Token(BaseModel):
    access_token:str
    token_type:str