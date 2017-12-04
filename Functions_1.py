#def hello():
#    print('Howdy!')
#    print('Howdy!!!')
#    print('Hello there.')

#hello()

#def hello(name):
#    print('Hello ' + name)

#hello('Enyel')
#hello('Eve')

import random

def getAnswer(answerNumber):

    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

#Hay dos formas de llamar y observar en pantalla el resultado    
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

#print(getAnswer(random.randint(1, 9)))

#None =  nil or Null es una valor nulo que tiene significado para python

#la funcion random.randint funciona usando numero de menor a mayor
