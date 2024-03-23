from dotenv import load_dotenv
import os

# load .env constants
load_dotenv()

class Constants:
    PORT:int                = int(os.getenv("PORT"))
    DATABASE_NAME:str       = os.getenv("DATABASE_NAME")
    DB_USERNAME:str         = os.getenv("DB_USERNAME")
    DB_PASSWORD:str         = os.getenv("DB_PASSWORD")
    DB_DOMAIN:str           = os.getenv("DB_DOMAIN")
    TOKEN_EXPIRATION:int    = int(os.getenv("TOKEN_EXPIRATION"))
    JWT_SECRET_KEY:str      = os.getenv("JWT_SECRET_KEY")
