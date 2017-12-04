#birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

#while True:
#        print('Enter a name: (blank to quit)')
#        name = input()
#        if name == '':
#            break

#        if name in birthdays:
#            print(birthdays[name] + ' is the birthday of ' + name)
#        else:
#            print('I do not have birthday information for ' + name)
#            print('What is their birthday?')
#            bday = input()
#            birthdays[name] = bday
#            print('Birthday database updated.')

#print(birthdays)

spam = {'color': 'red', 'age': 42}

for v in spam.values():
    print(v)

for v in spam.keys():
    print(v)

for v in spam.items():
    print(v)

#forma de transformar las claves a lista
x = list(spam.keys())
print(x)

#k es la clave y str(v) es el valor
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))

#.setdefault no sobreescribe
spam.setdefault('name', 'juan')
print(spam)
spam.setdefault('name', 'elsa')
print(spam)
