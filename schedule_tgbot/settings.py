from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.dirname(__file__), '.env')
env = os.environ.get
load_dotenv()


TOKEN = env("TOKEN")

START_MESSAGE="""Привет, добро пожаловать в бот Школы Kenji!
Используй команды, чтобы получить информацию о расписании и секциях:"""