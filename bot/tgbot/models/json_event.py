import requests
from bs4 import BeautifulSoup
import json
import datetime


def json_create():
# Отправляем GET-запрос на указанный URL
    url = "https://stzv.ru/events/" 
    plus_url = 'https://stzv.ru'
    response = requests.get(url)

# Парсим HTML-контент с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

# Находим все элементы с классом "col-md-4 col-6 element-item concert"
    event_elements = soup.find_all(class_="event-item-thumb")

# Создаем список для хранения данных о событиях
    events_data = {}

# Перебираем элементы событий
    for event in event_elements:
        image_element = event.find("img")
        link_element = event.find("a")
        date_element = event.find("p")
        cost_element = event.find("p")

            

        event_data = {
            "type": event.find("h6").text.strip(),
            "title": event.find("h5", class_="contentTitle").text.strip(),
            "cost": date_element.find_next_sibling("p").text.strip() if date_element and date_element.find_next_sibling("p") else None,
            "date": cost_element.text.strip() if cost_element and cost_element.find_next_sibling("p") else None,
            "location": event.find("div", class_="stkz-location").text.strip(),
            "image_src": plus_url + image_element["src"] if image_element else None,
            "link": plus_url + link_element["href"] if link_element else None,
        }

    
        events_data[event_data["title"]] = event_data

# Записываем данные в файл JSON
    with open("events.json", "w", encoding="utf-8") as json_file:
        json.dump(events_data, json_file, ensure_ascii=False, indent=4)

    print("Данные сохранены в events.json")


def get_events_data():
    with open("events.json", "r", encoding="utf-8") as json_file:
        events_data = json.load(json_file)
    return events_data

def get_date():
    data = get_events_data()
    date = []
    for event in data:
        date.append(data[event]["date"])

    return date

import datetime

def converter():
    date = get_date()
    res = []
    
    for i in date:
        # Извлекаем день и месяц из строки даты
        day = int(i.split()[1])  # Получаем день
        month_name = i.split()[2]  # Получаем название месяца
        
        # Преобразуем название месяца в номер месяца (если необходимо)
        month_dict = {
            'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
            'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
            'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
        }
        month = month_dict[month_name]
        
        # Создаем объект datetime
        date_obj = datetime.datetime(year=2023, month=month, day=day)
        date_obj = date_obj.strftime("%d.%m.%Y")
        if date_obj >= datetime.datetime.now().strftime("%d.%m.%Y"):
            print(date_obj)
            res.append(date_obj)

    
    return res

if __name__ == "__main__":
    json_create()
