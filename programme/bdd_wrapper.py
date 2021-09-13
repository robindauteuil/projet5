import mysql.connector
from mysql.connector import Error
import requests


class Data_base:
    def __init__(self):

        self.connexion = mysql.connector.connect(
            host='localhost', user='robin', password=''
        )
        self.cursor = self.connexion.cursor(buffered=True)
        self.categories_loaded = False
        self.list_category = None

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
                            ' name varchar(150) , category_ID smallint unsigned , description varchar(255),nutriscore varchar(1), shop varchar(255), brand varchar(255), url text, primary key (ID)) engine = innodb')

        self.cursor.execute(
            'create table if not exists registred_food(ID smallint unsigned not null auto_increment , name varchar(150), primary key (ID)) engine = innodb')

    def insert_products(self, list, nb):
        self.cursor.execute(
            'use open_food_facts'
        )
        products_name_list, categories_products_list, nutriscore_list, stores_list, brands_list, list_url, description_list = list

        for nom_produit in products_name_list:
            requete = "insert into food_items (name) values (%s);"
            value = [(nom_produit)]
            self.cursor.execute(requete, value)

        for keys, values in nutriscore_list.items():
            requete = "update food_items set nutriscore = (%s) where name = (%s )"
            value = [(values, keys)]
            self.cursor.executemany(requete, value)

        for keys, values in description_list.items():
            requete = "update food_items set description = (%s) where name = (%s )"
            value = [(values, keys)]
            self.cursor.executemany(requete, value)

        for keys, values in stores_list.items():
            requete = "update food_items set shop = (%s) where name = (%s )"
            value = [(values, keys)]
            self.cursor.executemany(requete, value)
        #
        for keys, values in brands_list.items():
            requete = "update food_items set brand = (%s) where name = (%s )"
            value = [(values, keys)]
            self.cursor.executemany(requete, value)

        for keys, values in list_url.items():
            requete = "update food_items set url = (%s) where name = (%s )"
            value = [(values, keys)]
            self.cursor.executemany(requete, value)

        for nom_produit in products_name_list:
            requete = 'update food_items set category_ID = (%s) where name = (%s)'
            value = [(int(nb), nom_produit)]
            self.cursor.executemany(requete, value)
        self.connexion.commit()
        #

    def checking_init(self):

        requete = "select exists(select 1 from category);"
        self.cursor.execute(requete)
        result_cat = self.cursor.fetchall()

        # result = self.cursor.fetchall()
        if result_cat == [(1,)]:
            self.categories_loaded = True
            print('pre_loaded')

    def insert_categories(self, list_categories):

        for category in list_categories:
            requete = "insert into category(name) values(%s);"
            value = [(category)]
            self.cursor.execute(requete, value)
        self.connexion.commit()
        self.categories_loaded = True

    def select_a_category(self, offset):

        # self.cursor.execute(requete)
        self.cursor.execute('select * from category as categorie limit %s offset %s', (20, int(offset)))
        resultat = self.cursor.fetchall()
        for tuple in resultat:
            print('{} . {}'.format(resultat.index(tuple) + 1, tuple[1]))

        self.list_category = resultat

    def show_all_products_from_a_cat(self, category_id, offset):

        for tuple in self.list_category:
            nb, name = self.list_category.index(tuple)+1, tuple[1]
            if nb == category_id:
                # name = name_category

                requete = 'select ID from category where name = %s '
                self.cursor.execute(requete, (name,))
                res = self.cursor.fetchall()

                nb = str(res).strip('[]')
                id = nb.strip('()')
                re_id = id.strip(',')
                int_id = int(re_id)
                requete = ('select * from food_items where category_id = (%s) limit 20 offset %s', (int_id, offset))
                print('category :', name)
                self.cursor.execute(*requete)
        resultat = self.cursor.fetchall()

        for tuple in resultat:
            print('{} . {}'.format(resultat.index(tuple) + 1, tuple[1]))
        return resultat, int_id

    def select_a_product(self, id_product, products):
        for tuple in products:
            nb = products.index(tuple)+1
            name = tuple[1]

            if nb == id_product:
                requete = 'select * from food_items where name = %s '
                self.cursor.execute(requete, (name,))
                res = self.cursor.fetchall()
                print(res)
                return nb-1

        self.connexion.commit()

    def show_substituants(self, nb, offset):

        requete = ('select * from food_items where category_id = (%s) limit 20 offset %s', (nb, offset))

        self.cursor.execute(*requete)

        resultat = self.cursor.fetchall()
        resultat.pop(nb)
        for tuple in resultat:
            print('{} . {}'.format(resultat.index(tuple) + 1, tuple[1]))



