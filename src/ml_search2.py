import requests
from bs4 import BeautifulSoup
import pandas as pd

keyword = 'janelas-de-aluminio'
url = f"https://lista.mercadolivre.com.br/{keyword}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    # Lista para armazenar os produtos
    produtos = []

    # Selecionar os itens de produtos
    for item in soup.select("li.ui-search-layout__item"):
        # Título do produto
        titulo = item.select_one("h2.ui-search-item__title").get_text(
            strip=True) if item.select_one("h2.ui-search-item__title") else None

        # Preço do produto
        preco = item.select_one("span.andes-money-amount__fraction").get_text(
            strip=True) if item.select_one("span.price-tag-fraction") else None

        # Marca do produto
        marca = item.select_one("span.ui-search-item__group__element.ui-search-item__brand").get_text(
            strip=True) if item.select_one("span.ui-search-item__group__element.ui-search-item__brand") else None

        # Link do produto
        link = item.select_one(
            "a.ui-search-link")["href"] if item.select_one("a.ui-search-link") else None

        # Adicionar ao dicionário de produtos
        produtos.append({
            "titulo": titulo,
            "preco": preco,
            "marca": marca,
            "link": link
        })

    # Exibir os produtos
    for produto in produtos:
        print(produto)

else:
    print("Erro")
