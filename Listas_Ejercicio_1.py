#catNames = []

#while True:
#    print('Enter the name of cat ' + str(len(catNames) + 1) +
#        ' (Or enter nothing to stop.):')
#    name = input()
#    if name == '':
#        break
#    catNames = catNames + [name] # list concatenation
#print('The cat names are:')
#for name in catNames:
#    print(' ' + name)

#per = ['q','u','e']

#for i in per:
#    print(i)
    
#supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
#for i in range(len(supplies)):
#    print('Index ' + str((i)+1) + ' in supplies is: ' + supplies[i])

#formas de saber si un string es parte de una lista 
spam = ['hello', 'hi', 'howdy', 'heyas']

print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
print('cat' in spam)
print('howdy' not in spam)
print('cat' not in spam)

#operador +=

pet = 43
pet +=1
print(pet)
pet -=1
print(pet)
pet *=2
print(pet)
pet /=3
print(pet)
pet %=2
print(pet)
