from fastapi import APIRouter,Depends
from typing import Any
from crud import usercrud
import schemas
from fastapi.security import OAuth2PasswordRequestForm
from dependancy import create_access_token
from student_logging import set_log

logger = set_log(__name__)



router = APIRouter(tags=["user"])


@router.post("/create_user")
def create_user(user : schemas.CreateUser):
    try:
        result = usercrud.createuser(user=user)
        return result
    except Exception as e :
        logger.error(f"Exception is : {type(e).__name__}")
        

@router.post("/login" , response_model=schemas.Token)
def login_user(user : OAuth2PasswordRequestForm=Depends()):
    try:
        result = usercrud.loginuser(user=user)
        access_token = create_access_token(data={"user_name": result.username})  
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        logger.error(f"Exception is : {type(e).__name__}")



@router.get("/current_user")
def read_user(current_user:Any=Depends(usercrud.get_current_user)):
    try:
        return {"current_user" : current_user}
    except Exception as e :
        logger.error(f"Exception is : {type(e).__name__}")

    