#
# File: temp.py
# Auth: Martin Burolla
# Date: 10/27/2021
# Desc: A temporary place to write python code.
#

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
    print(l);

    # l = list(map(lambda x : { 'short_name' : x['name'], 'new_age': x['age'] + 1 }, peopleList))
    # l = sum(list(map(lambda x : x['age'], peopleList)))

if __name__ == "__main__":
    main()
