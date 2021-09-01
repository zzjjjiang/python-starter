

myList = [
  { 'name' : 'fred', 'age' : 30 },
  { 'name' : 'joe', 'age' : 25 },
  { 'name' : 'sue', 'age' : 30 },
  { 'name' : 'mary', 'age' : 10 }
]

# sortedList2 = myList.sort(key = lambda x: x['age'])
# sortedList3 = sorted(myList, key = lambda x: x['age'])

myList2 = list(filter(lambda x: x['age'] > 25, myList))
# print(myList2)

def sub(x, y):
  return x - y

def add(x, y):
  return x + y

num1 = 1
num2 = 2
sub(num1, num2)
r = add(num1, num2)


# print(sortedList2)
# print(sortedList3)

myList = [1,2,3]
myList.append(4)
myList.remove(2)
print(myList)

myNumList = [1,2,3]

lambda x: x * 2
