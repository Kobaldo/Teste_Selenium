from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='C:\\Users\\Kobaldo\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://wordpress.com/log-in/pt-br?redirect_to=https%3A%2F%2Fwordpress.com%2F")
    driver.implicitly_wait(2) 

    email_login = driver.find_element(By.XPATH, '//*[@id="usernameOrEmail"]')
    email_login.send_keys("Seu email aqui")

    btn_login = driver.find_element(By.XPATH, '//*[@id="primary"]/div/main/div[3]/div/form/div[1]/div[2]/button')
    btn_login.click()

    senha_login = driver.find_element(By.XPATH, '//*[@id="password"]')
    senha_login.send_keys("Sua senha aqui")
    
    btn_login = driver.find_element(By.XPATH, '//*[@id="primary"]/div/main/div[3]/div/form/div[1]/div[2]/button')
    btn_login.click()

    driver.get("https://prozds2.wordpress.com/")
    driver.implicitly_wait(2) 

    link_pagina = driver.find_element(By.LINK_TEXT, "The City That Never Sleeps")
    link_pagina.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    comentario = driver.find_element(By.XPATH, '//*[@id="comment"]')
    comentario.send_keys("Seu nome aqui")

    driver.implicitly_wait(2) 
    btn_comentario = driver.find_element(By.XPATH, '//*[@id="comment-submit"]')
    btn_comentario.click()
    
    driver.implicitly_wait(5) 
    print("Teste Passou! Comentário postado.")
except:
    print("Teste Falhou! Não foi possível postar o comentário.")

driver.quit()