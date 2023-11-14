# 1 Importar Bibliotecas
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

caminho_print = 'C:/Users/Claudio C. Dias/PycharmProjects/fts132_inicial/Prints/' \
                + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'

#2 Classe
class Test_selenium_webdriver():
    primeira_vez = 'S'  # Controla se é a primeira execução: S ou outra: N

    def before_all(self):
        # Criar a pasta com data e hora para guardar os prints
        print('Passou pelo Before All')
        os.mkdir(caminho_print)

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
      caminho_print = 'C:/Users\Claudio C. Dias\PycharmProjects/fts132_inicial\prints/'
      self.driver.get('https://www.iterasys.com.br/pt')
      self.driver.get_screenshot_as_file(f'{caminho_print}home.png')
      self.driver.find_element(By.ID, '16237702146520').click()
      self.driver.find_element(By.CSS_SELECTOR, 'a[href="/pt/cursos/preparatorio-ctfl-at"] div').click()
      time.sleep(2)
      self.driver.get_screenshot_as_file(f'{caminho_print}home01.png')
      assert self.driver.find_element(By.CSS_SELECTOR, "h1:nth-child(1)").text == "Preparatório CTFL-AT"
      assert self.driver.find_element(By.CSS_SELECTOR,
                            ".content-purchase-info:nth-child(2) .content-price-installments-amount").text == 'R$ 24,83'
