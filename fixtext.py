import sys
import os

path = os.getcwd()

arch = sys.argv[1]
path = path + f'\{arch}'
path = os.path.normpath(path)

print (path)

archivo = open (path,"r", encoding="utf8") 
contenido = archivo.read()
contenido_sin_saltos = contenido.replace("\n", " ")
archivo_nuevo= open ('nuevo_texto.txt', 'w', encoding="utf-8")
archivo_nuevo.write(contenido_sin_saltos)


