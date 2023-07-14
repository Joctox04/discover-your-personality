#Elaborado por: Jocsan Pérez y José Andres Salazar
#Fecha de Creación: 30/05/2022 11:00am
#Fecha de última Modificación: 17/05/2022 10:00pm
#Versión: 3.10.2
#=========== Importación de librerías ============
from clases import*

#=========== Importación de librerías externas ============
from ast import DictComp
import re
from datetime import timedelta, date
from operator import index


import random



from secrets import choice
import xml.etree.ElementTree as ET

#=================== Listas Globales =====================
listadePersonas = []

diccPersonalidades = {}

listaPersonalidades = [] #se usa para la interfaz

listaPaises = [] #se usa para la interfaz

listaPer = [] #se usa para la interfaz

listadeCedulas = [] 

listaNombres = []

fechaActual = date.today() #para obtener la fecha actual
fecha = str(fechaActual) #para obtener la fecha actual

#======================================== validaciones =======================================================
def verificaCedula(cedula):
    if re.match("\d{1}\-{1}\d{4}\-{1}\d{4}",cedula): #verificación de la cédula ene ste formato: #-####-####
        return True
    return False


def verificaNombre(nombre):
    if re.match("\D+\s{1}\D+-{1}\D+",nombre): 
        return True
    return False


def verificaNum(num):
    if re.match("\d",num):
        return True
    return False

#================================= FUNCIONES =====================================
#==================== Crea un diccionario y una lista de personalidades y una miniLista de personalidades ==============================
def crearDiccionario(lista):
    listaTemp = []
    for i in lista:
        listaTemp.append(i[:-2])
    num = 0
    while num != 24:
        tipo = listaTemp[num] #cada tipo de personalidad
        descripcion = listaTemp[num+1] #la descripcion

        #subTipo numero 1
        subtipo1 = listaTemp[num+2][:-5]
        codigo1 = listaTemp[num+2][-4:]
        tupla1 = (subtipo1,codigo1)

        miniLista = [] 
        miniLista = [tipo,subtipo1]
        listaPersonalidades.append(miniLista) #para la interfaz 

        #subTipo numero 2
        subtipo2 = listaTemp[num+3][:-5]
        codigo2 = listaTemp[num+3][-4:]
        tupla2 = (subtipo2,codigo2)

        miniLista = [] 
        miniLista = [tipo,subtipo2]
        listaPersonalidades.append(miniLista) #para la interfaz

        #subTipo numero 3
        subtipo3 = listaTemp[num+4][:-5]
        codigo3 = listaTemp[num+4][-4:]
        tupla3 = (subtipo3,codigo3)

        miniLista = [] 
        miniLista = [tipo,subtipo3]
        listaPersonalidades.append(miniLista) #para la interfaz 

        #subTipo numero 4
        subtipo4 = listaTemp[num+5][:-5]
        codigo4 = listaTemp[num+5][-4:]
        tupla4 = (subtipo4,codigo4)

        miniLista = [] 
        miniLista = [tipo,subtipo4]
        listaPersonalidades.append(miniLista) #para la interfaz 

        diccPersonalidades[tipo] = descripcion,tupla1,tupla2,tupla3,tupla4

        listaPer.append(tipo)

        num += 6
    return diccPersonalidades,listaPersonalidades,listaPer

#==================== Crea una lista de paises ============================================
def crearListaPaises(lista):
    for i in lista:
        listaPaises.append(i[:-2])
    return listaPaises

#==================== Obtiene el valor de las personalidades (registrar persona) ==============================
def obtenerPersonali(valor): 
    valor = valor.split(" ")
    tipo = 0
    subcategoria = 0
    while subcategoria != 16:
        if valor == listaPersonalidades[subcategoria]:
            personalidad = (tipo,listaPersonalidades.index(listaPersonalidades[subcategoria]))
            return personalidad
        if subcategoria == 3:
            tipo += 1
        if subcategoria == 7:
            tipo += 1
        if subcategoria == 11:
            tipo += 1
        subcategoria += 1

#===================== Obtiene el valor de los paises (registrar persona) ==========================
def obtenerPaises(pais):
    for i in listaPaises:
        if pais == i:
            pais = listaPaises.index(i)
            return pais

#======================== Registrar Persona ============================
def registrarPersona(cedula,nombre,genero,personalidad,pais,estado):
    personaX = persona() #instaciación de la variable, llama al método init
    personaX.asignarCedula(cedula)
    personaX.asignarNombre(nombre)
    personaX.asignarGenero(genero)
    personaX.asignarPersonalidad(personalidad)
    personaX.asignarPais(pais)
    personaX.asignarEstado(estado)
    listadePersonas.append(personaX.indicarDatos())
    return listadePersonas

#==================== Obtiene el valor de las personalidades (para la función de crear n personas) ==============================
def obtenerPersonaliRandom(valor):
    tipo = 0
    subcategoria = 0
    while subcategoria != 16:
        if valor == listaPersonalidades[subcategoria]:
            personalidad = (tipo,listaPersonalidades.index(listaPersonalidades[subcategoria]))
            return personalidad
        if subcategoria == 3:
            tipo += 1
        if subcategoria == 7:
            tipo += 1
        if subcategoria == 11:
            tipo += 1
        subcategoria += 1

#==================== Obtiene el cédulas random (para la función de crear n personas) ==============================
def obtenerCedula():
    num1 = random.randint(1,9)
    num2 = random.randint(000,999)
    num3 = random.randint(000,999)
    if num3 < 99 or num2 < 99:
        return obtenerCedula()
    num4 = "0"
    num5 = "0"
    cedula = str(num1)+"-"+(num4)+str(num2)+"-"+(num5)+str(num3)
    if cedula in listadeCedulas:
        return obtenerCedula()
    else:
        listadeCedulas.append(cedula)
        return cedula

#==================== Obtiene el nombres random (para la función de crear n personas) ==============================
def DefineNombre():
    nombre = "Nombre"
    ap1 = "apellido"
    ap2 = "apellido"
    num = random.randint(00000,99999)
    nombre += str(num)
    ap1 += str(num)
    ap2 += str(num)
    ap1 += "-"
    apellido = ap1+ap2
    nombreFull = nombre +" "+ apellido
    if nombre in listaNombres: 
        return DefineNombre()
    else:
        listaNombres.append(nombre)
        return nombreFull

#=============== Funcion para generar una cantidad aleatoria de personas ===================
def IngresarNpersonas(num):
    for x in range(num):
        info = []
        cedula = obtenerCedula()
        if x % 2 == 0:
            nombre = DefineNombre()
            genero = True
        else:
            nombre = DefineNombre()
            genero = False
        pais = random.choice(listaPaises)
        pais = listaPaises.index(pais)
        personalidad = random.choice(listaPersonalidades)
        personalidad = obtenerPersonaliRandom(personalidad)
        estado = [True,"",fechaActual]
        info = [cedula,nombre,genero,personalidad,pais,estado]
        listadePersonas.append(info)
    return listadePersonas

#================= Funcion para determinar la personalidad =======================
def determinaPersonali(num):
    if num == 0:
        tipoPersonali = "Analistas"
    elif num == 1:
        tipoPersonali = "Diplomáticos"
    elif num == 2:
        tipoPersonali = "Centinelas"
    else:
        tipoPersonali = "Exploradores"       
    return tipoPersonali

#================= Funcion para determinar el subtipo de personalidad =======================
def determinaSubTipo(num):
    for i in listaPersonalidades:
        if num == listaPersonalidades.index(i):
            subTipo = i[1]
            return subTipo

#================= Funcion para determinar el pais =======================
def determinarPais(num):
    for i in listaPaises:
        if num == listaPaises.index(i):
            pais = i
            return pais

#================================ Funciones para crear el XML ============================
def prettify(element,indent=" "):
    queue = [(0,element)]
    while queue:
        level, element = queue.pop(0)
        children = [(level + 1, child) for child in list(element)]
        if children:
            element.text = "\n" + indent * (level+1)
        if queue:
            element.tail = "\n" + indent * queue[0][0]
        else:
            element.tail = "\n" + indent * (level-1)
        queue[0:0] = children
    return

def crearXml():
    personalidades = ET.Element("personalidades")
    for x in diccPersonalidades.keys():
        valores=diccPersonalidades[x]
        tipo = ET.SubElement(personalidades,"tipo="+x)
        ET.SubElement(tipo,"descripcion").text = valores[0]
        valores = valores[1:]
        conta=1
        for y in valores:
            ET.SubElement(tipo, "Subtipo"+str(conta)).text = y[0]
            ET.SubElement(tipo, "Codigo"+str(conta)).text = y[1]
            conta+=1
    tree = ET.ElementTree(personalidades)
    prettify(personalidades)
    tree.write("Personalidades.xml")
    return

#====================== Funciones para los reportes HTML ========================
#================================ Personalidades ================================
def grabaPersonalidades(archivo):
    try:
        hoja = open(archivo,"w")
        hoja.write("<html>\n")
        hoja.write("<head>\n")
        hoja.write("<title>Personalidades-"+fecha+"</title>\n")
        hoja.write("</head>\n\n")
        hoja.write("<body>\n")
        hoja.write("\t<header>\n")
        hoja.write("\t\t<h1>Personalidades</h1>\n")
        hoja.write("\t</header>\n")
        num = 0
        for i in diccPersonalidades:
            hoja.write(f"<table align=left cellspacing=2 cellpadding=2 border=1 bgcolor=#CC9BF5>\n")
            hoja.write(f"<td>{i}:</td>\n")
            hoja.write(f"<td>{(diccPersonalidades[i][0])}\
            {(diccPersonalidades[i][1][0])}:{str(diccPersonalidades[i][1][1])}\
            {(diccPersonalidades[i][2][0])}:{str(diccPersonalidades[i][2][1])}\
            {(diccPersonalidades[i][3][0])}:{str(diccPersonalidades[i][3][1])}\
            {(diccPersonalidades[i][4][0])}:{str(diccPersonalidades[i][4][1])}</td>")
            num += 1
        hoja.write("</body>\n")
        hoja.write("</html>")
        hoja.close()
    except Exception as e:
        print(f"Error:{e}")
    return

#====================== Tipo de personalidad =========================================
def grabaTiposPersonali(archivo,tipo):
    try:
        hoja = open(archivo,"w")
        hoja.write("<html>\n")
        hoja.write("<head>\n")
        hoja.write("<title>Tipos de personalidad-"+fecha+"</title>\n")
        hoja.write("</head>\n\n")
        hoja.write("<body>\n")
        hoja.write("\t<header>\n")
        hoja.write("\t\t<h1>Tipos de personalidad</h1>\n")
        hoja.write("\t</header>\n")
        hoja.write("\t\t<section>\n")
        hoja.write("\t\t\t<h2>Su tipo: "+tipo+"</h2>\n")
        for i in listadePersonas:
            if i[5][0] == True:
                if determinaPersonali(i[3][0]) == tipo:
                    pais = determinarPais(i[4])
                    subTipo = determinaSubTipo(i[3][1])
                    hoja.write("\t\t\t\t<p>Cédula: "+i[0])#cedula
                    hoja.write(", Nombre: "+i[1])#nombre
                    if i[2] == True:
                        hoja.write(", Genero: Hombre")
                    else:
                        hoja.write(", Genero: Mujer")
                    hoja.write(", subtipo: "+subTipo)
                    hoja.write(", País: "+pais+"</p>""\n")
        hoja.write("\t\t</section>\n")
        hoja.write("</body>\n")
        hoja.write("</html>")
        hoja.close()
    except Exception as e:
        print(f"Error:{e}")
    return

#================ Información de una persona =====================
def grabaPersona(archivo,cedula):
    try:
        hoja = open(archivo,"w")
        hoja.write("<html>\n")
        hoja.write("<head>\n")
        hoja.write("<title>Información de una persona-"+fecha+"</title>\n")
        hoja.write("</head>\n\n")
        hoja.write("<body>\n")
        hoja.write("<h1>Información de una persona</h1>\n") 
        for i in listadePersonas:
            if i[0] == cedula:
                if i[2] == True: #HOMBRE
                    genero = "hombre"
                if i[2] == False: #MUJER
                    genero = "Mujer"
                num = i[3][1] #para saber la personalidad
                personalidad = listaPersonalidades[num] #para saber la personalidad, regresa en una pequeña lista
                num = i[4] #Para saber el pais
                pais = listaPaises[num] #Para saber el pais
                if i[5][0] == True:
                    estado = "Activo"
                if i[5][0] == False:
                    estado = "Inactivo"
                hoja.write("\t<p>Su Cédula es: " +str(i[0])+"</p>\n") 
                hoja.write("\t<p>Su Nombre es: " +str(i[1])+"</p>\n")
                hoja.write("\t<p>Su genero es: "+genero+"</p>\n")
                hoja.write("\t<p>Su personalidad es: " +personalidad[0]+", "+personalidad[1]+"</p>\n")
                hoja.write("\t<p>Su país es: " +pais+"</p>\n")
                hoja.write("\t<p>Su estado actual es: " +estado+"</p>\n")
                break
        hoja.write("</body>\n")
        hoja.write("</html>")
        hoja.close()
    except Exception as e:
        print(f"Error:{e}")
    return

#================ Información completa =====================
def grabaBDcompleta(archivo):
    try:
        hoja = open(archivo,"w")
        hoja.write("<html>\n")
        hoja.write("<head>\n")
        hoja.write("<title>Información completa-"+fecha+"</title>\n")
        hoja.write("</head>\n\n")
        hoja.write("<body>\n")
        hoja.write("<h1>Información completa</h1>\n") 
        alternar = True
        for i in listadePersonas:
            if i[2] == True: #HOMBRE
                genero = "hombre"
            if i[2] == False: #MUJER
                genero = "Mujer"
            num = i[3][1] #para saber la personalidad
            personalidad = listaPersonalidades[num] #para saber la personalidad, regresa en una pequeña lista
            num = i[4] #Para saber el pais
            pais = listaPaises[num] #Para saber el pais
            if i[5][0] == True:
                estado = "Activo"
            if i[5][0] == False:
                estado = "Inactivo"
            if alternar == True:
                hoja.write(f"<table align=left cellspacing=2 cellpadding=2 border=1 bgcolor=#33E0FF>")
                hoja.write(f"<td>Cedula: {i[0]}, Nombre: {i[1]}, Genero: {genero}, Personalidad: {personalidad}, Pais: {pais}, Estado: {estado}</td>\n")
                alternar = False
            else:
                hoja.write(f"<table align=left cellspacing=2 cellpadding=2 border=1 bgcolor=#339FFF>")
                hoja.write(f"<td>Cedula: {i[0]}, Nombre: {i[1]}, Genero: {genero}, Personalidad: {personalidad}, Pais: {pais}, Estado: {estado}</td>\n")
                alternar = True
        hoja.write("</body>\n")
        hoja.write("</html>")            
        hoja.close()
    except Exception as e:
        print(f"Error:{e}")
    return

#================ Personas Retiradas del ambiente =====================
def grabaRetirados(archivo):
    try:
        hoja = open(archivo,"w")
        hoja.write("<html>\n")
        hoja.write("<head>\n")
        hoja.write("<title>Retirados del ambiente-"+fecha+"</title>\n")
        hoja.write("</head>\n\n")
        hoja.write("<body>\n")
        hoja.write("<h1>Retirados del ambiente</h1>\n") 
        for i in listadePersonas:
            if i[5][0] == False:
                fecha1 = ""
                fecha1 = str(i[5][2])
                justificacion = i[5][1]
                hoja.write("\t<p>Cédula: "+i[0])#cedula
                hoja.write(", Nombre: "+i[1])#nombre
                hoja.write(", Fecha: "+fecha1)#fecha
                hoja.write(", Justificacion: "+justificacion+"</p>\n")#justificacion
        hoja.write("</body>\n")
        hoja.write("</html>")
        hoja.close()
    except Exception as e:
        print(f"Error:{e}")
    return

#===================== Personas por pais ================================
def grabaPorPais(archivo):
    try:
        hoja = open(archivo,"w")
        hoja.write("<html>\n")
        hoja.write("<head>\n")
        hoja.write("<title>Personas por país-"+fecha+"</title>\n")
        hoja.write("</head>\n\n")
        hoja.write("<body>\n")
        hoja.write("<h1>Personas por país</h1>\n")        
        num = 0
        while num != len(listadePersonas):
            for i in listadePersonas:
                if num == i[4]:
                    hoja.write("\t<p>Cédula: "+i[0])#cedula
                    hoja.write(", Nombre: "+i[1])#nombre  
                    if i[5][0] == True:  
                        hoja.write(", Activo")
                    else:
                        hoja.write(", Inactivo")
                    hoja.write(", País: "+listaPaises[i[4]]+"</p>\n")
            num += 1
        hoja.write("</body>\n")
        hoja.write("</html>")
        hoja.close()
    except Exception as e:
        print(f"Error:{e}")
    return
