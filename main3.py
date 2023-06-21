import csv
import requests
from bs4 import BeautifulSoup

# URL страницы для парсинга
url = 'https://4lapy.ru/catalog/sobaki/korm-sobaki/sukhoy-korm-sobaki/'

# Отправляем GET-запрос и получаем HTML-код страницы
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все элементы, соответствующие товарам
product_items = soup.find_all('div', class_='b-common-item--catalog-item')

# Открываем файл для записи данных
with open('products1.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Наименование', 'Ссылка', 'Регулярная цена', 'Промо цена', 'Бренд'])

    # Парсим данные для каждого товара
    for item in product_items:
        product_id = item['data-productid']
        name = item.find('span', class_='b-item-name').text.strip()
        link = "https://4lapy.ru/" + item.find('a', class_='b-common-item__description-wrap')['href']
        regular_price = item.find("a", class_="b-weight-container__link js-price active-link").get("data-oldprice").split("\n")
        promo_price = item.find('a', class_='js-price')['data-packageprice']
        brand = item.find('span', class_='span-strong').text.strip()

        # Записываем данные в CSV файл
        writer.writerow([product_id, name, link, regular_price, promo_price, brand])

print("Парсинг завершен. Данные сохранены в products.csv.")
