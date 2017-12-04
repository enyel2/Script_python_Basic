# This is a guess the number game.
#import random #module para tomar numero random

#secretNumber = random.randint(1, 20)
#print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
#for guessesTaken in range(1, 7):
#    print('Take a guess.')
#    guess = int(input())
#    if guess < secretNumber:
#        print('Your guess is too low.')
#    elif guess > secretNumber:
#        print('Your guess is too high.')
#    else:
#        break

# This condition is the correct guess!
#if guess == secretNumber:
#    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
#else:
#    print('Nope. The number I was thinking of was ' + str(secretNumber))


#def number(name):
#    if name % 2 == 0:
#        print ('Numero par')
#    else:
#        print ('No es par')

#number(6)

#def collatz(number):
#    if number % 2 == 0:
#        print(number//2)
#    else:
#        print(3*number+1)

#collatz(1)

def number(x):
    if x == 2:
        print('Numero Primo')
    elif x % 2 == 0:
        print('Numero par')
    for i in range(2,x):
        if x%i == 0:
            print ('Numero No primo')
            break
    else:
        print('Numero Primo')
        
number(2)

# Python program to check if the input number is prime or not

num = 125

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

















    
