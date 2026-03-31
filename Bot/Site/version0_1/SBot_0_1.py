from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import os
import hashlib

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from data0_1.database import salvar_projeto, criar_banco, projeto_existe
import pandas as pd
import dotenv

# Configuração do navegador
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--user-data-dir=workana_profile")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

dotenv.load_dotenv()
PATH_LINKS = os.getenv("CATEGORIES_PATH")
data = pd.read_csv(PATH_LINKS, sep=";")
dados = []
for i in range(len(data)):
    #print(f"Processando categoria: {data.columns}")
    categoria = data.loc[i, "Nome"]
    link = data.loc[i, "Link"]

    driver.get(link)
    jobs = driver.find_elements(By.CSS_SELECTOR, "a[href*='/job/']")
    for job in jobs:
        try:
            titulo = job.text
            link = job.get_attribute("href")

            if link:
                dados.append({
                    "categoria": categoria,
                    "titulo": titulo,
                    "link": link
                })

        except:
            pass

# Remover duplicados
links_unicos = list({d['link']: d for d in dados}.values())


# Abrir cada projeto
for item in links_unicos:
    # Criar hash antes
    hash_id = hashlib.sha256(
            f"{item['categoria']}{item['titulo']}{item['link']}".encode()
        ).hexdigest()

    # Verificar se já existe
    if projeto_existe(hash_id):
        print("Projeto já cadastrado:", item['link'])
        continue

    print("Novo projeto:", item['link'])

    driver.get(item['link'])
    time.sleep(3)


    try:
        titulo = driver.find_element(By.TAG_NAME, "h1").text
    except:
        titulo = item['titulo']


    # Descrição
    try:
        descricao = driver.find_element(By.TAG_NAME, "body").text
    except:
        descricao = ""


    # Cliente verificado
    try:
        driver.find_element(
            By.XPATH,
            "//*[contains(text(),'Cliente verificado')]"
        )
        cliente_verificado = True
    except:
        cliente_verificado = False


    # Pagamento verificado
    try:
        driver.find_element(
            By.XPATH,
            "//*[contains(text(),'Pagamento verificado')]"
        )
        cliente_pagamento = True
    except:
        cliente_pagamento = False


    # Histórico cliente
    try:
        cliente_historico = driver.find_element(
            By.XPATH,
            "//*[contains(text(),'projetos publicados')]"
        ).text
    except:
        cliente_historico = ""

    # Considerar enviar proposta se o cliente for verificado ou tiver pagamento verificado
    enviar_proposta = False

    # Salvar banco
    salvar_projeto(
        item['categoria'],
        titulo,
        item['link'],
        descricao,
        hash_id,
        cliente_verificado,
        cliente_pagamento,
        cliente_historico
    )


driver.quit()