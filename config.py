from dotenv import load_dotenv
import os

load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY',None)
ALGORITHM = os.environ.get('ALGORITHM',None)
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES',None)