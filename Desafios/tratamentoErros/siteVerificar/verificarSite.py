# Desafio: Crie um código em Python que teste se o site Pudim(pudim.com.br) está acessível pelo computador usado.

import requests

site01 = 'https://www.pudim.com.br'
site02 = 'https://www.carrosnaweb.com.br/'
site03 = 'https://korncars.com/'
site04 = 'https://bitcoinfora.com.br/'
site05 = 'https://developer.mozilla.org/pt-BR/'
site06 = 'https://www.youtube.com/'
site07 = 'https://github.com/'
site08 = 'https://scholar.google.com.br/'
site09 = 'https://icloud.com/'
site10 = 'https://www.facebook.com/'

def verificarSite(site):
    try:
        verificando = requests.get(site)
        statusCode = verificando.status_code
        return f'-> \033[0;35mStatus do site: ({statusCode}) {site} funcionando corretamente!\033[m'
    except:
        return f'\033[0;31mERROR!!!\033[m \n -> {site} \n -> \033[0;31mNão foi possível acessar site...\033[m \n'


print(verificarSite(site01))
print(verificarSite(site02))
print(verificarSite(site03))
print(verificarSite(site04))
print(verificarSite(site05))
print(verificarSite(site06))
print(verificarSite(site07))
print(verificarSite(site08))
print(verificarSite(site09))
print(verificarSite(site10))
