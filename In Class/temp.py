def createList():
    personList = [
    { 'ssn': '222-22-2222' , 'name' : 'charlie', 'weight' : 150 },
    { 'ssn': '333-33-3333' , 'name' : 'bob', 'weight' : 150 },
    { 'ssn': '555-55-5555' , 'name' : 'mary', 'weight' : 140 },
    { 'ssn': '444-44-4444' , 'name' : 'fred', 'weight' : 130 },
    { 'ssn': '111-11-1111' , 'name' : 'alex', 'weight' : 150 }
  ]
    return personList

def mapList(personList):
    personList = createList()
    mapped = list(map(lambda x : {x['name'] : x['weight'] - 10}, personList))

    print(mapped)


def main():
    personList = createList()
    mapList(personList)

if __name__ == "__main__":
    main() 