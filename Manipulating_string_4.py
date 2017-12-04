def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 10)
printPicnic(picnicItems, 20, 20)

 
spam = '     Hello world    '
#imprimir directamen spam en la terminal

print(spam.strip())
#elimina todos los espacios vacios

print(spam.lstrip())
# elimina los espacio en blanco de la derecha

print(spam.rstrip())
# elimina los espacios en blanco de la izquierda
