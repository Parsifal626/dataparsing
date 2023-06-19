import csv
import requests
from bs4 import BeautifulSoup

# url = 'https://4lapy.ru/catalog/sobaki/korm-sobaki/sukhoy-korm-sobaki/'

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
# }


# # Отправляем GET-запрос на сайт и получаем HTML-код страницы
# req = requests.get(url)
# src = req.text

with open('index.html', encoding="utf-8") as file:
    src = file.read()


soup = BeautifulSoup(src, 'lxml')

# csv_file = open("dog_food.csv", "w", newline="", encoding="utf-8")
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["ID товара", "Наименование", "Ссылка", "Регулярная цена", "Промо цена", "Бренд"])


# # # Ищем все элементы товаров на странице
products = soup.find_all(class_='b-common-item--catalog-item')

for product in products:
    
    productid = product["data-productid"]
    # name = soup.find("span", class_="b-item-name js-item-name").text.strip()
    # href = "https://4lapy.ru"+ product.find("a", class_="b-common-item__description-wrap js-item-link")["href"]
    # brand = soup.find("span", class_= "span-strong").text.strip()
    # regular_price = soup.find("span", class_= "b-common-item__prev-price js-sale-origin").text.strip() + " ₽"
    # promo_price = product.find("div", class_="js-price-block").text.strip()
    # # product_id = product.find("div", class_= "b-common-item__image-link js-item-link").get('id')
    

    print(f"{productid}")


# # Создаем список для хранения данных
# data = []

# # Проходимся по каждому элементу товара и извлекаем необходимые данные
# for item in product_items:
#     product_id = item.find('div', {"class": 'b-common-item__image-link js-item-link', "data-productid": "155222" }).text.strip()
#     name = item.find('span', class_='b-item-name js-item-name').text.strip()
#     link = item.find('a', class_='b-common-item__description-wrap')['href']
#     regular_price = item.find('a', class_='js-price')['data-price']
#     promo_price = item.find('a', class_='js-price')['data-packageprice']
#     brand = item.find(class_='span-strong').text.strip()


#     # Добавляем данные товара в список
#     data.append([product_id, name, link, regular_price, promo_price, brand])

# # Сохраняем данные в CSV-файл
# with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['ID', 'Наименование', 'Ссылка', 'Регулярная цена', 'Промо цена', 'Бренд'])
#     writer.writerows(data)



# import requests
# from bs4 import BeautifulSoup
# import csv

# url = "https://4lapy.ru/catalog/sobaki/korm-sobaki/sukhoy-korm-sobaki/"

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# csv_file = open("dog_food.csv", "w", newline="", encoding="utf-8")
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["ID товара", "Наименование", "Ссылка", "Регулярная цена", "Промо цена", "Бренд"])

# products = soup.find_all("a", class_="b-common-item__image-link js-item-link")
# for product in products:
#     # product_id = product.get("href").split("=")[-1]
#     # name = product.img.get("alt")
#     # link = "https://4lapy.ru" + product.get("href")
#     # regular_price = product.find("div", class_="price-block__regular").text.strip()
#     # promo_price = product.find("div", class_="price-block__special").text.strip()
#     # brand = product.img.get("title")
#     product_id = product.get('a', class_= '')

#     csv_writer.writerow([product_id, name, link, regular_price, promo_price, brand])

# csv_file.close()

# print("Данные успешно сохранены в файл dog_food.csv.")
