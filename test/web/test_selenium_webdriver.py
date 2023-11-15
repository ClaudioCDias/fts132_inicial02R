# 1 Importar Bibliotecas
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

caminho_print = 'C:/Users/Claudio C. Dias/PycharmProjects/fts132_inicial/prints/' \
                + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'

#2 Classe
class Test_selenium_webdriver():



# Definição de Início - Executa Antes do teste
    def setup_method(self, method):
        # Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)  # O Selenium vai esperar até três segundos pelos elementos
        self.driver.maximize_window()  # Maximizar a janela do navegador

        # cria a pasta caminho_print apenas antes do primeiro teste
        try:
            os.mkdir(caminho_print)
        except:
            print('A pasta ja existia')

# Definição de Fim - Executa depois do teste
    def teardown_method(self, method):
        # Destruir o objeto do Selenium
        self.driver.quit()

    # Definição do Teste
    @pytest.mark.parametrize('id', [
    ('1'),
    ('2'),
    ])
    def testar_comprar_curso_PreparatorioCTFLAT(self, id):
        self.driver.get('https://www.iterasys.com.br/pt')
        time.sleep(1)
        self.driver.get_screenshot_as_file(f'{caminho_print}teste {id} - passo 1 - home.png')
        time.sleep(2)
        self.driver.find_element(By.ID, '16237702146520').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/pt/cursos/preparatorio-ctfl-at"] div').click()
        time.sleep(2)
        self.driver.get_screenshot_as_file(f'{caminho_print}teste {id} - passo 2 - pesquisa_curso.png')
        time.sleep(2)
        assert self.driver.find_element(By.CSS_SELECTOR, "h1:nth-child(1)").text == "Preparatório CTFL-AT"
        assert self.driver.find_element(By.CSS_SELECTOR,
                            ".content-purchase-info:nth-child(2) .content-price-installments-amount").text == 'R$ 24,83'
        time.sleep(2)