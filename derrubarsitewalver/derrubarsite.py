from selenium import webdriver
import time

# Iniciar o navegador (exemplo com Chrome)
driver = webdriver.Chrome()  # Baixe o chromedriver e coloque na PATH

# Acesse o site
driver.get("http://alb-1477147751.sa-east-1.elb.amazonaws.com/")

# Fica dando refresh infinito
try:
    while True:
        time.sleep(0.01)  # 0.5 segundos entre F5, ajuste conforme necessário
        driver.refresh()
except KeyboardInterrupt:
    driver.quit()
