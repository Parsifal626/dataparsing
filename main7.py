import requests
import csv

base_url = 'https://4lapy.ru/api/goods_list_cached/'
category_id = 166
count = 10
sort = 'popular'

proxy = {
    'http': 'http://your_proxy_here',
    'https': 'https://your_proxy_here'
}

user_agent = 'lapy/3.9.2 (Samsung; Android)'

headers = {
    'User-Agent': user_agent
}

with open('products2.csv', 'a+', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Наименование', 'Ссылка', 'Регулярная цена', 'Промо цена', 'Бренд'])

    for page in range(1, 10):
        params = {
            'category_id': category_id,
            'count': count,
            'page': page,
            'sort': sort
        }

# response не сработает - нужен прокси. Если хочешь без прокси тоже ок - удали proxies=proxy из строчки ниже)
        response = requests.get(url=base_url, params=params, proxies=proxy, headers=headers) 
        data = response.json()['data']["goods"]

        for product in data:
            product_id = product['id']
            name = product['title']
            link = product['webpage']
            brand = product['brand_name']
            regular_price = product['price']['old']
            promo_price = product['price']['actual']

            writer.writerow([product_id, name, link, regular_price, promo_price, brand])
    print("Завершено")
