spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[-1])

print(spam[0:4])

print(spam[1:3])

print(spam[0:-1])

print(spam[:2])

print(spam[:])

#para remplazar elementos:

spam[1] = 'hola'

print(spam)
      
spam = spam + ['a', 'b', 'c']

print(spam)

#Removiendo elementos

del spam[2]

print(spam)

catName1 = 'Zophie'
catName2 = 'Pooka'
catName3 = 'Simon'
catName4 = 'Lady Macbeth'
catName5 = 'Fat-tail'
catName6 = 'Miss Cleo'

print('Enter the name of cat1:')
catName1 = input()
print('Enter the name of cat2:')
catName2 = input()
print('Enter the name of cat3:')
catName3 = input()
print('Enter the name of cat4:')
catName4 = input()
print('Enter the name of cat5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
print('The cat names are:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' +
catName5 + ' ' + catName6)

