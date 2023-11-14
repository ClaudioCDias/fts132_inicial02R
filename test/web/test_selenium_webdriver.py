# 1 Importar Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


# 2 Classe
class Test_selenium_webdriver():
# Definição de Início - Executa Antes do teste
 def setup_method(self, method):
    # Declarar o objeto do Selenium e instanciar como o navegador desejado
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(30)  # O Selenium vai esperar até três segundos pelos elementos
    self.driver.maximize_window()  # Maximizar a janela do navegador


# Definição de Fim - Executa depois do teste
 def teardown_method(self, method):
    # Destruir o objeto do Selenium
    self.driver.quit()


# Definição do Teste
 def testar_comprar_curso_PreparatorioCTFLAT(self):
      self.driver.get('https://www.iterasys.com.br/pt')
      self.driver.find_element(By.ID, '16237702146520').click()
      self.driver.find_element(By.CSS_SELECTOR, 'a[href="/pt/cursos/preparatorio-ctfl-at"] div').click()
      assert self.driver.find_element(By.CSS_SELECTOR, "h1:nth-child(1)").text == "Preparatório CTFL-AT"
      assert self.driver.find_element(By.CSS_SELECTOR,
                            ".content-purchase-info:nth-child(2) .content-price-installments-amount").text == 'R$ 24,83'
