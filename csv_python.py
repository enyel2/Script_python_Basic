import csv

exampleFile = open('/home/enbelyert/Dropbox/Script_py/automate_online-materials/example.csv')
exampleReader = csv.reader(exampleFile)

#exampleData = list(exampleReader)

# en la terminal -> exampleData
# exampleData[0][0]
# exampleData[0][1]
# exampleData[0][2]
# exampleData[1][1]
# exampleData[6][1]

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
