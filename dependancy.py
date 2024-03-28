from jose import JWTError,jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime,timedelta
from config import SECRET_KEY,ACCESS_TOKEN_EXPIRE_MINUTES,ALGORITHM








oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')





def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now()+ timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"expire": expire.strftime("%Y-%m-%d %H:%M:%S")})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token_access(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        print("payload:----" , payload)

        username: str = payload.get("user_name")

        if username is None:
            raise credentials_exception
        
        return username
    except JWTError as e:
        print(e)
        raise credentials_exception




    
