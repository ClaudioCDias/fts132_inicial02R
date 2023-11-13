import pytest

def print_hi(name):
    print(f'Olá, {name}')

# Cozinheiro - Definições
def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

# Calcular e testar a área de um quadrado
# Area = Lado **2
def calcular_area_do_quadrado(area):
    return area ** 2

# Calcular e testar a área de um retândulo
# Área = Lado1 * Lado2
def calcular_area_do_retangulo(lado1, lado2):
    return lado1 * lado2

# Calcular e testar a área de um triângulo
# Área = Lado1 * Lado2 / 2
def calcular_area_do_triangulo(lado1, lado2):
    return lado1 * lado2 / 2

# Calcular e testar a área de um círculo
# Área = Pi * raio **2
def calcular_area_do_circulo(raio):
    try:
        return 3.14 * raio ** 2
    except TypeError:
        return 'Falha no Calculo - Raio não é um número'

def calcular_volume_do_paralelograma(largura, comprimento, altura):
    return largura * comprimento * altura


if __name__ == '__main__':

    print_hi('Claudio')

    # Garçon - Requisições / Chamadas
    resultado = somar_dois_numeros(5,7)
    print(f'A soma é {resultado}') # <-- Prato

    resultado = subtrair_dois_numeros(7,5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(3,5)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(8,4)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2,3)
    print(f'A exponenciação é {resultado}')

    resultado = calcular_area_do_quadrado(8)
    print(f'A área do quadrado é {resultado}')

    resultado = calcular_area_do_retangulo(6,9)
    print(f'A área do retangulo é {resultado}')

    resultado = calcular_area_do_triangulo(10,7)
    print(f'A área do triângulo é {resultado}')

    resultado = calcular_area_do_circulo(5)
    print(f'A área do círculo é {resultado}')

    resultado = calcular_volume_do_paralelograma(5,10,2)
    print(f'O volume do paralelograma é {resultado}')

    # Degustador / Teste
'''
def testar_somar_dois_numeros():
    # 1ª Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / InPut
    num1 = 8
    num2 = 9
    # Saída / OutPut
    resultado_esperado = 17

    # 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado
'''