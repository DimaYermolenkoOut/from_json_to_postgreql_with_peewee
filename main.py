import json
from random import randint, choice

import openpyxl


# створили функцію для записування JSON
def write_json(data, filename):
    with open(filename, 'w') as write_file:
        json.dump(data, write_file, indent=4)

# рандомний класс для генерації
class Person:
    def __init__(self):
        self.name = choice(['John', 'Jane', 'Jack', 'Jill', 'Jim'])
        self.surname = choice(['Smith', 'Johnson', 'Brown', 'Garcia', 'Miller'])
        self.age = randint(18, 65)

# словник і генерація 100 persons
data = {
    'persons': []
}
# якщо без __dict__ то вийдуть тільки ссилки на пам'ять
for i in range(100):
    data['persons'].append(Person().__dict__)


# записали в json
write_json(data, 'data_file3.json')

def read_json(filename):
    with open(filename, 'r') as read_file:
        data = json.load(read_file)
        return data

# призначаємо дані з Json файлу в змінну для використання в проєкті
json_data = read_json('movies.json')
# print(type(json_data))
# print("read JSON data: ", json_data['movies'][0]['genres'])

# перевіряємо дані
for movie in json_data['movies']:
    id = movie['id']
    title = movie['title']
    year = movie['year']
    runtime = movie['runtime']
    genres = movie['genres']
    director = movie['director']
    actors = movie['actors']

    print(id, title, year, runtime, genres, director, actors)
#Створюємо нову книгу
book = openpyxl.Workbook()
# створюємо нову лист
sheet = book.active
# назви колонок
sheet['A1'] = 'ID'
sheet['B1'] = 'TITLE'
sheet['C1'] = 'YEAR'
sheet['D1'] = 'RUNTIME'
sheet['E1'] = 'GENRES'
sheet['F1'] = 'DIRECTOR'
sheet['G1'] = 'ACTORS'

# записуємо дані в колонки
row = 2
for movie in json_data['movies']:
    sheet[f'A{row}'] = movie['id']
    sheet[f'B{row}'] = movie['title']
    sheet[f'C{row}'] = movie['year']
    sheet[f'D{row}'] = movie['runtime']
    sheet[f'E{row}'] = ', '.join(movie['genres'])
    sheet[f'F{row}'] = movie['director']
    sheet[f'G{row}'] = movie['actors']
    row += 1
# зберігаємо файл
book.save('movies.xlsx')
# закриваємо
book.close()