with open('cuento./libro.text','r+') as file: 
 #('cuento./libro.text, r+') escritura y lectura 
 #('cuento./libro.text' 'w+') rescibre el archivo
 for line in file:
    print(line)
 file.write('nuevas lineas de  texto\n')
 file.write("nuevas lineas  de texto 2\n")
 file.write("nuevas lineas de  texto 3\n")
 file.write("nuevas lineas de  texto 4\n")