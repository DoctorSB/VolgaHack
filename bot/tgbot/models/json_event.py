import requests
from bs4 import BeautifulSoup
import json

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
        "date": date_element.find_next_sibling("p").text.strip() if date_element and date_element.find_next_sibling("p") else None,
        "cost": cost_element.text.strip() if cost_element and cost_element.find_next_sibling("p") else None,
        "location": event.find("div", class_="stkz-location").text.strip(),
        "image_src": plus_url + image_element["src"] if image_element else None,
        "link": plus_url + link_element["href"] if link_element else None,
    }
    
    events_data[event_data["title"]] = event_data

# Записываем данные в файл JSON
with open("events.json", "w", encoding="utf-8") as json_file:
    json.dump(events_data, json_file, ensure_ascii=False, indent=4)

print("Данные сохранены в events.json")
