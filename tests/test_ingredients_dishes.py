import unittest
import datetime
import time
from ingredient import Ingredient, Dish


class MyTestCase(unittest.TestCase):
    def test_ingredient_expired(self):
        now = datetime.datetime.now()
        ingredient = Ingredient('dummy', best_before=now, use_by=now)
        now = now + datetime.timedelta(seconds=20)
        is_expired = ingredient.is_expired(now)
        self.assertTrue(is_expired)

    def test_ingredient_not_expired(self):
        now = datetime.datetime.now()
        future = now + datetime.timedelta(days=1)
        ingredient = Ingredient('dummy', now, future)
        self.assertFalse(ingredient.is_expired(now))

    def test_dish_expired(self):
        dish = Dish('dummy')
        now = datetime.datetime.now()
        ingredient1 = Ingredient('dummy', now, now)
        ingredient2 = Ingredient('dummy2', now, now)
        dish.add_ingredient(ingredient1)
        dish.add_ingredient(ingredient2)
        time.sleep(10)
        can_prepare = dish.can_prepare(datetime.datetime.now())
        self.assertFalse(can_prepare)


if __name__ == '__main__':
    unittest.main()
