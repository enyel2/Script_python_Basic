# Es mejor no trabajar con variables Globales debido a que se genera error
# en el tiempo


#def spam():
#    eggs = 31337
#print(eggs)

#spam()
#print(eggs)

#se esta llamando una variable local propia de la funcion spam
#y python lo considera como error pk no esta definda

#def spam():
#    eggs = 99
#    bacon()
#    print(eggs)

#def bacon():
#    ham = 101
#    eggs = 0

#spam()

#la variable eggs exite en ambas pero como es llamado por spam se impime 99=egg

#def spam():
#    eggs = 12
#    print(eggs)

#eggs = 42

#spam()
#print(eggs)

#este ejemplo muestra las diferencias entre una variable Global y local
#dependiendo de la funcion 

#def spam():
#    eggs = 'spam local'
#    print(eggs) # prints 'spam local'

#def bacon():
#    eggs = 'bacon local'
#    print(eggs) # prints 'bacon local'
#    spam()
#    print(eggs) # prints 'bacon local'

#eggs = 'global'
#bacon()
#print(eggs) # prints 'global'

#A variable named eggs that exists in a local scope when spam() is called.
#A variable named eggs that exists in a local scope when bacon() is called.
#A variable named eggs that exists in the global scope.
#POR ES MEJOR USAR DIFERENTES NOMBRES DE VARIABLES PARA NO GENERAR ERROR

#def spam():
#    global eggs
#    eggs = 'spam' # this is the global
#def bacon():
#    eggs = 'bacon' # this is a local
#def ham():
#    print(eggs) # this is the global

#eggs = 42 # this is the global
#spam()
#print(eggs)

#Tiene mas peso una variables global en una funcion definida

#def spam():
#    print(eggs) # ERROR!
#    eggs = 'spam local'

#eggs = 'global'
#spam()

#no esta definido eggs al inicio por eso el error





