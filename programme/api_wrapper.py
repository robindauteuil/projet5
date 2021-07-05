import requests
import json
import binance
from programme.bdd_wrapper import *


class Api:

    def __init__(self):

        self.url_list = None
        self.list_code_products_from_a_category = None

    def get_categories(self):
        url_list = {}
        url_requests_category = "https://france.openfoodfacts.org/categories.json"
        all_categories = requests.get(url_requests_category).json()
        tags_categories = all_categories['tags']
        # print(tags_categories)
        # print(list(tags_categories.keys()))
        for categories in tags_categories:
            if len(url_list) < 10:
                url_list[categories['name']] = categories['url']

        self.url_list = url_list

        print(self.url_list)
        return self.url_list
    def get_products_from_a_category(self, category_name):

        list_code_products_from_a_category = []
        list_url_products = []
        url = self.url_list[category_name]
        response_category_request = requests.get(url + '.json').json()
        products_from_1_category = response_category_request['products']
        for products in products_from_1_category:
            if products.get('code') is not None:
                list_code_products_from_a_category.append(products.get('code'))
            if products.get('url') is not None:
                list_url_products.append(products.get('url'))

        self.list_code_products_from_a_category = list_code_products_from_a_category
        # print(self.list_code_products_from_a_category)
        # print(list_url_products)
        #
        #    #products = api.get_products_from_one_category("bio")
        # #def get_infos_from_product(self):

        categories_products_list = {}
        nutriscore_list = {}
        stores_list = {}
        brands_list = {}
        products_name_list = []
        for code in self.list_code_products_from_a_category:
            reponse = requests.get(
                "https://fr.openfoodfacts.org/api/v0/produit/" + code + ".json").json()
            produit = reponse['product']


            nom_produit = (produit["product_name"])
            products_name_list.append(nom_produit)

            categories_produit = (produit["categories"])
            #categories_products_list.append(categories_produit)
            categories_products_list[nom_produit] = categories_produit

            #
            try:
                nutriscore = produit['nutrition_grades']
            except:
                nutriscores = 'inconnu'
            #nutriscore_list.append(nutriscore)
            nutriscore_list[nom_produit] = nutriscore


            try:
                marque = produit['brands']
            except:
                marque = 'marque inconnu'
            #brands_list.append(marque)
            brands_list[nom_produit] = marque

            try:
                magasin_dispo = produit['stores']
            except:
                magasin_dispo = 'magasin inconnu'
            #stores_list.append(magasin_dispo)
            stores_list[nom_produit] = magasin_dispo

        return products_name_list, categories_products_list, nutriscore_list, stores_list, brands_list


# 1) finir fonction get_product_1_category => liste code et url des produits pour la catégorie en parametre

# 2)placer une catégorie en parametre
# 3)récuperer name, category, nutriscore, magasin, marque de chaque produit pour la catégorie sélectionnée depuis la requete
# 4)organisation en module
# 5)insertion données dans les tables
#)affichage les catégories, les produits
# 6)sélection d'un produit et comparaison produits pour trouver un substitut
#)enregister un substitut
# 7)L'utilisateeur peut accéder à sa  base de données

