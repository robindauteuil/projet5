import mysql.connector
from mysql.connector import Error
import requests


class Data_base:
    def __init__(self):

        self.connexion = mysql.connector.connect(
            host='localhost', user='robin', password=''
        )
        self.cursor = self.connexion.cursor()


    def initialisation(self):
        """Connect and create Mysql database"""



        self.cursor.execute(
            'create database if not exists open_food_facts'
        )
        self.cursor.execute(
            'use open_food_facts'
        )
        self.cursor.execute(
            'create table if not exists category('
            'ID smallint unsigned not null auto_increment primary key, name varchar(150) not null '
            ') engine = innodb;'
        )
        self.cursor.execute('create table if not exists food_items(ID smallint unsigned not null auto_increment ,'
                       ' name varchar(150) , category_ID smallint unsigned , categories_tags text , description varchar(255),nutriscore varchar(1), shop varchar(50), brand varchar(50), primary key (ID)) engine = innodb')

        self.cursor.execute(
            'create table if not exists registred_food(ID smallint unsigned not null auto_increment primary key, name varchar(150)) engine = innodb')

    def insert_products(self, list):
        self.cursor.execute(
            'use open_food_facts'
        )
        products_name_list, categories_products_list, nutriscore_list, stores_list, brands_list = list
        print(nutriscore_list)
        print(products_name_list)

        for nom_produit in products_name_list:
            requete = "insert into food_items (name) values (%s);"
            value = [(nom_produit )]
            self.cursor.execute(requete, value)

        for keys, values in nutriscore_list.items():
            requete = "update food_items set nutriscore = (%s) where name = (%s )"
            value = [(values, keys)]
            self.cursor.executemany(requete, value)

        for keys, values in categories_products_list.items():
             requete = "update food_items set categories_tags = (%s) where name = (%s )"
             value = [(values, keys)]
             self.cursor.executemany(requete, value)


        for keys, values in stores_list.items():
             requete = "update food_items set shop = (%s) where name = (%s )"
             value = [(values, keys)]
             self.cursor.executemany(requete, value)
        #
        for keys, values in brands_list.items():
            requete = "update food_items set brand = (%s) where name = (%s )"
            value = [(values , keys)]
            self.cursor.executemany(requete, value)
        #
        #         # resultat = self.cursor.fetchall()
        #         # print("resultat = ", resultat)
        self.connexion.commit()