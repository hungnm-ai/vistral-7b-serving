import os

from dotenv import load_dotenv
load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')
MODEL_NAME = "Viet-Mistral/Vistral-7B-Chat"