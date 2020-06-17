import requests
from config import URL_BASE, CHAVE_API

nome_cidade = input("Insira o nome da cidade para pesquisar o clima: ")

# q={city name}&appid={your api key}
url_completa = f"{URL_BASE}q={nome_cidade}&appid={CHAVE_API}"
# print(url_completa)

dados_recebidos = requests.get(url_completa).json()
# print(dados_recebidos)

if dados_recebidos['cod'] != '404':
    # Dados da chave 'main' = principal
    principal = dados_recebidos['main']
    # print(principal)
    temperatura_corrente = principal['temp']
    pressao_corrente = principal['pressure']
    humidade_corrente = principal['humidity']

    # Dados da chave 'weather'= Clima
    clima = dados_recebidos['weather']
    # print(clima)
    descricao_clima = clima[0]['description']
    # print(descricao_clima)

    # Mostrar os seguintes valores
    print(f"\nTemperatura = {round(temperatura_corrente - 273.15, 1)}C°.")
    print(f"Pressão Atmosférica = {pressao_corrente} hPa.")
    print(f"Humidade Corrente = {humidade_corrente}%.")
    print(f"Descrição = {descricao_clima}.")
else:
    print("Cidade não encontrada! Tente novamente.")
