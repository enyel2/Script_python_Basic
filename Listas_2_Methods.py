#spam = ['hello', 'hi', 'howdy', 'heyas']
#spam.index('hello')

# El siguiente ejemplo muestra solo la posicion 1 y no la 3

#spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']

#print(spam.index('Pooka'))


#adicion de un elemento
#spam = ['cat', 'dog', 'bat']
#spam.append('moose')

#print(spam)

#spam = ['cat', 'dog', 'bat']
#spam.insert(1, 'chicken')

#print(spam)

#los metodos append and insert son solo para listas lo mismo para remove

#spam = ['cat', 'bat', 'rat', 'elephant']
#print(spam)
#spam.remove('bat')

#print(spam)

#remueve solo el primer cat de izq a derecha es bueno cuando sabes la posicion

#spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
#print(spam)
#spam.remove('cat')
#print(spam)

#spam = [2, 5, 3.14, 1, -7]
#print(spam)
#spam.sort()
#print(spam)

#la funcion sort solo ordena si la lista tiene solo integer o string
#word = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
#print(word)
#word.sort()
#print(word)
#word.sort(reverse=True)
#print(word)

# el sort ordena primero por mayusca y luego por minuscula en caso de string

# otra manera de ordenar usando el sort
example = ['a', 'z', 'A', 'Z']
example.sort(key=str.lower)

print(example)














