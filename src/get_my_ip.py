import requests

# proxy = {
#    'http': 'http://localhost:8080',
#    'https': 'http://localhost:8080',
# }

proxy = {
    'http': 'http://131.196.42.95:667',
    'https': 'http://131.196.42.95:667',
}

url = "http://lumtest.com/myip.json"
url2 = "https://www.globo.com"

response = requests.get(url, proxies=proxy)

if response.status_code == 200:
    print(response.json())
else:
    print("Erro")
