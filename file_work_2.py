import os

base_path = os.getcwd()
file_name = 'file_work_1.py'
full_path = os.path.join(base_path, file_name)

from file_work_1 import cook_book


def dict_to_dict(dish_dict, person_count):
    piece_of_order = {}
    ingr_info = {'measure': dish_dict['measure'], 'quantity': f'{int(dish_dict["quantity"]) * person_count}'}
    key_ingr = dish_dict['ingredient_name']
    piece_of_order[key_ingr] = ingr_info
    return piece_of_order


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    person = person_count
    for i in range(len(dishes)):
        if dishes[i] in cook_book:
            for j in range(len(cook_book[dishes[i]])):
                dictionary = dict_to_dict(cook_book[dishes[i]][j], person)
                shop_list.update(dictionary)
    return shop_list

shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
print(shop_list)

