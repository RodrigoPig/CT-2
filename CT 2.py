from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

link = 'https://cadastramento-demo.mercafacil.com/#/home'
cpf = '137.865.800-06'
nome = 'Fábio Vitor Freitas'
celular = '(91) 98736-6012'
email = 'fabiovitorfreitas@imail.com'
data_nascimento = '13/04/1994'
cep = '68792-970'
numero = '45'


# Acessando a pagina de cadastro CPF

nav = webdriver.Chrome()
nav.get(link)
nav.maximize_window()
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/section/div/div[2]/button').click()
sleep(3)
nav.find_element(By.ID,'input-19').send_keys(cpf)
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div[2]/div/div/div[2]/button').click()
sleep(3)

# validando os campos de cadastro

nav.find_element(By.ID,'input-42').send_keys(Keys.TAB)
sleep(3)
nav.find_element(By.ID,'input-42').send_keys(nome)
sleep(2)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div/div[2]/div/div/div/div[3]/div/div/div[1]/div/div[2]/div/div').click()
nav.find_element(By.ID,'input-46').send_keys(Keys.TAB)
sleep(3)
nav.find_element(By.ID,'input-46').send_keys(celular)
sleep(3)
nav.find_element(By.ID,'input-50').send_keys(email)
sleep(3)
nav.find_element(By.ID,'input-54').send_keys(Keys.TAB)
sleep(3)
nav.find_element(By.ID,'input-54').send_keys(data_nascimento)
sleep(3)
nav.find_element(By.ID,'input-81').send_keys(cep)
sleep(3)
nav.find_element(By.ID,'input-108').send_keys(Keys.DOWN)
sleep(2)
nav.find_element(By.ID,'input-108').send_keys(numero)
sleep(2)
nav.find_element(By.ID,'input-108').send_keys(Keys.TAB)
sleep(3)

# marcando os termos de adesão

nav.find_element(By.XPATH,'/html/body/div/div[2]/div/main/div/div/div/div[2]/div/div/div/div[9]/div[1]').click()
sleep(3)
nav.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div/div/div[2]/button[1]').click()
sleep(3)
nav.find_element(By.ID,'input-72').send_keys(Keys.PAGE_DOWN)
sleep(3)
nav.close()