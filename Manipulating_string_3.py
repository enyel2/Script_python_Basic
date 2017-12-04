#while True:
#    print('Enter your age:')
#    age = input()
#    if age.isdecimal():
#        break
#    print('Please enter a number for your age.')


#while True:
#    print('Select a new password (letters and numbers only):')
#    password = input()
#    if password.isalnum():
#        break
#    print('Passwords can only have letters and numbers.')

#es necesario revisar documentacion ambos no corren :D

x = ['cats', 'rats', 'bats']

print(', '.join(x))

y = ['My', 'name', 'is', 'Simon']

print(' '.join(y))

z = y

print('ABC'.join(z))

a = 'My name is Simon'

a = a.split()

print(a)


b = 'MyABCnameABCisABCSimon'

b = b.split('ABC')

print(b)

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

spam = spam.split('\n')

print(spam)
print(spam[4])

c = 'Hello'
print(c.rjust(10))

print('Hello'.ljust(10, '-'))
print('Hello'.ljust(20, '*'))

print('Hello'.center(20))
print('Hello'.center(20, '='))


#poner 'Hello'.ljust(10) en la terminal y ver el reslultado





