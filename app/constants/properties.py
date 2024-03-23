from dotenv import load_dotenv
import os

# load .env constants
load_dotenv()

class Constants:
    PORT:int = int(os.getenv("PORT"))

