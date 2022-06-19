import os

base_path = os.getcwd()
file_name = 'file_work_1.py'
full_path = os.path.join(base_path, file_name)

from file_work_1 import cook_book


def dict_to_dict(dish_dict, person_count):
    piece_of_order = {}
    ingr_info = {'measure': dish_dict['measure'].strip(), 'quantity': f'{int(dish_dict["quantity"]) * person_count}'}
    key_ingr = dish_dict['ingredient_name']
    piece_of_order[key_ingr] = ingr_info
    return piece_of_order


def dict_to_str(dict_):
    keys, *values = dict_.items()
    str_ = keys[0]
    return str_


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    count = 0
    person = person_count
    for i in range(len(dishes)):
        if dishes[i] in cook_book:
            for j in range(len(cook_book[dishes[i]])):
                if len(dishes) != len(set(dishes)):
                    dictionary = dict_to_dict(cook_book[dishes[i]][j], person)
                    dict_key = dict_to_str(dictionary)
                    if dict_key not in shop_list:
                        shop_list.update(dictionary)

                    else:
                        dictionary[dict_key]['quantity'] = str(int(dictionary[dict_key]['quantity']) + int(shop_list[dict_key]['quantity']))



                        # print(dictionary[dict_key]['quantity'])
                        # print()
                        # print(shop_list[dict_key]['quantity'])

                        # print(dictionary)
                        # print(dict_key, len(dict_key))
                        # for key, values in dictionary.items():
                        #     count = int(values['quantity'])
                        #     print('dictionary quantity: ', values['quantity'])
                        # for key, values in shop_list.items():
                        #     values['quantity'] = int(values['quantity']) + count
                        #     count = 0

                        # for key, values in dictionary.items():
                        #     count = int(values['quantity'])
                        #     print(values['quantity'])
                        #     print(count)
                        #     for key, values in shop_list.items():
                        #         values['quantity'] = int(values['quantity']) + count
                        #         count = 0
                        shop_list.update(dictionary)

    return shop_list


shop_list = get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
print(shop_list)

