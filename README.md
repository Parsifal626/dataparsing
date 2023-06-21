Это тестовое задание для парсинга данных с сайта https://4lapy.ru/catalog/sobaki/korm-sobaki/sukhoy-korm-sobaki/.


Начало работы:

1. Установка зависимостей - pip install -r requirements.txt

2 работа со скриптом: вводим в командной строке bash: $python main3.py - результатом будем появившийся файл products1.csv.


3.Для того, чтобы добавить информацию с других страниц в файл products1.csv необходимо сделать следующее:
в файле main3.py изменяем строку:
https://4lapy.ru/catalog/sobaki/korm-sobaki/sukhoy-korm-sobaki/?section_id=166&sort=popular&page={указываем число от 1 до максимального количества страниц (в данном случае 12)}
вводим в командной строке bash: $python main3.py


P.s. работа над пагинацией страниц продолжается :)
