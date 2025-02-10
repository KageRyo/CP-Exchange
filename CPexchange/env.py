import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
load_dotenv(BASE_DIR / 'web.env')

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'