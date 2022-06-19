from file_work_1 import cook_book


def dict_to_dict(dish_dictionary, person_count):
    piece_of_order = {}
    ingredient_info = {
        'measure': dish_dictionary['measure'].strip(), 'quantity': f'{int(dish_dictionary["quantity"]) * person_count}'}
    key_ingredient = dish_dictionary['ingredient_name']
    piece_of_order[key_ingredient] = ingredient_info
    return piece_of_order


def dict_to_str(dictionary):
    keys, *values = dictionary.items()
    string_ = keys[0]
    return string_


def get_shop_list_by_dishes(dishes, person_count):
    order_list = {}
    person = person_count
    for i in range(len(dishes)):
        if dishes[i] in cook_book:
            for j in range(len(cook_book[dishes[i]])):
                ingredient_data = dict_to_dict(cook_book[dishes[i]][j], person)
                ingredient = dict_to_str(ingredient_data)
                if ingredient not in order_list:
                    order_list.update(ingredient_data)

                else:
                    ingredient_data[ingredient]['quantity'] = str(
                        int(ingredient_data[ingredient]['quantity']) + int(order_list[ingredient]['quantity']))
                    order_list.update(ingredient_data)

    return order_list


shop_list = get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель', 'Фахитос'], 1)
print(shop_list)
