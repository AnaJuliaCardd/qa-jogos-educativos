from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_sucesso():
    driver = webdriver.Chrome()
    driver.get("https://app-jogos-educativos.com")
    driver.find_element(By.ID, "email").send_keys("teste@email.com")
    driver.find_element(By.ID, "senha").send_keys("senha123")
    driver.find_element(By.ID, "entrar").click()
    assert "Bem-vindo" in driver.page_source
    driver.quit()