#varibles
#spam = 42
#cheese = spam
#spam = 100

#print(spam)
#print(cheese)

#listas
#primero = [0, 1, 2, 3, 4, 5]
#segundo = primero
#segundo[1] = 'Hello'

#print(primero)
#print(segundo)

#las listas generan un solo id que puede se llamado por diferentes nombres

#def eggs(someParameter):
#    someParameter.append('Hello')

#spam = [1, 2, 3]
#print(spam)
#eggs(spam)
#print(spam)

import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

#de esta manera se logra genera un id distinto para las listas



