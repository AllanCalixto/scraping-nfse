from dotenv import load_dotenv
import os

load_dotenv()

CNPJ = os.getenv("CNPJ")
SENHA = os.getenv("SENHA")

if not CNPJ or not SENHA:
    raise Exception("CNPJ ou SENHA não carregados do .env")