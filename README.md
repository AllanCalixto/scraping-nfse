# Scraping NFSe com Selenium

Automacao em Python para acessar e interagir com o portal NFSe usando Selenium.

## Tecnologias

- Python 3
- Selenium
- python-dotenv

## Como rodar

1. Clone o repositorio e entre na pasta:

```bash
git clone https://github.com/SEU_USUARIO/scraping-nfse.git
cd scraping-nfse
```

2. Crie e ative o ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

3. Instale as dependencias:

```bash
python -m pip install -r requirements.txt
```

4. Crie o arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

Depois, edite o `.env` com suas credenciais:

```env
CNPJ=seu_cnpj
SENHA=sua_senha
```

5. Execute o projeto:

```bash
python main.py
```
