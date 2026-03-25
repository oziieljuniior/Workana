from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
from database import salvar_projeto


# Configuração do navegador
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--user-data-dir=workana_profile")

driver = webdriver.Chrome(options=options)

url = "https://www.workana.com/jobs?category=it-programming&language=xx&subcategory=data-science-1%2Cartificial-intelligence-1"
driver.get(url)

time.sleep(5)

# Scroll para carregar mais projetos
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

# Buscar projetos
jobs = driver.find_elements(By.CSS_SELECTOR, "a[href*='/job/']")

dados = []

for job in jobs:
    try:
        titulo = job.text
        link = job.get_attribute("href")

        dados.append({
            "titulo": titulo,
            "link": link
        })
    except:
        pass

# Abrir cada projeto
for link in dados:
    driver.get(link['link'])
    time.sleep(3)

    try:
        titulo = driver.find_element(By.TAG_NAME, "h1").text
    except:
        titulo = ""

    try:
        descricao = driver.find_element(By.TAG_NAME, "body").text
    except:
        descricao = ""

    salvar_projeto(
        link['titulo'],
        link['link'],
        descricao
    )

# salvar
with open("projetos.json", "w") as f:
    json.dump(projetos, f, indent=4)

driver.quit()

