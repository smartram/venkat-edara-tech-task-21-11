class Ingredient:
    def __init__(self, name, best_before, use_by):
        """
        represents ingredients
        :param name:
        :param best_before:
        :param use_by:
        """
        self.name = name
        self.best_before = best_before
        self.use_by = use_by

    def is_expired(self, date):
        """
        given lunch date determines ingredient can be used
        :param date:
        :return: True or False
        """
        return self.use_by < date


class Dish:
    def __init__(self, name):
        """
        represents recipe .
        :param name:
        :param list_ingredients:
        """
        self.name = name
        self.list_ingredients = []

    def add_ingredient(self, ingredient):
        """
        adds ingredient to dish.
        :param ingredient:
        :return:
        """
        if isinstance(ingredient, Ingredient):
            self.list_ingredients.append(ingredient)

    def can_prepare(self, lunch_date):
        """
        can we prepare dish given lunch_date
        :param lunch_date:
        :return: True or False
        """
        total = len(self.list_ingredients)
        count = 0
        for x in self.list_ingredients:
            if not x.is_expired(lunch_date):
                count += 1

        return count == total



