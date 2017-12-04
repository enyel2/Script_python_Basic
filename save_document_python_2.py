helloFile = open('/home/enbelyert/Dropbox/Script_py/doc/doc_1.txt')

print(helloFile)

helloContent = helloFile.read()
print(helloContent)

sonnetFile = open('/home/enbelyert/Dropbox/Script_py/doc/sonnet29.txt')

x = sonnetFile.readlines()

print(x)

#la ruta, la escritura, el cierre

baconFile = open('/home/enbelyert/Dropbox/Script_py/doc/bacon.txt', 'w') 

baconFile.write('Hello world!\n')

baconFile.close() 

baconFile = open('/home/enbelyert/Dropbox/Script_py/doc/bacon.txt', 'a')

baconFile.write('Bacon is not a vegetable.')

baconFile.close()

baconFile = open('/home/enbelyert/Dropbox/Script_py/doc/bacon.txt')

content = baconFile.read()

baconFile.close()

print(content)


