#
# File: temp.py
# Auth: Martin Burolla
# Date: 10/27/2021
# Desc: A temporary place to write python code.
#

import random



def main():

    people_list = [
        {"firstname": "joe", "lastname": "smith", "age": 30},
        {"firstname": "peter", "lastname": "jones", "age": 66},
        {"firstname": "mary", "lastname": "jane", "age": 22},
        {"firstname": "sue", "lastname": "anderson", "age": 11},
    ]

    my_dict = {
        1: 'one',
        2: 'two',
        3: 'three '
    }

    #print(people_list)
    people_list.sort(key=lambda p: p['age'])
    #print(people_list)

    l = list(map(lambda p: {'age': p['age']}, people_list))
    print(l)

    foo()

def foo():
    my_list = []
    for _ in range(0, 10):
        my_list.append(random.randint(1, 100))
    print(my_list)
    # total = sum(my_list)
    # print(f'The sum is: {total}')


if __name__ == "__main__":
    main()
