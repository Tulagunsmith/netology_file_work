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
    order_list = {}
    person = person_count
    for i in range(len(dishes)):
        if dishes[i] in cook_book:
            for j in range(len(cook_book[dishes[i]])):
                dictionary = dict_to_dict(cook_book[dishes[i]][j], person)
                dict_key = dict_to_str(dictionary)
                if dict_key not in order_list:
                    order_list.update(dictionary)

                else:
                    dictionary[dict_key]['quantity'] = str(
                        int(dictionary[dict_key]['quantity']) + int(order_list[dict_key]['quantity']))
                    order_list.update(dictionary)

    return order_list


shop_list = get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель', 'Фахитос'], 1)
print(shop_list)
