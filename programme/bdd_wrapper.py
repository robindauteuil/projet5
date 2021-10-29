import mysql.connector
from mysql.connector import Error
import requests


class Data_base:

    def __init__(self):

        self.connexion = mysql.connector.connect(
            host='localhost', user='robin', password=''
        )
        self.cursor = self.connexion.cursor(buffered=True)
        self.insert_name = set()

    def initialisation(self):
        """Connect and create Mysql database"""
        self.cursor.execute('create database if not exists open_food_facts;')

        with open("creation_bdd.sql", 'r') as bdd:
            file = bdd.read()
            requetes = file.split(';')
        for line in requetes:
            self.cursor.execute(line)

        self.connexion.commit()

    def insert_products(self, list_products, nb):
        self.cursor.execute(
            'use open_food_facts'
        )

        for product in list_products:
            if product['name'] not in self.insert_name:
                requete = 'insert into food_items (name, nutriscore, description, shop, brand, url, category_ID) value (%s,%s,%s,%s,%s,%s,%s);'
                value = [product['name'], product['nutriscore'], product['description'], product['magasin'],
                         product['marque'], product['url'], int(nb)]
                self.cursor.execute(requete, value)

                self.insert_name.add(product['name'])

        self.connexion.commit()


    def checking_init(self):

        requete = "select exists(select 1 from food_items);"
        self.cursor.execute(requete)
        result_cat = self.cursor.fetchall()

        if result_cat == [(1,)]:
            return True
            print('pre_loaded')

    def insert_categories(self, list_categories):

        for category in list_categories:
            requete = "insert into category(name) values(%s);"
            value = [(category)]
            self.cursor.execute(requete, value)
        self.connexion.commit()

    def select_categories(self, offset):

        self.cursor.execute('select * from category as categorie limit %s offset %s', (20, int(offset)))
        resultat = self.cursor.fetchall()

        return resultat

    def select_all_categories(self):
        self.cursor.execute('select * from category as categorie ')  # limit %s offset %s', (20, int(offset)))
        resultat = self.cursor.fetchall()

        return len(resultat)

    def select_all_products(self, id_category):
        requete = ('select * from food_items where category_id = (%s)')
        value = [id_category]
        self.cursor.execute(requete, value)
        resultat = self.cursor.fetchall()
        return len(resultat)

    def select_products(self, list_categories, category_id, offset):

        for category in list_categories:
            nb, name = list_categories.index(category) + 1, category[1]
            if nb == category_id:

                requete = 'select ID from category where name = %s '
                self.cursor.execute(requete, (name,))
                res = self.cursor.fetchall()

                nb = str(res).strip('[]')
                id = nb.strip('()')
                re_id = id.strip(',')
                int_id = int(re_id)
                requete = (
                'select name, description, nutriscore, shop, brand from food_items where category_id = (%s)  limit 20 offset %s',
                (int_id, offset))
                print('category :', name)
                self.cursor.execute(*requete)
        resultat = self.cursor.fetchall()

        return resultat, int_id

    def select_a_product(self, id_product, products):

        for tuple in products:
            nb = products.index(tuple) + 1
            name = tuple[0]

            if nb == id_product:
                requete = 'select * from food_items where name = %s '
                self.cursor.execute(requete, (name,))
                res = self.cursor.fetchall()
                self.connexion.commit()
                return name, res

    def select_nutriscore_product(self, product):

        requests = 'select nutriscore from food_items where name = %s '
        self.cursor.execute(requests, (product,))
        result = self.cursor.fetchall()
        nutriscore = result[0][0]
        return (nutriscore)

    def select_all_substituants(self, nb_category, produit, nutriscore):

        requete = ("select * from food_items where category_id = (%s) and nutriscore < %s and name != %s")
        value = (nb_category,nutriscore, produit)
        self.cursor.execute(requete, value)
        resultat = self.cursor.fetchall()
        return len(resultat)

    def select_substituants(self, nb, offset, produit,nutriscore_product):
        if nutriscore_product != 'a':
            requete = (
                "select name, description, nutriscore, shop, brand from food_items where category_id = (%s) and name != %s and nutriscore < %s limit 20 offset %s",
                (nb, produit,nutriscore_product, offset))

            self.cursor.execute(*requete)
        if nutriscore_product == 'a':
            requete = (
                "select name, description, nutriscore, shop, brand from food_items where category_id = (%s) and name != %s and nutriscore = %s limit 20 offset %s",
                (nb, produit, nutriscore_product, offset))
            self.cursor.execute(*requete)

        resultat = self.cursor.fetchall()
        return resultat

    def select_a_substituant(self, id_substituant, substituants):

        for tuple in substituants:
            nb = substituants.index(tuple) + 1
            name = tuple[0]

            if nb == id_substituant:
                requete = 'select * from food_items where name = %s '
                self.cursor.execute(requete, (name,))
                res = self.cursor.fetchall()
                return name, res

    def save_product_substituant(self, product, substituant):

        requete = 'insert into registred_food(product, substituant) values(%s, %s)'
        values = [product, substituant]
        self.cursor.execute(requete, values)
        self.connexion.commit()

    def select_registered_substituant(self, offset):

        requete = ('select product as product, substituant as substituant from registred_food limit 20 offset %s; ')
        self.cursor.execute(requete, (offset,))
        resultat = self.cursor.fetchall()
        return resultat

    def select_all_registered_substituants(self):
        requete = ('select * from registred_food ; ')
        self.cursor.execute(requete)
        resultat = self.cursor.fetchall()
        return len(resultat)
