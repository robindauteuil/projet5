import requests
import json

from programme.bdd_wrapper import *


class Api:

    def get_categories(self):

        name_dict = {}
        id_list = []
        list_categories = []
        url_requests_category = "https://france.openfoodfacts.org/categories.json"
        all_categories = requests.get(url_requests_category).json()
        tags_categories = all_categories['tags']
        n = 1
        for categories in tags_categories:

            if len(name_dict) < 60:
                name_dict[n] = categories['name']
                id_list.append(categories['id'])
                list_categories.append(categories['name'])
                n += 1

        return name_dict, id_list, list_categories

    def get_products_from_a_category(self, category_id):

        url = "https://us.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + category_id + "&tagtype_1=nutrition_grades&tag_contains_1=contains&json=true"
        response_category_request = requests.get(url).json()

        products = response_category_request['products']


        list_dict = []
        for produit in products:
            dict = {}
            nom_produit = (produit["product_name"])
            url_produit = (produit['url'])

            try:
                marque = produit['brands']
            except KeyError:
                marque = 'marque inconnu'

            try:
                magasin_dispo = produit['stores']
            except KeyError:
                magasin_dispo = 'magasin inconnu'

            try:
                description = produit['ecoscore_data']['agribalyse']['name_fr']
            except KeyError:
                description = 'description inconnu'
            try:
                nutriscore = (produit['nutriscore_grade'])
            except KeyError:
                nutriscore = 'nutriscore inconnu'

            dict['name'] = nom_produit
            dict['url'] = url_produit
            dict['nutriscore'] = nutriscore
            dict['magasin'] = magasin_dispo
            dict['marque'] = marque
            dict['description'] = description
            list_dict.append(dict)

        return list_dict

