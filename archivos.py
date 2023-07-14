#Elaborado por: Jocsan Pérez y José Andres Salazar
#Fecha de Creación: 30/05/2022 11:00am
#Fecha de última Modificación: 17/05/2022 10:00pm
#Versión: 3.10.2

#=========== Importación de librerías ============
from funciones import*
import codecs
from tkinter import messagebox

#=========== Leer archivo de texto sobre los paises ==============
def leerArchivoPaises(nomArchLeer):
    lista = []
    try:
        f = codecs.open(nomArchLeer,"rb","utf-8") #utf-8 es la codificacion que usa el archivo
        num = 0
        for linea in f:
            lista.append(linea)
            num += 1
            if num == 15:
                f.close()
                return crearListaPaises(lista)
    except:
        return ""
leerArchivoPaises("paises.txt") 

#=========== Leer archivo de texto sobre las personalidades ==============
def leerArchivoPerso(nomArchLeer):
    lista = []
    try:
        f = codecs.open(nomArchLeer,"rb","utf-8") #utf-8 es la codificacion que usa el archivo
        for linea in f:
            lista.append(linea)
        f.close()
        return crearDiccionario(lista)
    except:
        messagebox.showinfo(message="No existe archivo que leer acerca de: " +nomArchLeer, title="Error")
        return ""
leerArchivoPerso("personalidades.txt")
