import requests
from pathlib import Path
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# Iniciar uma sessão
with requests.Session() as s:
    # URL do site
    url = 'https://www.codechef.com'
    login_url = 'https://www.codechef.com/api/codechef/login'
    dashboard_url = 'https://www.codechef.com/api/learn/dashboard'

    proxy = {
        'http': 'http://localhost:8080',
        'https': 'http://localhost:8080',
    }

    # Fazer uma solicitação GET à página inicial para obter o CSRF token
    context = s.get(login_url, verify=False)  # proxies=proxy,

    # Procurar pelo CSRF token
    soup = BeautifulSoup(context.content, 'html.parser')
    csrf_token = soup.find_all('input')[3]['value']
    cleaned_token = csrf_token.replace('\\"', '')
    form_id = soup.find_all('input')[4]['value']
    cleaned_form_id = form_id.replace('\\"', '')

    print('oi')

    # Definir os dados de login
    payload = {
        'name': os.getenv('CC_USER'),
        'pass': os.getenv('CC_PASS'),
        'csrfToken': cleaned_token,
        'form_build_id': cleaned_form_id,
        'form_id': 'ajax_login_form'
    }

    # Fazer uma solicitação POST para o endpoint de login
    login = s.post(url=login_url, data=payload, verify=False)  # proxies=proxy,

    if login.status_code == 200:
        print("Login bem-sucedido")
        dashboard = s.get(url=dashboard_url, verify=False)  # proxies=proxy,
        if dashboard.status_code == 200:
            print(
                f'Sucesso ao receber os dados de Dashboard: Status Code - {dashboard.status_code}')
            print(dashboard.text)
        else:
            print(
                f'Falha ao receber os dados de Dashboard: Status Code - {dashboard.content}')
    else:
        print("Falha no login")
        print(login.status_code)
        print(login.text)
