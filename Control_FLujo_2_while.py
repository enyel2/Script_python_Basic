#while age < 10:
#    print(age)
#    age = age + 1

#spam = 0

#-- con la sentencia if no se repite la palabra hello world
#if spam < 5:
#    print('Hello, world.')
#    spam = spam + 1

#while spam < 5:
#    print('Hello, world')
#    spam = spam + 1 


#name = ''

#-- En la terminar para que resulte es necesario escribirlo como string usando ''
#-- de esta manera el while estará cosntantemente en él ciclo 

#while name != 'Enyel':
#    print('Please type your name.')
#    name = input('')
#print('Thank you!')

#while True:
#    print('Please type your name.')
#    name = input()
#    if  name == 'Enyel':
#        break
#print('Thank you!')


while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')


    


