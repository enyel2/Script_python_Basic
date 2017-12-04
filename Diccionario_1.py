#diccionario

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat)
print(myCat['size'])

print('My cat has ' + myCat['color'] + ' fur.')

#recordar q los diccionarios si se pueden declaran con numeros, pero no con 0

per = {4353: 'sdfsd', 5464: 'jety'}
print(per)

#diferencias con las listas ej:, los dicionarios no tiene un orden 

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}

print(eggs == ham)
