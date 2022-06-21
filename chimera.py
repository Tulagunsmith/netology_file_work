import os
base_path = os.getcwd()
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
chimera_file = '4.txt'
files = {0: file_name_1, 1: file_name_2, 2: file_name_3}
mega_file = {}


def file_reader(dictionary):
    file_data = {}
    with open(dictionary) as text:
        content = text.readlines()
        file_data['data'] = content
        file_data['name'] = dictionary
        file_data['length'] = len(content)
    return file_data


def mega_file_reader(mega_dict, file_dict):
    for i in range(len(file_dict)):
        mega_dict[(file_reader(file_dict[i]))['length']] = file_reader(file_dict[i])
    sorted_keys = sorted(mega_dict)
    sorted_mega_dict = {}
    for digit in sorted_keys:
        sorted_mega_dict[digit] = mega_dict[digit]
    return sorted_mega_dict


def file_writer(file_name):
    with open(file_name, 'a') as text:
        text.write(f'{crap["name"]}\n')
        text.write(f'{str(crap["length"])}\n')
        for line in crap['data']:
            text.write(line)


#file_writer(chimera_file)


mega_file = mega_file_reader(mega_file, files)
print(mega_file)
crap = file_reader(file_name_1)
print(crap)