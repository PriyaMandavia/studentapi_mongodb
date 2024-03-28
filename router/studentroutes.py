from fastapi import APIRouter,Depends,HTTPException,status
from crud import studentcrud
from schemas import Students
from dependancy import oauth2_scheme,verify_token_access
from student_logging import set_log

logger = set_log(__name__)



router = APIRouter(tags=["students"])

#add the data
@router.post("/create_students", response_description="Add the new data")
def create_student_data(stud: Students, token: str = Depends(oauth2_scheme)):
    
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
        token= verify_token_access(token, credentials_exception)
        
        try:
            result = studentcrud.create_data(stud=stud)
            return result
        except Exception as e:
            logger.error(f"Exception is : {type(e).__name__}")

        

#find_all data
@router.get("/find_student_data")
def show_data(limit:int):
    try:
        result = studentcrud.find_data(limit=limit)
        return result
    except Exception as e:
        logger.error(f"Exception is : {type(e).__name__}")

#find only name
@router.get("/find_name")
def show_name():
    try:
        result = studentcrud.find_name()
        return result
    except Exception as e:
        logger.error(f"Exception is : {type(e).__name__}")

#find student field by search student name
@router.get("/show_field{name}")
def display_field(name: str):
    try:
        result = studentcrud.find_field(name=name)
        return result   
    except Exception as e :
        logger.error(f"Exception is : {type(e).__name__}")


#update data
@router.put("/update_data{name}")
def upgrade_data(name:str,stud : Students,token:str = Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                            detail="could not validate",
                                            headers={"WWW-Authenticate" : "bearer"})

    token = verify_token_access(token,credentials_exception)
    try:    
        result = studentcrud.update_data(name=name,stud=stud)
        return result
    except Exception as e :
        logger.error(f"Exception is : {type(e).__name__}")

#delete the data
@router.delete("/delete_data{name}")
def delete_student_data(name : str,token:str = Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                            detail="could not validate",
                                            headers={"WWW-Authenticate" : "bearer"})
        
        
    token = verify_token_access(token,credentials_exception)
    try:
            result = studentcrud.delete_data(name=name)
            return result
    except Exception as e :
            logger.error(f"Exception is : {type(e).__name__}")