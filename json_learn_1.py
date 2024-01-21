'''
Пример сериализации JSON Python
'''
import json

data ={
    'president': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
    }
}

# Используя контекстный менеджер Python, вы можете создать файл под названием data_file.json и
# открыть его в режиме write (файлы JSON имеют расширение .json).

with open('data_file.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)

# так же можно присвоить данные json в переменную используем dampS,  но это не создает и не
# добавляет данные в файл в папку проекта

json_string = json.dumps(data, indent=4)

print(json_string) # {"president": {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}}


# indent=4 , json.dumps(data, indent=4) делает вывод красивее
# {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }

output = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], sort_keys=True, indent=4)
print(output)

'''
Десериализация JSON
'''
# удалось поймать экземпляр дикого JSON! Теперь нам нужно предать ему форму. В модуле json вы
# найдете load() и loads() для превращения кодированных данных JSON в объекты Python.

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)
print(encoded_hand)
print()
print(decoded_hand)

with open('data_file.json', 'r') as read_file:
    data = json.load(read_file)

# Если вы внесли данные JSON из другой программы, или полученную каким-либо другим способом
# строку JSON форматированных данных в Python, вы можете легко десериализировать это при помощи
# loads(), который естественно загружается из строки:
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
# Ву а ля! Вам удалось укротить дикого JSON, теперь он под вашим контролем.

print(data) # {'researcher': {'name': 'Ford Prefect', 'species': 'Betelgeusian',
# 'relatives': [{'name': 'Zaphod Beeblebrox', 'species': 'Betelgeusian'}]}}

'''
Пример работы с JSON Python
'''

# Для тестового API, мы воспользуемся JSONPlaceholder, отличный источник фейковых данных JSON для
# практических целей.
#
# Для начала, создайте файл под названием scratch.py, или как вам удобно. Здесь я не могу вас
# контролировать.
#
# Вам нужно выполнить запрос API в сервис JSONPlaceholder, так что просто используйте пакет
# requests, чтобы он сделал за вас всю грязную работу. Добавьте следующие импорты вверху файла:

import json
import requests

#Идем дальше и создаем запрос в API JSONPlaceholder для конечной точки GET /todos. Если вы слабо
# знакомы с запросами, есть очень удобный метод json(), который выполнит за вас всю работу,
# но вы можете попрактиковаться в использовании модуля json для десериализации атрибута текста
# объекта response. Это должно выглядеть следующим образом

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)
print(todos[:10])
