#ejercio de conteo de elemento en una oracion como caracteres

#message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
#count = {}
#for character in message:
#    count.setdefault(character, 0)
#    count[character] = count[character] + 1
#print(count)

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)



#impoty pprint imprime en forma vertical

dic = {'as': 'asd', 'plo':'sadf'}

#pprint.pprint sirve para listas anidadas o dicionarios
pprint.pprint(dic)
#pprint.pformat si se desea tener el valor del texto en cadena usarlo
print(pprint.pformat(dic))
