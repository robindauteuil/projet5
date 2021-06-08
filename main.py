import mysql.connector
from mysql.connector import Error
import requests
import json


def connect():
    """Connect to Mysql database"""


connexion = mysql.connector.connect(
    host='localhost', user='robin', password=''
)

cursor = connexion.cursor()

cursor.execute(
    'create database if not exists open_food_facts'
)
cursor.execute(
    'use open_food_facts'
)
cursor.execute(
    'create table if not exists category('
    'ID smallint unsigned not null auto_increment primary key, name varchar(150) not null '
    ') engine = innodb;'
)
cursor.execute('create table if not exists food_items(ID smallint unsigned not null auto_increment primary key,'
               ' name varchar(150) not null, category varchar(150) not null, substitute_food varchar (255), description varchar(255), shop varchar(50)) engine = innodb')

cursor.execute(
    'create table if not exists registred_food(ID smallint unsigned not null auto_increment primary key, name varchar(150)) engine = innodb')
cursor.execute('show tables')

for x in cursor:
    print(x)





url = "https://us.openfoodfacts.org/api/v0/product/5000112519945"

reponse = requests.get(url)

print(reponse)

print(reponse.json())