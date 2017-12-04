import random, sys, os, math

#gracias al module random
for i in range(5):
    print(random.randint(1, 10))

#gracias al module sys un while q sale solo cuando se escribe exit
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
