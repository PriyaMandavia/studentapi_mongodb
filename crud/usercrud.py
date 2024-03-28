from database import user_collection
from pymongo.results import InsertOneResult
import schemas
from utils import hash_pass,verify_password
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends,status,HTTPException,security
from dependancy import oauth2_scheme,verify_token_access



def createuser(user : schemas.CreateUser):
    hash_password = hash_pass(user.password)
    password = hash_password


    user_dict = {"email" : user.email,
                 "password" : password}
    

    user_collection.insert_one(user_dict)
    return {"msg" : "successfully create a user"}

def loginuser(user : OAuth2PasswordRequestForm=Depends()):
    login = user_collection.find_one({"email" : user.username})
    if not login:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"user not exits")
    if not verify_password(user.password,login['password']):
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="password not match")
    return user


def get_current_user(token : str =  Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="could not validate",
                                          headers={"WWW-Authenticate" : "bearer"})
    
    token = verify_token_access(token,credentials_exception)
    return token
    
