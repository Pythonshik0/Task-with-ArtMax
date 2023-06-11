from bs4 import BeautifulSoup
import requests
import lxml
import json
from loguru import logger
import logging
import sqlite3

logging.basicConfig(level=logging.DEBUG)

#-----------------------------------------------------------------------------------------------------------------------1111
url = 'https://2gis.ru/ufa/search/%D0%92%D0%BA%D1%83%D1%81%D0%BD%D0%BE%20%E2%80%94%20%D0%B8%20%D1%82%D0%BE%D1%87%D0%BA%D0%B0%2C%20%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%BF%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%B5/firm/70000001006794970/55.992071%2C54.746479/tab/reviews'

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}

req = requests.get(url, headers=headers)
src = req.text

with open('index.html', 'w', encoding="utf-8") as file:
    file.write(src)

with open('index.html', encoding="utf-8") as file:
    src = file.read()


soup = BeautifulSoup(src, 'lxml')
all_products_hrefs = soup.find_all(class_='_1i94jn5')

all_categories_dict = {}
for item in all_products_hrefs:
    item_text = 'Первый филиал. Отзыв сайта "Вкусно и Точка!"   ' + item.text
    item_id = item.id
    all_categories_dict[item_text] = item_id
    logger = logging.getLogger('Ошибки нет!')
    logger.debug(f'{item_text} {item_id}')


#Сохраняю с json
with open('all_categories_dict_1', 'w', encoding="utf-8") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    #count = cursor.executemany("INSERT INTO Parser (item_text) VALUES(?,?)", zip(all_categories_dict))
    count = cursor.executemany("INSERT INTO Parser_2 (item_text) VALUES (?)", zip(all_categories_dict))
    sqlite_connection.commit()
    print("Запись успешно вставлена в таблицу")

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)

#-----------------------------------------------------------------------------------------------------------------------2222
url = 'https://2gis.ru/ufa/search/%D0%92%D0%BA%D1%83%D1%81%D0%BD%D0%BE%20%E2%80%94%20%D0%B8%20%D1%82%D0%BE%D1%87%D0%BA%D0%B0%2C%20%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%BF%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%B5/firm/2393065583018885/55.945985%2C54.724021/tab/reviews?m=55.958761%2C54.734741%2F11'
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}

req = requests.get(url, headers=headers)
src = req.text


with open('index.html', 'w', encoding="utf-8") as file:
    file.write(src)

with open('index.html', encoding="utf-8") as file:
    src = file.read()


soup = BeautifulSoup(src, 'lxml')
all_products_hrefs = soup.find_all(class_='_1i94jn5')

all_categories_dict = {}
for item in all_products_hrefs:
    item_text = 'Второй филиал. Отзыв сайта "Вкусно и Точка!"   ' + item.text
    item_id = item.id
    all_categories_dict[item_text] = item_id
    logger = logging.getLogger('Ошибки нет!')
    logger.debug(f'{item_text} {item_id}')



#Сохраняю с json
with open('all_categories_dict_2', 'w', encoding="utf-8") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    #count = cursor.executemany("INSERT INTO Parser (item_text) VALUES(?,?)", zip(all_categories_dict))
    count = cursor.executemany("INSERT INTO Parser_2 (item_text) VALUES (?)", zip(all_categories_dict))
    sqlite_connection.commit()
    print("Запись успешно вставлена в таблицу")

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)


# -----------------------------------------------------------------------------------------------------------------------3333

url = 'https://2gis.ru/ufa/search/%D0%92%D0%BA%D1%83%D1%81%D0%BD%D0%BE%20%E2%80%94%20%D0%B8%20%D1%82%D0%BE%D1%87%D0%BA%D0%B0%2C%20%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%BF%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%B5/firm/2393066583092767/55.995445%2C54.697511/tab/reviews?m=55.958761%2C54.734741%2F11'

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}

req = requests.get(url, headers=headers)
src = req.text


with open('index.html', 'w', encoding="utf-8") as file:
    file.write(src)

with open('index.html', encoding="utf-8") as file:
    src = file.read()


soup = BeautifulSoup(src, 'lxml')
all_products_hrefs = soup.find_all(class_='_1i94jn5')

all_categories_dict = {}
for item in all_products_hrefs:
    item_text = 'Третий филиал. Отзыв сайта "Вкусно и Точка!"   ' + item.text
    item_id = item.id

    logger = logging.getLogger('Ошибки нет!')
    logger.debug(f'{item_text} {item_id}')
    all_categories_dict[item_text] = item_id

#Сохраняю с json
with open('all_categories_dict_3', 'w', encoding="utf-8") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    #count = cursor.executemany("INSERT INTO Parser (item_text) VALUES(?,?)", zip(all_categories_dict))
    count = cursor.executemany("INSERT INTO Parser_2 (item_text) VALUES (?)", zip(all_categories_dict))
    sqlite_connection.commit()
    print("Запись успешно вставлена в таблицу")

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)

