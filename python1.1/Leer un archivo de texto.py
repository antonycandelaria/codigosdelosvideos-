file = open('cuento./libro.text')
#print(file.read())
 #print(file.readline())
 #print(file.readline())
 #print(file.readline())

for line in file:
    print(line)
file.close

with open('cuento./libro.text') as file: 
 for line in file:
    print(line)