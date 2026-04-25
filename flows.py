from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, datetime
import time


def new_nfse(driver):
    print("Entrou após login no sistema NFSe")

    wait = WebDriverWait(driver, 20)
    btn_nova_nfse = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a.btnAcesso[href="/EmissorNacional/DPS/Pessoas"]')
        )
    )
    btn_nova_nfse.click()

    campo_data_competencia = wait.until(
        EC.visibility_of_element_located((By.ID, "DataCompetencia"))
    )
    campo_data_competencia.clear()
    campo_data_competencia.send_keys(date.today().strftime("%d-%m-%Y"))
    campo_data_competencia.send_keys(Keys.TAB)
    campo_data_competencia.send_keys(Keys.TAB)

    # Aguarda a pagina reagir ao TAB e renderizar os radios corretamente.
    time.sleep(1.5)

    radio_tomador_brasil = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'input[name="Tomador.LocalDomicilio"][value="1"]')
        )
    )
    label_tomador_brasil = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'radiobutton')]//label[.//input[@name='Tomador.LocalDomicilio' and @value='1'] and contains(normalize-space(.), 'Brasil')]",
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
        label_tomador_brasil,
    )

    try:
        label_tomador_brasil.click()
    except Exception:
        driver.execute_script("arguments[0].click();", label_tomador_brasil)

    if not radio_tomador_brasil.is_selected():
        driver.execute_script(
            """
            arguments[0].checked = true;
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            """,
            radio_tomador_brasil,
        )

    time.sleep(0.5)
    campo_tomador_inscricao = wait.until(
        EC.visibility_of_element_located((By.ID, "Tomador_Inscricao"))
    )
    campo_tomador_inscricao.clear()
    campo_tomador_inscricao.send_keys("60.507.706/0001-76")
    campo_tomador_inscricao.send_keys(Keys.TAB)

    time.sleep(0.5)
    wait.until(EC.presence_of_element_located((By.ID, "btnAvancar")))
    btn_avancar = wait.until(EC.element_to_be_clickable((By.ID, "btnAvancar")))
    url_antes_avancar = driver.current_url
    btn_avancar.click()
    wait.until(lambda d: d.current_url != url_antes_avancar)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    return driver


def new_nfse_service(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # Garante que estamos na tela de servicos apos o avancar.
    wait.until(
        EC.presence_of_element_located((By.ID, "LocalPrestacao_CodigoMunicipioPrestacao"))
    )

    seletor_municipio = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "span.select2-selection.select2-selection--single[aria-labelledby='select2-LocalPrestacao_CodigoMunicipioPrestacao-container']",
            )
        )
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
        seletor_municipio,
    )
    try:
        seletor_municipio.click()
    except Exception:
        driver.execute_script("arguments[0].click();", seletor_municipio)

    campo_busca_municipio = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "input.select2-search__field[aria-controls='select2-LocalPrestacao_CodigoMunicipioPrestacao-results']",
            )
        )
    )
    campo_busca_municipio.clear()
    campo_busca_municipio.send_keys("Fortaleza")
    time.sleep(0.5)
    campo_busca_municipio.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.3)
    campo_busca_municipio.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.3)
    campo_busca_municipio.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.3)
    campo_busca_municipio.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.3)
    campo_busca_municipio.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.3)
    campo_busca_municipio.send_keys(Keys.ENTER)
    time.sleep(0.5)

    body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body.send_keys(Keys.TAB)
    time.sleep(0.3)
    body.send_keys(Keys.ENTER)

    seletor_codigo_tributacao = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "span.select2-selection.select2-selection--single[aria-labelledby='select2-ServicoPrestado_CodigoTributacaoNacional-container']",
            )
        )
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
        seletor_codigo_tributacao,
    )
    driver.execute_script("arguments[0].focus();", seletor_codigo_tributacao)
    try:
        seletor_codigo_tributacao.click()
    except Exception:
        driver.execute_script("arguments[0].click();", seletor_codigo_tributacao)

    campo_busca_codigo_tributacao = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "input.select2-search__field[aria-controls='select2-ServicoPrestado_CodigoTributacaoNacional-results']",
            )
        )
    )
    campo_busca_codigo_tributacao.clear()
    campo_busca_codigo_tributacao.send_keys("010601")
    time.sleep(0.5)
    campo_busca_codigo_tributacao.send_keys(Keys.ENTER)
    time.sleep(0.5)
    campo_busca_codigo_tributacao.send_keys(Keys.ENTER)
    time.sleep(1.0)

    radio_exportacao_nao = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[name='ServicoPrestado.HaExportacaoImunidadeNaoIncidencia'][value='0']",
            )
        )
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
        radio_exportacao_nao,
    )
    driver.execute_script("arguments[0].focus();", radio_exportacao_nao)
    try:
        radio_exportacao_nao.click()
    except Exception:
        driver.execute_script("arguments[0].click();", radio_exportacao_nao)

    time.sleep(0.5)
    body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body.send_keys(Keys.TAB)

    campo_descricao_servico = wait.until(
        EC.presence_of_element_located((By.ID, "ServicoPrestado_Descricao"))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
        campo_descricao_servico,
    )
    driver.execute_script("arguments[0].focus();", campo_descricao_servico)
    try:
        campo_descricao_servico.click()
    except Exception:
        driver.execute_script("arguments[0].click();", campo_descricao_servico)

    meses_pt = [
        "janeiro",
        "fevereiro",
        "marco",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
    ]
    agora = datetime.now()
    mes_atual = meses_pt[agora.month - 1]
    ano_atual = agora.year
    descricao = (
        "Assessoria e consultoria em informatica(Automacao de processos) - "
        f"{mes_atual} {ano_atual}."
    )
    campo_descricao_servico.clear()
    campo_descricao_servico.send_keys(descricao)

    seletor_codigo_nbs = wait.until(
        EC.presence_of_element_located((By.ID, "ServicoPrestado_CodigoNBS_chosen"))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
        seletor_codigo_nbs,
    )
    driver.execute_script("arguments[0].focus();", seletor_codigo_nbs)

    seletor_codigo_nbs_click = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#ServicoPrestado_CodigoNBS_chosen a.chosen-single")
        )
    )
    try:
        seletor_codigo_nbs_click.click()
    except Exception:
        driver.execute_script("arguments[0].click();", seletor_codigo_nbs_click)

    campo_busca_codigo_nbs = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#ServicoPrestado_CodigoNBS_chosen .chosen-search input")
        )
    )
    campo_busca_codigo_nbs.clear()
    campo_busca_codigo_nbs.send_keys("115011000")
    campo_busca_codigo_nbs.send_keys(Keys.ENTER)

    btn_avancar_servico = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//button[@type='submit' and contains(@class,'btn-primary') and .//span[normalize-space()='Avancar' or normalize-space()='Avançar']]",
            )
        )
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
        btn_avancar_servico,
    )
    try:
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@type='submit' and contains(@class,'btn-primary') and .//span[normalize-space()='Avancar' or normalize-space()='Avançar']]",
                )
            )
        ).click()
    except Exception:
        driver.execute_script("arguments[0].click();", btn_avancar_servico)

    time.sleep(2.5)
    return driver


def new_nfse_valours(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    wait.until(
        EC.presence_of_element_located((By.ID, "Valores_ValorServico"))
    )

    campo_valor_servico = wait.until(
        EC.presence_of_element_located((By.ID, "Valores_ValorServico"))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
        campo_valor_servico,
    )
    driver.execute_script("arguments[0].focus();", campo_valor_servico)
    try:
        campo_valor_servico.click()
    except Exception:
        driver.execute_script("arguments[0].click();", campo_valor_servico)

    campo_valor_servico.clear()
    campo_valor_servico.send_keys("0000")
    campo_valor_servico.send_keys(Keys.TAB)


    radio_tipo_tributo_3 = wait.until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "input[name='ValorTributos.TipoValorTributos'][value='3']",
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
        radio_tipo_tributo_3,
    )

    try:
        radio_tipo_tributo_3.click()
    except Exception:
        driver.execute_script("arguments[0].click();", radio_tipo_tributo_3)

    # Garantia extra (igual você já fez antes)
    if not radio_tipo_tributo_3.is_selected():
        driver.execute_script(
            """
            arguments[0].checked = true;
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            """,
            radio_tipo_tributo_3,
        )

    driver.execute_script("document.querySelector('button[type=\"submit\"]').closest('form').submit();")


    time.sleep(0.5)

    


    return driver