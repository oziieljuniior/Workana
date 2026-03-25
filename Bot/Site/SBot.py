from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configuração do navegador
options = Options()
options.add_argument("--start-maximized")

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

# Mostrar resultados
for d in dados:
    print(d)

driver.quit()
