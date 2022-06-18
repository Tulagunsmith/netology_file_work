import os
from pprint import pprint
base_path = os.getcwd()
file_name = 'recipes.txt'
full_path = os.path.join(base_path, file_name)


def catalogue_reader(file_path):
    with open(file_path, encoding='utf-8') as file:
        result = {}
        for line in file:
            dish_name = line.strip()
            ingredients = []
            for item in range(int(file.readline())):
                ingredient = file.readline().split('|')
                ingredients.append({'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
            result[dish_name] = ingredients
            file.readline()
        return result


cook_book = catalogue_reader(full_path)
pprint(cook_book)


