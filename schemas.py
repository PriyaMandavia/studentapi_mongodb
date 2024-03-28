
from pydantic import BaseModel,EmailStr,validator
from typing import Union
import re




 
class Students(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Union[str,None] = "0"
    field : str
    gpa : int

    @validator('phone_number')
    def phone(cls,v):
        if  len(v) < 10:
            raise ValueError("number must be atleast ten digit")
        return v


class CreateUser(BaseModel):
    email : EmailStr
    password : str 

    @validator('password')
    def pwd(cls,v):
        p= ("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$")
        if not re.match(p,v):
            raise ValueError("Must be enter minimum six characters, at least one upper and lower letter, one number and one special character:")
        return v
    
    @validator('email')
    def email_valid(cls,v):
        if not v.islower():
            raise ValueError("please enter email in small letter")
        return v
    

class Token(BaseModel):
    access_token: str
    token_type: str


