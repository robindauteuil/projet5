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

        key = input('\n1. for choose a product\n2. to check your registred substituants\n\n')
        if key == '1':
            self.function_choose_products = True
        if key == '2':
            self.function_check_registred_substituant = True

    def tets_show_cate(self, list_tuple_categories, offset):
        tuple_on_screen = []
        for tuple in list_tuple_categories:
            if list_tuple_categories.index(tuple)> offset:
                if len(tuple_on_screen) <20:
                    tuple_on_screen.append(tuple)
        #print(tuple_on_screen)
        for tuple in tuple_on_screen:
            print('{} . {}'.format(tuple_on_screen.index(tuple) + 1, tuple[1]))

    def show_categories(self, list_tuples_categories):

        for tuple in list_tuples_categories:
            print('{} . {}'.format(list_tuples_categories.index(tuple) + 1, tuple[1]))

    def get_category(self, offset,nb_categories):

        l = list(np.arange(20, nb_categories, 20))
        l.insert(0, 0)
        offset_indexe = l.index(offset)
        max_index_l = len(l)-1

        if offset_indexe == 0:
            key = input('\n n for next page\n')


        if offset_indexe not in [0, max_index_l]:
            key = input('\n n for next and p for precedent or q to quit\n')

        if offset_indexe == max_index_l :
            key = input('\n p for precedent\n')
        # else:
        #     key = input('n for next and p for precedent or q to quit')
        if key == "p":
            offset_indexe -= 1
            offset = l[offset_indexe]
            self.offset_category = offset

        if key == 'n':
            offset_indexe += 1

            offset = l[offset_indexe]
            self.offset_category = offset

        if key.isnumeric():
            category_nb = int(key)
            self.category_chosen = True
            return category_nb

        if key == 'q':
            self.function_choose_products = False


    def get_product(self, offset, nb_products):

        l = list(np.arange(20, nb_products, 20))
        l.insert(0, 0)
        offset_indexe = l.index(offset)
        max_index_l = len(l) - 1
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
            offset = l[offset_indexe]
            self.offset_product = int(offset)

        if key == 'n':
            offset_indexe += 1
            offset = l[offset_indexe]
            self.offset_product = int(offset)

        if key.isnumeric():
            id_product = int(key)
            self.product_chosen = True
            return id_product

    def show_products(self, list_tuples_products):

        for tuple in list_tuples_products:
            print('{} . {}'.format(list_tuples_products.index(tuple) + 1, tuple))
        #if not list_tuples_products:




    def show_product_selected(self, product):

        print(product)

    def get_a_substituant(self, offset, nb_substituant):

        l = list(np.arange(20, nb_substituant, 20))
        l.insert(0, 0)
        offset_indexe = l.index(offset)
        max_index_l = len(l) - 1

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
            offset = l[offset_indexe]
            self.offset_substituant = int(offset)

        if key == 'n':
            offset_indexe += 1
            offset = l[offset_indexe]
            self.offset_substituant = int(offset)

        if key.isnumeric():
            id_product = int(key)
            self.substituant_chosen = True
            return id_product

    def get_registred_food(self, offset, nb_registred):

        l = list(np.arange(20, nb_registred, 20))
        l.insert(0, 0)
        offset_indexe = l.index(offset)
        max_index_l = len(l) - 1

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
            offset = l[offset_indexe]
            self.offset_registred_food = int(offset)

        if key == 'n':
            offset_indexe += 1
            offset = l[offset_indexe]
            self.offset_registred_food = int(offset)

        if key == 'q':
            self.function_check_registred_substituant = False


    def show_subtituants(self, list_tuple_substituants):

        print('SUBSTITUANT :')
        for tuple in list_tuple_substituants:
            print('{} . {}'.format(list_tuple_substituants.index(tuple) + 1, tuple))

    def show_product_substituant_selected(self,product, substituant):

        print(product,'/',substituant)

    def show_registred_substituants(self, registred):

        for tuple in registred:
            print('Product : {}  /  Substituant : {}'.format(tuple[0], tuple[1]))

    def save_in_database(self, product, substituant):

        key = input('\n voulez vous enregister la paire produit substituant o pour oui, n pour non\n')
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
            # self.offset_registred_food = 0
            self.category_chosen = False
            self.product_chosen = False
            self.substituant_chosen = False
            self.choose_function()
            while self.function_choose_products:

                while not self.category_chosen:
                    list_categories_on_screen = self.bdd.select_a_category(self.offset_category)

                    self.show_categories(list_categories_on_screen)
                    #self.tets_show_cate(list_categories_on_screen, self.offset_category)
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
                self.show_registred_substituants(self.bdd.select_registred_substituant(self.offset_registred_food))
                len_registred_subtituant = self.bdd.select_all_registred_substituants()
                self.get_registred_food(self.offset_registred_food, len_registred_subtituant)


Controll = Controller()
Controll.loop()

# etat: initial
# bonjour veuillez selectionner une option
# '1. for choose a product/ 2. to check your registred substituants'
# 1 creer une relation substituant substitué

# 3quitter
#
# #etat : selection des categories avec ID et page precedent, suivante
# 1.cereale
# 2.biscotte
# enter your category ID or n for next and p for precedent
# (q to go back to the mainmenu)
#
# affichage des produits de la catgorie

# enter your product ID or n for next and p for precedent
# 1,Natural almonds
# 2,Rice Cakes
# 3 Original Gourmet Popcorn
# 4,"Lightly salted organic brown rice puffed grain cakes, lightly salted"
# 5,Jackpot sea salt popcorn
##selection du produit avec choix de page
# Affichage produit sélectionné


# Affichage des substituts de la meme categorie
# 1,Natural almonds
# 2,Rice Cakes
# 3 Lightly salted organic brown rice puffed grain cakes, lightly salted
# 4,Jackpot sea salt popcorn
# selction du substitut
# affichage du substitut sélectionné
# affichage de la paire
# possibilité d'enregistrer le produit/substitut
# "voulez vous enregister la paire produit substituant o pour oui, n pour non"
# enregistrement du substitut

# 2voir les relations deja creer
# affichage produit/subtitut
# Product : Wild caught chunk light tuna in water  /  Substituant : Solid white albacore
# Product : Wowen Wheats  /  Substituant : Red Potatoes
# Product : Freeze Dried Raspberries  /  Substituant : Granny Smith Apples
# Product : Plain icelandic style skyr strained non-fat yogurt, plain  /  Substituant : Ultra-filtered milk
# Product : Haselnusskerne gemahlen  /  Substituant : Trader joe's, raw almond butter, crunchy
# Product : Uncured black forest ham  /  Substituant : Tofu
# Product : Lentils  /  Substituant : Baked Beans
# Product : Maranatha, organic raw almond butter creamy  /  Substituant : Crunchy Peanut Butter
# Product : Food for life, ezekiel 4:9, english muffins, cinnamon raisin  /  Substituant : Food for life, ezekiel 4:9, flax sprouted grain bread
# Product : Roast beef  /  Substituant : Seasoned cooked roast beef with sea salt & black pepper


# to do affichage des produits selectionnés
# to do affichage de la paire produit/subtituant
# fonctionnalité regarder les produits enregistrés
