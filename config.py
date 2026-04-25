from dotenv import load_dotenv
import os

load_dotenv()

CNPJ = (os.getenv("CNPJ") or "").strip()
SENHA = (os.getenv("SENHA") or "").strip()

if not CNPJ or not SENHA:
    raise RuntimeError(
        "Credenciais nao carregadas. Crie um arquivo .env na raiz com CNPJ e SENHA."
    )