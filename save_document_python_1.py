import os

#os.path.join('usr', 'bin', 'spam')

#myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
#for filename in myFiles:
#    print(os.path.join('C:\\Users\\asweigart', filename))


#os.makedirs('/home/enbelyert/Dropbox/Script_py/doc')

#os.makedirs('C:\\delicious\\walnut\\waffles') windows

#os.getcwd() si se escribe en la terminal se observa la ruta

path = '/home/enbelyert/Dropbox/Script_py/doc/doc_1.txt'

print(os.path.basename(path))

print(os.path.dirname(path))

#calcFilePath = '/home/enbelyert/Dropbox/Script_py/doc/doc_1.txt'
# en terminal  os.path.split(calcFilePath)
# en terminal calcFilePath.split(os.path.sep)

print(os.path.exists('/home/enbelyert/Dropbox'))
