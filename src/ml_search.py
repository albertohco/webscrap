import requests
from bs4 import BeautifulSoup
import pandas as pd

keyword = 'janela-aluminio'
url = f"https://lista.mercadolivre.com.br/{keyword}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    data = []

    search_result = soup.find_all("div", class_="ui-search-result")

    for result in search_result:
        link = None
        title = result.find("h2", class_="ui-search-item__title").text.strip()
        price = result.find(
            "span", class_="andes-money-amount__fraction").text.strip()
        link_tag = result.find("a", class_="ui-search-link")
        if link_tag:
            link = link_tag.get("href")

        data.append({"Title": title,
                     "Price": price,
                     "Link": link
                     })

    print(data)

else:
    print("Erro")
