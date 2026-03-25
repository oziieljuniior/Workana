from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#Abrir navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Abrir site
driver.get("https://www.workana.com")

title = driver.title
print(title)



#Aguardar o carregamento da página
driver.implicitly_wait(10)


driver.quit()

