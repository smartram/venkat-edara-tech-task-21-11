import os
import json
import datetime
from ingredient import Ingredient, Dish


class Chef:
    def __init__(self):
        """
        Chef will make dishes . loads json files
        """
        self.recipes_file = os.path.join("resources", "recipes.json")
        self.ingredients_file = os.path.join("resources", "ingredients.json")
        self.dishes = []

    def load_conf(self):
        """
        parses json files and populate self.dishes
        :return:
        """
        recipes_json, ingredients_json = {}, {}
        # dict of title  of ingredient and its object
        dict_ingredients = {}

        with open(self.recipes_file) as frecipes:
            recipes_json = json.load(frecipes)
        with open(self.ingredients_file) as fingredients:
            ingredients_json = json.load(fingredients)

        for x in ingredients_json["ingredients"]:
            title = x["title"]
            # parse use by
            use_by = x["use-by"]
            fields = [int(d) for d in use_by.split("-")]
            assert len(fields) == 3
            use_by_date = datetime.datetime(year=fields[0], month=fields[1], day=fields[2])
            # parse best before now
            best_before = x["best-before"]
            fields = [int(d) for d in best_before.split("-")]
            assert len(fields) == 3
            best_before_date = datetime.datetime(year=fields[0], month=fields[1], day=fields[2])
            dict_ingredients[title] = Ingredient(title, best_before_date, use_by_date)

        for recipe in recipes_json["recipes"]:
            title = recipe["title"]
            dish = Dish(title)
            for ingre in recipe["ingredients"]:
                dish.add_ingredient(dict_ingredients[ingre])

            self.dishes.append(dish)


    def filter_dishes(self, lunch_date):
        """
        given lunch_date return dishes can be prepared. remove by use_them, filter them according to time
        :param lunch_date: datetime.datetime
        :return: [String] list of dishes
        """

        filtered = []
        for dish in self.dishes:
            if dish.can_prepare(lunch_date):
                filtered.append(dish)
        # now lets sort according to ingredients
        dishes = sorted(filtered, key=lambda dish: min([i.best_before for i in dish.list_ingredients]), reverse=True)
        return [x.name for x in dishes]

if __name__ == '__main__':
    chef = Chef()
    chef.load_conf()
    future = datetime.datetime(year=2021, month=3, day=8)
    dishes = chef.filter_dishes(future)
    print(dishes)


