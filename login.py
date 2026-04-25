from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CNPJ, SENHA

def login_nfse(driver):
    driver.get("https://www.nfse.gov.br/EmissorNacional/")
    wait = WebDriverWait(driver, 10)

    campo_cnpj = wait.until(
        EC.visibility_of_element_located((By.ID, "Inscricao"))
    )

    campo_senha = wait.until(
        EC.visibility_of_element_located((By.ID, "Senha"))
    )

    campo_cnpj.clear()
    campo_senha.clear()

    campo_cnpj.send_keys(CNPJ)
    campo_senha.send_keys(SENHA)

    btn_entrar = driver.find_element(By.XPATH, "//button")
    btn_entrar.click()

    return driver