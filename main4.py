import requests
import csv
from bs4 import BeautifulSoup

# Функция для получения данных о товарах
def parse_data():
    url = "https://4lapy.ru/catalog/sobaki/korm-sobaki/sukhoy-korm-sobaki/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='b-common-item')

    parsed_data = []

    for item in items:
        product_id = item['data-productid']
        name = item.find('span', class_='b-item-name').text.strip()
        link = item.find('a', class_='b-common-item__description-wrap')['href']
        regular_price = item.find('a', class_='js-price')['data-price']
        promo_price = item.find('a', class_='js-price')['data-packagediscount']
        brand = item.find('span', class_='span-strong').text.strip()

        data = {
            'ID товара': product_id,
            'Наименование': name,
            'Ссылка на товар': link,
            'Регулярная цена': regular_price,
            'Промо цена': promo_price if promo_price else '',
            'Бренд': brand
        }

        parsed_data.append(data)

    return parsed_data

# Функция для сохранения данных в CSV файл
def save_to_csv(data):
    keys = data[0].keys()
    filename = 'parsed_data.csv'

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Данные сохранены в файл: {filename}")

# Вызов функций для парсинга и сохранения данных
parsed_data = parse_data()
save_to_csv(parsed_data)
