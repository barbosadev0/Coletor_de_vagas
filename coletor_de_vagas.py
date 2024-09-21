from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

job = input('Pesquise por uma vaga: ')

browser = webdriver.Firefox()
browser.get('https://www.vagas.com.br/')

search = browser.find_element(By.ID,'nova-home-search')
search.send_keys(job)

btn_search = browser.find_element(By.ID,'header__search-button')
btn_search.click()

result = browser.find_element(By.TAG_NAME,'h1')

print(result.text)

vagas = browser.find_elements(By.CLASS_NAME,'link-detalhes-vaga')

for vaga in vagas:
  print(f'-{vaga.text}-')