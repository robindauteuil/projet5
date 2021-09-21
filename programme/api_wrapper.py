import requests
import json

from programme.bdd_wrapper import *


class Api:

    def __init__(self):

        self.category_id = None
        self.id_dict = None
        self.list_categories = None

    def get_categories(self):
        name_dict = {}
        id_list = []
        list_categories = []
        url_requests_category = "https://france.openfoodfacts.org/categories.json"
        all_categories = requests.get(url_requests_category).json()
        tags_categories = all_categories['tags']
        # print(tags_categories)
        # print(list(tags_categories.keys()))
        n = 1
        for categories in tags_categories:

            if len(name_dict) < 60:
                name_dict[n] = categories['name']
                id_list.append(categories['id'])
                list_categories.append(categories['name'])
                n += 1

        return name_dict, id_list, list_categories

    def get_products_from_a_category(self, category_id):

        url = "https://us.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + category_id + "&tagtype_1=nutrition_grades&tag_contains_1=contains&tag_1=A&additives=without&ingredients_from_palm_oil=without&json=true"
        response_category_request = requests.get(url).json()

        produit = response_category_request['products']

        # products_name_list = []
        # categories_products_list = {}
        # nutriscore_list = {}
        # stores_list = {}
        # brands_list = {}
        # list_url = {}
        # description_list = {}
        list_dict = []
        for products in produit:
            dict = {}
            nom_produit = (products["product_name"])
            url_produit = (products['url'])
            nutriscore = products['nutrition_grades']
            try:
                marque = products['brands']
            except:
                marque = 'marque inconnu'

            try:
                magasin_dispo = products['stores']
            except:
                magasin_dispo = 'magasin inconnu'

            try:
                description = products['ecoscore_data']['agribalyse']['name_fr']
            except:
                description = 'description inconnu'


            dict['name'] = nom_produit
            dict['url'] = url_produit
            dict['nutriscore'] = nutriscore
            dict['magasin'] = magasin_dispo
            dict['marque'] = marque
            dict['description'] = description
            list_dict.append(dict)
        #
        #     products_name_list.append(nom_produit)
        #
        #     url_produit = (products['url'])
        #     list_url[nom_produit] = url_produit
        #
        #     categories_produit = (products["categories"])
        #     categories_products_list[nom_produit] = categories_produit
        #
        #     try:
        #         nutriscore = products['nutrition_grades']
        #     except:
        #         nutriscore = 'inconnu'
        #     nutriscore_list[nom_produit] = nutriscore
        #
        #     try:
        #         marque = products['brands']
        #     except:
        #         marque = 'marque inconnu'
        #     brands_list[nom_produit] = marque
        #
        #     try:
        #         magasin_dispo = products['stores']
        #     except:
        #         magasin_dispo = 'magasin inconnu'
        #     stores_list[nom_produit] = magasin_dispo
        #
        #

            # try:
            #     description = products['ecoscore_data']['agribalyse']['name_fr']
            # except:
            #     description = 'description inconnu'
            # description_list[nom_produit] = description

        #return products_name_list, categories_products_list, nutriscore_list, stores_list, brands_list, list_url, description_list
        return  list_dict
    def get_category_id(self, id_list, category_id):

        for nb, val in enumerate(id_list, start=1):
            if val == category_id:
                nb_category = nb
                # list_keys = list(id_list.keys())
                # nb_category = list_keys.index(k)

                return nb_category

# 1) finir fonction get_product_1_category => liste code et url des produits pour la catégorie en parametre

# 2)placer une catégorie en parametre
# 3)récuperer name, category, nutriscore, magasin, marque de chaque produit pour la catégorie sélectionnée depuis la requete
# 4)organisation en module
# 5)insertion données dans les tables
# )affichage les catégories, les produits
# 6)sélection d'un produit et comparaison produits pour trouver un substitut
# )enregister un substitut
# 7)L'utilisateeur peut accéder à sa  base de données
