#Tic-Tac-Toe Board

#theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

#print(theBoard)

#def printBoard(board):
#    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#    print('-+-+-')
#    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#    print('-+-+-')
#    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#printBoard(theBoard)

#theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
#'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

#def printBoard(board):
#    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#    print('-+-+-')
#    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#    print('-+-+-')
#    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#printBoard(theBoard)


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|'+ board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|'+ board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|'+ board['low-M'] + '|' + board['low-R'])

turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    print('put move = top-L, or mid-M or low-R ')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
        
printBoard(theBoard)

#se define el diccionario, luego se crea< una funcion q imprime el diccionario, y se corre el for, en la terminal solo se elige el movimiento
          
