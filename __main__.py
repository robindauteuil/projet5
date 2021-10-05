from programme.api_wrapper import *
from programme.bdd_wrapper import *
import numpy as np


class Controller:

    def __init__(self):
        self.open_food_facts = Api()
        self.bdd = Data_base()
        self.category_chosen = False
        self.product_chosen = False
        self.substituant_chosen = False
        self.function_choose_products = False
        self.function_check_registred_substituant = False
        self.offset_category = 0
        self.offset_product = 0
        self.offset_substituant = 0
        self.offset_registred_food = 0

    def choose_function(self):

        key = input('\n1. to choose a product\n2. to check your registred substituants\n\n')
        if key == '1':
            self.function_choose_products = True
        if key == '2':
            self.function_check_registred_substituant = True


    def show_categories(self, list_tuples_categories):

        for category in list_tuples_categories:
            print('{} . {}'.format(list_tuples_categories.index(category) + 1, category[1]))

    def get_category(self, offset, nb_categories):

        list_offset = list(np.arange(20, nb_categories, 20))
        list_offset.insert(0, 0)
        offset_indexe = list_offset.index(offset)
        max_index_l = len(list_offset) - 1

        if offset_indexe == 0:
            key = input('\n n for next page\n')

        if offset_indexe not in [0, max_index_l]:
            key = input('\n n for next and p for precedent or q to quit\n')

        if offset_indexe == max_index_l :
            key = input('\n p for precedent\n')

        if key == "p":
            offset_indexe -= 1
            offset = list_offset[offset_indexe]
            self.offset_category = offset

        if key == 'n':
            offset_indexe += 1

            offset = list_offset[offset_indexe]
            self.offset_category = offset

        if key.isnumeric():
            category_nb = int(key)
            self.category_chosen = True
            return category_nb

        if key == 'q':
            self.function_choose_products = False
            return False


    def get_product(self, offset, nb_products):

        list_offset = list(np.arange(20, nb_products, 20))
        list_offset.insert(0, 0)
        offset_indexe = list_offset.index(offset)
        max_index_l = len(list_offset) - 1
        if max_index_l != 0:
            if offset_indexe == 0:
                key = input('\n n for next page\n')
            if offset_indexe == max_index_l:
                key = input('\n p for precedent or q to quit\n')
            if offset_indexe not in [0, max_index_l]:
                key = input('\n n for next and p for precedent or q to quit\n')
        if max_index_l == 0:
            key = input('\n select the product with the number\n')
        if key == "p":
            offset_indexe -= 1
            offset = list_offset[offset_indexe]
            self.offset_product = int(offset)

        if key == 'n':
            offset_indexe += 1
            offset = list_offset[offset_indexe]
            self.offset_product = int(offset)

        if key.isnumeric():
            id_product = int(key)
            self.product_chosen = True
            return id_product

    def show_products(self, list_tuples_products):

        for product in list_tuples_products:
            name, description, nutriscore, shop, brand = product
            print('{} . name : {} / description : {} / nutriscore : {} / shop : {} / brand : {}'.format(list_tuples_products.index(product) + 1, name, description, nutriscore, shop, brand))





    def show_product_selected(self, product):

        print(product)

    def get_a_substituant(self, offset, nb_substituant):

        list_offset = list(np.arange(20, nb_substituant, 20))
        list_offset.insert(0, 0)
        offset_indexe = list_offset.index(offset)
        max_index_l = len(list_offset) - 1

        if max_index_l != 0:
            if offset_indexe == 0:
                key = input('\n n for next page\n')
            if offset_indexe == max_index_l:
                key = input('\n p for precedent or q to quit\n')
            if offset_indexe not in [0, max_index_l]:
                key = input('\n n for next and p for precedent or q to quit\n')
        if max_index_l == 0:
            key = input('\n select the product with the number')

        if key == "p":
            offset_indexe -= 1
            offset = list_offset[offset_indexe]
            self.offset_substituant = int(offset)

        if key == 'n':
            offset_indexe += 1
            offset = list_offset[offset_indexe]
            self.offset_substituant = int(offset)

        if key.isnumeric():
            id_product = int(key)
            self.substituant_chosen = True
            return id_product

    def get_registered_food(self, offset, nb_registred):

        list_offset = list(np.arange(20, nb_registred, 20))
        list_offset.insert(0, 0)
        offset_indexe = list_offset.index(offset)
        max_index_l = len(list_offset) - 1

        if max_index_l != 0:
            if offset_indexe == 0:
                key = input('\n n for next page\n')
            if offset_indexe == max_index_l:
                key = input('\n p for precedent or q to quit\n')
            if offset_indexe not in [0, max_index_l]:
                key = input('\n n for next and p for precedent or q to quit\n')
        if max_index_l == 0:
            key = input('\n q to quite\n')
        if key == "p":
            offset_indexe -= 1
            offset = list_offset[offset_indexe]
            self.offset_registred_food = int(offset)

        if key == 'n':
            offset_indexe += 1
            offset = list_offset[offset_indexe]
            self.offset_registred_food = int(offset)

        if key == 'q':
            self.function_check_registred_substituant = False


    def show_subtituants(self, list_tuple_substituants):

        print('Substitutes :')
        for substituant in list_tuple_substituants:
            name, description, nutriscore, shop, brand = substituant
            print('{} . name : {} / description : {} / nutriscore : {} / shop : {} / brand : {}'.format(
                list_tuple_substituants.index(substituant) + 1, name, description, nutriscore, shop, brand))


    def show_product_substituant_selected(self,product, substituant):

        print('product:',product,'/','substitute:',substituant)

    def show_registered_substituants(self, registred):

        for tuple in registred:
            print('\nProduct : {}  /  substitute : {}'.format(tuple[0], tuple[1]))

    def save_in_database(self, product, substituant):

        key = input('\n do you want to register the pair product/substitute o for yes, n for no\n')
        if key == 'o':
            self.bdd.save_product_substituant(product, substituant)
        if key == 'n':
            pass

        self.function_choose_products = False
        self.category_chosen = False
        self.product_chosen = False
        self.substituant_chosen = False




    def loop(self):

        self.bdd.initialisation()

        if not self.bdd.checking_init():
            name_dict, id_list, list_categories = self.open_food_facts.get_categories()
            self.bdd.insert_categories(list_categories)
            for nb, id in enumerate(id_list, start=1):
                self.bdd.insert_products(self.open_food_facts.get_products_from_a_category(id), nb)

        while True:
            self.offset_category = 0
            self.offset_product = 0
            self.offset_substituant = 0
            self.offset_registred_food = 0
            self.category_chosen = False
            self.product_chosen = False
            self.substituant_chosen = False
            self.choose_function()
            while self.function_choose_products is True:

                while not self.category_chosen:
                    list_categories_on_screen = self.bdd.select_categories(self.offset_category)
                    self.show_categories(list_categories_on_screen)
                    len_categories = self.bdd.select_all_categories()
                    category_id = self.get_category(self.offset_category, len_categories)

                while not self.product_chosen:
                    product_on_screen, id_category = self.bdd.select_products(list_categories_on_screen, category_id,self.offset_product)
                    len_products = self.bdd.select_all_products(id_category)
                    if len_products < 2:
                        print('No product in this category')
                        break
                    self.show_products(product_on_screen)

                    key_product = self.get_product(self.offset_product, len_products)
                try:
                    name_product, product_selected = self.bdd.select_a_product(key_product, product_on_screen)
                    self.show_product_selected(product_selected)
                except UnboundLocalError:
                    break
                while not self.substituant_chosen:
                    substituant_on_screen = self.bdd.select_substituants(id_category, self.offset_substituant,
                                                                         name_product)
                    self.show_subtituants(substituant_on_screen)
                    len_substituant = self.bdd.select_all_substituants(id_category, name_product)
                    id_substituant = self.get_a_substituant(self.offset_substituant, len_substituant)
                name_substituant_selected, substituant_selected = self.bdd.select_a_substituant(id_substituant,
                                                                                                substituant_on_screen)
                self.show_product_substituant_selected(product_selected,substituant_selected)
                self.save_in_database(name_product, name_substituant_selected)

            while self.function_check_registred_substituant is True:
                self.show_registered_substituants(self.bdd.select_registered_substituant(self.offset_registred_food))
                len_registred_subtituant = self.bdd.select_all_registered_substituants()
                self.get_registered_food(self.offset_registred_food, len_registred_subtituant)


Controll = Controller()
Controll.loop()

