import mysql.connector
from mysql.connector import Error
import requests


class Data_base:
    def __init__(self):

        self.connexion = mysql.connector.connect(
            host='localhost', user='robin', password=''
        )
        self.cursor = self.connexion.cursor(buffered=True)
        self.list_category = None
        self.insert_name = []

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
                            ' name varchar(150) , category_ID smallint unsigned , description varchar(255),nutriscore varchar(1), shop varchar(255), brand varchar(255), url varchar(500) , primary key (ID  )) engine = innodb')

        self.cursor.execute(
            'create table if not exists registred_food(ID smallint unsigned not null auto_increment , product varchar(150), substtituant varchar(150), primary key (ID)) engine = innodb')

    def insert_products(self, list, nb):
        self.cursor.execute(
            'use open_food_facts'
        )
        inserted_names = set()
        for dict in list:
            if dict['name'] not in self.insert_name:
                requete = 'insert into food_items (name) value(%s);'
                value = [dict['name']]
                self.cursor.execute(requete,value)

                requete = 'update food_items set nutriscore = (%s) where name = (%s )'
                value = [dict['nutriscore'],dict['name']]
                self.cursor.execute(requete, value)

                requete = "update food_items set description = (%s) where name = (%s )"
                value = [dict['description'], dict['name']]
                self.cursor.execute(requete, value)

                requete = "update food_items set shop = (%s) where name = (%s )"
                value = [dict['magasin'],dict['name']]
                self.cursor.execute(requete, value)

                requete = "update food_items set brand = (%s) where name = (%s )"
                value = [dict['marque'],dict['name']]
                self.cursor.execute(requete, value)

                requete = "update food_items set url = (%s) where name = (%s )"
                value = [dict['url'], dict['name']]
                self.cursor.execute(requete, value)

                requete = 'update food_items set category_ID = (%s) where name = (%s)'
                value = [(int(nb), dict['name'])]
                self.cursor.executemany(requete, value)
                self.insert_name.append(dict['name'])
                #print(inserted_names)
            
        self.connexion.commit()
        #

    def checking_init(self):

        requete = "select exists(select 1 from food_items);"
        self.cursor.execute(requete)
        result_cat = self.cursor.fetchall()

        # result = self.cursor.fetchall()
        if result_cat == [(1,)]:
            return True
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
        # for tuple in resultat:
        #     print('{} . {}'.format(resultat.index(tuple) + 1, tuple[1]))

        self.list_category = resultat
        return resultat
    def select_products(self, category_id, offset):

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

        # for tuple in resultat:
        #     print('{} . {}'.format(resultat.index(tuple) + 1, tuple[1]))
        return resultat, int_id

    def select_a_product(self, id_product, products):
        for tuple in products:
            nb = products.index(tuple)+1
            name = tuple[1]

            if nb == id_product:
                requete = 'select * from food_items where name = %s '
                self.cursor.execute(requete, (name,))
                res = self.cursor.fetchall()
                #print(res)

                self.connexion.commit()
                return name,res

    def select_substituants(self, nb, offset, produit):

        requete = ("select * from food_items where category_id = (%s) and name != %s limit 20 offset %s", (nb, produit, offset))

        self.cursor.execute(*requete)

        resultat = self.cursor.fetchall()
        # print('SUBSTITUANT :')
        # for tuple in resultat:
        #     print('{} . {}'.format(resultat.index(tuple) + 1, tuple[1]))
        return resultat

    def select_a_substituant(self, id_substituant, substituants):
        for tuple in substituants:
            nb = substituants.index(tuple)+1
            name = tuple[1]

            if nb == id_substituant:
                requete = 'select * from food_items where name = %s '
                self.cursor.execute(requete, (name,))
                res = self.cursor.fetchall()
                #print(res)
                return name, res

    def save_product_substituant(self, product, substituant):
        requete = 'insert into registred_food(product, substtituant) values(%s, %s)'
        values = [product, substituant]
        self.cursor.execute(requete, values)
        self.connexion.commit()

    def select_registred_substituant(self, offset):

        requete = ('select * from registred_food limit 20 offset %s; ')
        value = offset
        self.cursor.execute(requete , (offset,))
        resultat = self.cursor.fetchall()
        return resultat