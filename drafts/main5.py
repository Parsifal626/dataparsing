import requests
import csv
from bs4 import BeautifulSoup


num_of_pages = 12

url = "https://4lapy.ru/catalog/sobaki/korm-sobaki/sukhoy-korm-sobaki/"

headers = { "user-agent": 
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0 (Edition Yx 05)"
}

response = requests.get(url, headers)



# with open("projects.html", "w") as file:
#     file.write(response.text)

with open("projects.html") as file:
    src= file.read()


soup = BeautifulSoup(src, 'html.parser')

pages_count = (soup.find("a", class_ ="b-pagination__link").find_all("title"))




# items = soup.find_all('div', class_='b-common-item')

# with open('products5.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['ID', 'Наименование', 'Ссылка', 'Промо цена', 'обычная цена', 'Бренд'])

#     # def data_parse(url):
#     for item in items:
#         productid = item['data-productid']
#         name = item.find('span', class_='b-item-name').text.strip()
#         link = "https://4lapy.ru/" + item.find('a', class_='b-common-item__description-wrap')['href']
#         promo_price = item.find("span", class_="b-common-item__bottom_current_price").text.strip()
#         regular_price_element = item.find("a", class_="b-weight-container__link js-price active-link").get("data-oldprice").split("\n")
#         brand = item.find('span', class_='span-strong').text.strip()
#         writer.writerow([productid, name, link, regular_price_element, promo_price, brand])

# print("Парсинг завершен. Данные сохранены в products.csv.")    







    





# def main():
#     data_parse()



# if __name__ = "__main__":
#     main()