from peewee import *

import json

# підключення до бази даних
db = PostgresqlDatabase(database="******", user="postgres", password="********",
                           host="localhost",  port="5432")


# створення таблиці
# якщо в json файлі є масив чи список його треба перетворити в строку в цій моделі genres був
# список але я зробив йому тип в таблиці text і коли робив вставку то
# genres=', '.join(movie['genres']) зробив з масива строку
class Movies(Model):
    id = IntegerField(unique=True)
    title = CharField()
    year = IntegerField()
    runtime = IntegerField()
    genres = TextField()
    director = CharField()
    actors = CharField()

    class Meta:
        database = db


db.connect()
# створення таблиці
db.create_tables([Movies], safe=True)


# читання з Json
with open('movies.json', 'r') as read_file:
    data = json.load(read_file)

# вставка даних в таблицю
for movie in data['movies']:
    Movies.create(
        id=movie['id'],
        title=movie['title'],
        year=movie['year'],
        runtime=movie['runtime'],
        genres=', '.join(movie['genres']),
        director=movie['director'],
        actors=movie['actors']
    )
