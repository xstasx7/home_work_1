from json import dump
from itertools import zip_longest

names = [
    'Иванов, Иван, Иванович \n',
    'Петров, Петр, Петрович \n',
    'Станислав, Стас, Станиславович \n'
    'Васильев, Василий, Васильевич'
]
hobby = ['скалолазание, охота \n'
         'рыбалка \n'
         'футбол \n'
         'вклопрогулки \n'
         'автомобили \n'
         ]
with open('users.csv', 'w', encoding='utf-8') as file_1:
    file_1.writelines(names)

with open('hobby.csv', 'w', encoding='utf-8') as file_2:
    file_2.writelines(hobby)

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        if len(users.readline()) >= len(hobby.readline()):
            users.seek(0)
            hobby.seek(0)
            with open('dict_n_json', 'w', encoding='utf-8') as f:
                all_list = zip_longest((''.join(us.split(',')) for us in users), hobby, fillvalue=None)
                my_dict = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}

                dump(my_dict, f, ensure_ascii=False, indent=4)
            print(my_dict)
        else:
            exit(1)
