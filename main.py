from programme.api_wrapper import *
from programme.bdd_wrapper import *



class Controller:

    def __init__(self):
        self.Open_food_facts = Api()
        self.Bdd = Data_base()

    def loop(self):

        self.Bdd.initialisation()
        self.Open_food_facts.get_categories()
        #self.Open_food_facts.get_products_from_a_category('Plats préparés')
        #print('return', self.Open_food_facts.get_products_from_a_category('Plats préparés'))
        self.Bdd.insert_products(self.Open_food_facts.get_products_from_a_category('Snacks'))





Controll = Controller()
Controll.loop()