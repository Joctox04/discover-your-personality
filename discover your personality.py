#Elaborado por: Jocsan Pérez y José Andres Salazar
#Fecha de Creación: 30/05/2022 11:00am
#Fecha de última Modificación: 17/05/2022 10:00pm
#Versión: 3.10.2

#=========== Importación de librerías ===========
from funciones import*
from archivos import*

#=========== Importación de librerías Externas para la interfaz ============
from tkinter import *
import tkinter
from tkinter import font
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#======================== VENTANA PRINCIPAL ===================================
ventana = tkinter.Tk() 
#======================== Ventanas Secundarias ===================================
registraDatos = Toplevel(ventana)
registraDatos.withdraw()#Oculta la ventana de registra Datos

registroDina = Toplevel(ventana)
registroDina.withdraw()

modificar = Toplevel(ventana)
modificar.withdraw()

datosAModificar = Toplevel(ventana)
datosAModificar.withdraw()

SioNO = Toplevel(ventana)
SioNO.withdraw()#Oculta la ventana de elegir si o no

eliminarDatos = Toplevel(ventana)
eliminarDatos.withdraw()

justiEliminar = Toplevel(ventana)
justiEliminar.withdraw()

SioNO2 = Toplevel(ventana)
SioNO2.withdraw()#Oculta la ventana de elegir si o no

reportes = Toplevel(ventana)
reportes.withdraw()#Oculta la ventana de reportes

elegir = Toplevel(ventana)
elegir.withdraw()#Oculta la ventana de elegir personalidad

infoPersona = Toplevel(ventana)
infoPersona.withdraw() #Oculta la ventana de información de persona

fecha = str(fechaActual) #la fecha actual
#==============================================================
#================  FUNCIONES PARA LAS VENTANAS  ===============
#==============================================================
def cambiarEstado(): #cambia estado
    boton1['state'] = tk.NORMAL
    boton2['state'] = tk.NORMAL
    boton5["state"] = tk.NORMAL
    messagebox.showinfo(message="La base de datos de personalidades ha sido cargada con éxito", title="Excelente trabajo")
    return

def cambiarEstado2():
    boton3["state"] = tk.NORMAL
    boton4["state"] = tk.NORMAL
    boton6["state"] = tk.NORMAL
    return

def mostrar(ventana): ventana.deiconify()#mostrar una ventana
def ocultar(ventana):ventana.withdraw()#ocultar una ventana
def ejecutar(f): ventana.after(130,f)#para que haya un lapso de tiempo entre cerrar y abrir ventanas

def eliminarTextoEntry1(): #elimina texto
    entry1.delete(0,"end")
    return ""

def eliminarTextoEntry2(): #elimina texto
    entry2.delete(0,"end")
    return ""

def eliminarTextoEntry3(): #elimina texto
    entry3.delete(0,"end")
    return ""

def eliminarTextoEntry4(): #elimina texto
    entry4.delete(0,"end")
    return ""

def eliminarTextoEntry6(): #elimina texto
    entry6.delete(0,"end")
    return ""

def eliminarTextoEntry7(): #elimina texto
    entry7.delete(0,"end")
    return ""

def eliminarTextoEntry8(): #elimina texto
    entry8.delete(0,"end")
    return ""

#============================= Funciones de procesamiento de las ventanas ==============================

#============================= Funcion registrar una persona ======================================
def recibeRegistrar():
    cedula = entry1.get()
    nombre = entry2.get()
    genero = seleccion.get() #hombre = 1, mujer = 2
    personalidad = personali.get()

    pais = country.get()
    if verificaCedula(cedula) == True:
        for i in listadePersonas:
            if cedula in i:
                messagebox.showinfo(message="Esa cédula ya existe registrada", title="Error")
                return
        if verificaNombre(nombre) == True:
            if genero == 1 or genero == 2:
                if personalidad == "":
                    messagebox.showinfo(message="Debe de indicar una personalidad", title="Error")
                    return
                else:
                    if pais == "":
                        messagebox.showinfo(message="Debe de indicar un país", title="Error")
                        return
                    else:
                        if genero == 1:
                            genero = True #hombre
                        if genero == 2:
                            genero = False #mujer
                        estado = [True,"",fechaActual]
                        personalidad = obtenerPersonali(personalidad)
                        pais = obtenerPaises(pais)
                        registrarPersona(cedula,nombre,genero,personalidad,pais,estado) #Funcion para registrar los datos
                        cambiarEstado2()
                        return ejecutar(mostrar(ventana)),ejecutar(ocultar(registraDatos)) 
            else:
                messagebox.showinfo(message="Debe de ingresar un genero", title="Error")
                return
        else:
            messagebox.showinfo(message="Debe ser como el siguiente formato:\n nombre apellido1-apellido2", title="Error")
            eliminarTextoEntry2()
            return
    else:
        messagebox.showinfo(message="Debe de ingresar una cédula correcta", title="Error")
        eliminarTextoEntry1()
        return

#============================= Funcion ingresar una cantidad aleatoria de personas ======================================
def recibeNpersonas():
    num = entry3.get()
    if verificaNum(num) == True:
        num = int(num)
        if num > 24:
            IngresarNpersonas(num)
            eliminarTextoEntry3()
            messagebox.showinfo(message="Se han creado "+str(num)+" personas", title="Error")
            cambiarEstado2()
            return ejecutar(mostrar(ventana)),ejecutar(ocultar(registroDina))
        else:
            messagebox.showinfo(message="Debe de ingresar un numero mayor o igual a 25", title="Error")
            eliminarTextoEntry3()
            return
    else:
        messagebox.showinfo(message="Debe de ingresar un numero por favor", title="Error")
        eliminarTextoEntry3()
        return

#============================= Funcion modificar una persona ======================================
def recibeModificar():
    cedula = entry4.get()
    if verificaCedula(cedula) == True:
        for i in listadePersonas:
            if cedula == i[0]:
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

                messagebox.showinfo(title="Datos obtenidos",
                message = "\nSu Cédula es: " +str(i[0])+ 
                "\nSu Nombre es: " +str(i[1])+ 
                "\nSu genero es: "+genero+
                "\nSu personalidad es: " +personalidad[0]+", "+personalidad[1]+
                "\nSu país es: " +pais+
                "\nSu estado actual es: " +estado)
                return ejecutar(mostrar(datosAModificar)),ejecutar(ocultar(modificar))
        else:  
            messagebox.showinfo(title="Lo sentimos",
            message = " La cedula indica no existe registrada ")
            eliminarTextoEntry4()
            return ejecutar(mostrar(ventana)),ejecutar(ocultar(modificar))
    else:
        messagebox.showinfo(message="Debe de ingresar una cédula correcta", title="Error")
        eliminarTextoEntry4()
        return

#============================= Funcion para modificar la personalidad ======================================
def modificarPersonalidad():
    cedula = entry4.get()
    nuevaPersonali = personali2.get() # la nueva personalidad
    nuevaPersonali = obtenerPersonali(nuevaPersonali)
    for i in listadePersonas:
        if cedula == i[0]:
            i[3] = nuevaPersonali # la nueva personalidad

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

            messagebox.showinfo(title="Nuevos Datos",
            message = "\nSu Cédula es: " +str(i[0])+ 
            "\nSu Nombre es: " +str(i[1])+ 
            "\nSu genero es: "+genero+
            "\nSu personalidad es: " +personalidad[0]+", "+personalidad[1]+
            "\nSu país es: " +pais+
            "\nSu estado actual es: " +estado)
            eliminarTextoEntry4()

            return ejecutar(mostrar(ventana)),ejecutar(ocultar(SioNO))

#==================== Funcion para eliminar una persona =========================
def recibeEliminar():
    cedula = entry6.get()
    if verificaCedula(cedula) == True:
        for i in listadePersonas:
            if cedula == i[0]:
                if i[5][0] == False:
                    messagebox.showinfo(title="Cuidado",
                    message = "Esa persona ya se encuentra prescindida de los servicios profesionales de esa persona en la compañía")
                    eliminarTextoEntry6()
                    return ejecutar(mostrar(ventana)),ejecutar(ocultar(eliminarDatos))
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

                messagebox.showinfo(title="Datos obtenidos",
                message = 
                "\nSu Cédula es: " +str(cedula)+ 
                "\nSu Nombre es: " +str(i[1])+ 
                "\nSu genero es: "+genero+
                "\nSu personalidad es: " +personalidad[0]+", "+personalidad[1]+
                "\nSu país es: " +pais+
                "\nSu estado actual es: " +estado)
                return ejecutar(mostrar(justiEliminar)),ejecutar(ocultar(eliminarDatos))
        else:  
            messagebox.showinfo(title="Lo sentimos",
            message = " La cedula indica no existe registrada ")
            eliminarTextoEntry6()
            return ejecutar(mostrar(ventana)),ejecutar(ocultar(eliminarDatos))
    else:
        messagebox.showinfo(message="Debe de ingresar una cédula correcta", title="Error")
        eliminarTextoEntry6()
        return

#==================== Funcion para recibir la justificacion y eliminar una persona =========================
def recibeJusti():
    cedula = entry6.get()
    justificacion = entry7.get()
    for i in listadePersonas:
        if cedula == i[0]:
            if i[2] == True: #HOMBRE
                genero = "hombre"
            if i[2] == False: #MUJER
                genero = "Mujer"
            num = i[3][1] #para saber la personalidad
            personalidad = listaPersonalidades[num] #para saber la personalidad, regresa en una pequeña lista
            num = i[4] #Para saber el pais
            pais = listaPaises[num] #Para saber el pais
            i[5][0] = False
            if i[5][0] == False:
                estado = "Inactivo"
            i[5][1] = justificacion
            i[5][2] = fecha
            ejecutar(ocultar(SioNO2))

            messagebox.showinfo(title="Sus nuevos datos obtenidos",
            message = 
            "\nSu Cédula es: " +str(cedula)+ 
            "\nSu Nombre es: " +str(i[1])+ 
            "\nSu genero es: "+genero+
            "\nSu personalidad es: " +personalidad[0]+", "+personalidad[1]+
            "\nSu país es: " +pais+
            "\nSu justificacion fue: " +justificacion+
            "\nSu nuevo estado actual es: " +estado)

            eliminarTextoEntry6()
            eliminarTextoEntry7()
            return ejecutar(mostrar(ventana))

#============================== Funciones de reportes ===================================
#=================== Funcion para elegir cuales personalidades ver ======================
def recibeElegir():
    perso = personali2.get()
    if perso == "":
        messagebox.showinfo(message="Debe de indicar una personalidad", title="Error")
        return
    else:
        grabaTiposPersonali("Tipos-"+fecha+".html",perso)
        messagebox.showinfo(message="Se ha creado un html con los datos de las personas\n con la personalidad: "+perso, title="Éxito")
        return ejecutar(mostrar(ventana)),ejecutar(ocultar(elegir))

#=========== Funcion para ver la información de una persona ==============
def recibeInfoPersona():
    cedula = entry8.get()
    if verificaCedula(cedula) == True:
        for i in listadePersonas:
            if i[0] == cedula:
                grabaPersona("Persona-"+fecha+".html",cedula)
                messagebox.showinfo(message="Se ha creado un html con los datos de la persona", title="Éxito")
                eliminarTextoEntry8()
                return ejecutar(mostrar(ventana)),ejecutar(ocultar(infoPersona))
        else:
            messagebox.showinfo(message="Esa cedula no existe registrada", title="Error")
            eliminarTextoEntry8()
            return
    else:
        messagebox.showinfo(message="Debe de ingresar una cédula correcta", title="Error")
        eliminarTextoEntry8()
        return

#=========== Funcion para ver la información de las personas retiradas ==============
def recibeRetirados():
    existe = False
    for i in listadePersonas:
        if i[5][0] == False:
            existe = True
    if existe == True:
        grabaRetirados("Retirados-"+fecha+".html")
        messagebox.showinfo(message="Se ha creado un HTML con los datos de las personas retiradas", title="Éxito")
        return
    messagebox.showinfo(message="No existen personas retiradas", title="Lo sentimos")
    return

#==========================================================================================
#=============           CONFIGURACIÓN DE LAS VENTANAS SECUNDARIAS           ==============
#==========================================================================================
#==========================================================================================
#==========            Configuración de la ventana Registrar Datos            =============
#==========================================================================================
registraDatos.geometry("700x600") #Dimensiones: Anchura x ALtura  
registraDatos.configure(background="white") #cambia de color el fondo

#========= Configuración del título ==================
Label(registraDatos, text="Registrar datos",fg = "black", bg = "white", font=("Arial Baltic",18),).grid(row=0, column=0, sticky="w") 

textEntry = tk.StringVar()
textEntry.set("Activo")

#======== Configuración de etiquetas y cajas de textos ============
#-----Etiqueta Cédula----
Label(registraDatos,text="Cédula (ejemplo: #-####-####)", fg="black",bg="white", font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")
#Caja de texto.
entry1 = Entry(registraDatos,background="#ffa500",font=font.Font(family="Times", size=14))
entry1.grid(row=1, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#-----Etiqueta Nombre----
Label(registraDatos,text="Nombre (Ejemplo: Nombre apellido1-apellido2)", fg="black",bg="white", font=("Arial Baltic", 12)).grid(row=2, column=0, sticky="w")
#Caja de texto.
entry2 = Entry(registraDatos,background="#ffa500",font=font.Font(family="Times", size=14))
entry2.grid(row=2, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#-----Etiqueta Genero----
Label(registraDatos,text="Genero",fg="black",bg="white", font=("Arial Baltic", 12)).grid(row=3, column=0, sticky="w")

#botones
seleccion = IntVar()
hombre = Radiobutton(registraDatos, text="Hombre",background="white",font=font.Font(family="Times", size=12), variable = seleccion, value =1).grid(
sticky="w", row=3,column=1, padx=5, ipadx=90, pady=3, ipady=3)
mujer = Radiobutton(registraDatos, text="Mujer", background="white",font=font.Font(family="Times", size=12), variable = seleccion, value = 2).grid(
sticky="w", row=4, column=1, padx=5, ipadx=90, pady=3, ipady=3)

#-----Etiqueta Personalidad----
Label(registraDatos,text="Personalidad", fg="black",bg="white", font=("Arial Baltic", 12)).grid(row=5, column=0, sticky="w")
#Caja de selección.
personali = ttk.Combobox(registraDatos,state = "readonly",values = listaPersonalidades) #-------------------------------------------------------
personali.grid(row=5, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#-----Etiqueta País ----
Label(registraDatos,text="País", fg="black",bg="white", font=("Arial Baltic", 12)).grid(row=6, column=0, sticky="w")
#Caja de selección.    
country = ttk.Combobox(registraDatos,state = "readonly",values = listaPaises) #---------------------------------------------------------------
country.grid(row=6, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#============== Configuración de los botones ===============
#----Boton Insertar----
insertar = tkinter.Button(registraDatos, text="Insertar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [recibeRegistrar()]).place(relx=0.04, rely=0.85, relwidth=0.3, relheight=0.09)

#----Boton Limpiar----
limpiar = tkinter.Button(registraDatos, text="Limpiar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [eliminarTextoEntry1(),eliminarTextoEntry2()]).place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.09)

#----Boton Regresar----
regresar = tkinter.Button(registraDatos, text="Regresar", fg = "white",bg = "black", font = "Arial",
command = lambda: [ejecutar(ocultar(registraDatos)),ejecutar(mostrar(ventana)),eliminarTextoEntry1(),eliminarTextoEntry2()]).place(relx=0.66, rely=0.85, relwidth=0.3, relheight=0.09)

#========================================================================================
#=============    Configuración de la ventana Registro Dinámico     ===================== ############################################
#========================================================================================
registroDina.geometry("500x200") #Dimensiones: Anchura x ALtura  
registroDina.configure(background="white") #cambia de color el fondo
registroDina.resizable(width=0, height=0)

#========= Configuración del título ======================
Label(registroDina,text="Ingresar participantes \naleatorios",fg = "black",  bg = "white", font=("Arial Baltic",18)).grid(row=0, column=0, sticky="w") 

#========= Configuración de la etiqueta ======================
#-----Etiqueta Cantidad a generar----
Label (registroDina,text="Cantidad a generar:\n (un numero mayor o igual a 25)", fg="black", bg="white", font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")

#Caja de texto.
entry3 = Entry(registroDina,background="#ffa500",font=font.Font(family="Times", size=14))
entry3.grid(row=1, column=1, padx=1, ipadx=20, pady=15, ipady=10)

#============== Configuración de los botones ===============
#----Boton Insertar----
insertar = tkinter.Button(registroDina, text="Insertar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [recibeNpersonas()]).place(relx=0.04, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Limpiar----
limpiar = tkinter.Button(registroDina, text="Limpiar",fg = "white", bg = "black", font = "Arial", 
command = eliminarTextoEntry3).place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Regresar----
regresar = tkinter.Button(registroDina, text="Regresar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(ocultar(registroDina)),ejecutar(mostrar(ventana)),eliminarTextoEntry3()]).place(relx=0.66, rely=0.7, relwidth=0.3, relheight=0.20)

#===================================================================================
#=============          Configuración de la ventana Modificar         ==============
#===================================================================================
modificar.geometry("500x200") #Dimensiones: Anchura x ALtura  
modificar.configure(background="white") #cambia de color el fondo
modificar.resizable(width=0, height=0)

#========= Configuración del título ======================
Label(modificar, text="Modificar Persona",fg = "black",  bg = "white",  font=("Arial Baltic",18),).grid(row=0, column=0, sticky="w") 

#========= Configuración de la etiqueta ======================
#-----Etiqueta Cantidad a generar----
Label(modificar,text="Cédula de la persona", fg="black",bg="white", font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")
#Caja de texto.
entry4 = Entry(modificar,background="#ffa500",font=font.Font(family="Times", size=14))
entry4.grid(row=1,  column=1, padx=10, ipadx=50, pady=15, ipady=10)

#============== Configuración de los botones ===============
#----Boton Insertar----
insertar = tkinter.Button(modificar, text="Insertar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [recibeModificar()]).place(relx=0.04, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Limpiar----
limpiar = tkinter.Button(modificar, text="Limpiar", fg = "white", bg = "black", font = "Arial", 
command = eliminarTextoEntry4).place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Regresar----
regresar = tkinter.Button(modificar, text="Regresar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(ocultar(modificar)),ejecutar(mostrar(ventana)),eliminarTextoEntry4()]).place(relx=0.66, rely=0.7, relwidth=0.3, relheight=0.20)

#==========================================================================================
#==========            Configuración de la ventana Datos a modificar          =============
#==========================================================================================
datosAModificar.geometry("650x200") #Dimensiones: Anchura x ALtura  
datosAModificar.configure(background="white") #cambia de color el fondo

#========= Configuración del título ======================
Label(datosAModificar, text="Modificar Personalidad",fg = "black",  bg = "white",font=("Arial Baltic",18)).grid(row=0, column=0, sticky="w") 

#======== Configuración de etiquetas y cajas de textos ============
#-----Etiqueta Cédula----
Label(datosAModificar,text="Nueva personalidad", fg="black",bg="white", font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")
#Caja de selección.
personali2 = ttk.Combobox(datosAModificar,state = "readonly",values = listaPersonalidades) 
personali2.grid(row=1, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#============== Configuración de los botones ===============
#----Boton Insertar----
insertar = tkinter.Button(datosAModificar, text="Insertar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(ocultar(datosAModificar)),ejecutar(mostrar(SioNO))]).place(relx=0.04, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Regresar----
regresar = tkinter.Button(datosAModificar, text="Regresar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(ocultar(datosAModificar)),ejecutar(mostrar(ventana)),eliminarTextoEntry4()]).place(relx=0.66, rely=0.7, relwidth=0.3, relheight=0.20)

#----------------------------------------------------------------------------------------------------
#=============== Ventana SI o NO ==================
#----------------------------------------------------------------------------------------------------
SioNO.geometry("240x150") #Dimensiones: Anchura x ALtura  
SioNO.configure(background="white") #cambia de color el fondo
Label(SioNO, text="Desea continuar?", fg = "black",bg="white", font=("Arial Baltic",20),).grid(row=0,column=1) 

#----Boton SI----
si = Button(SioNO, text="Si", fg = "white", bg = "black", font = "Arial",
command = lambda: modificarPersonalidad()).place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton NO----
no = Button(SioNO, text="No", fg = "white", bg = "black", font = "Arial",
command = lambda: [messagebox.showinfo(message="Se ha cancelado", title="Procedimiento cancelado"),eliminarTextoEntry4(),ejecutar(ocultar(SioNO)),ejecutar(mostrar(ventana))]).place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.20)

#========================================================================================
#=============          Configuración de la ventana Eliminar Datos         ==============
#========================================================================================
eliminarDatos.geometry("500x200") #Dimensiones: Anchura x ALtura  
eliminarDatos.configure(background="white") #cambia de color el fondo
eliminarDatos.resizable(width=0, height=0)

#========= Configuración del título ======================
Label(eliminarDatos, text="Eliminar Datos",fg = "black", bg = "white", font=("Arial Baltic",18),).grid(row=0, column=0, sticky="w") 

#========= Configuración de la etiqueta ======================
#-----Etiqueta Cantidad a generar----
Label(eliminarDatos,text="Cédula de la persona", fg="black",bg="white", font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")
#Caja de texto.
entry6 = Entry(eliminarDatos,background="#ffa500",font=font.Font(family="Times", size=14))
entry6.grid(row=1,  column=1, padx=10, ipadx=50, pady=15, ipady=10)

#============== Configuración de los botones ===============
#----Boton Insertar----
insertar = tkinter.Button(eliminarDatos, text="Insertar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [recibeEliminar()]).place(relx=0.04, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Limpiar----
limpiar = tkinter.Button(eliminarDatos, text="Limpiar", fg = "white", bg = "black", font = "Arial", 
command = eliminarTextoEntry6).place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Regresar----
regresar = tkinter.Button(eliminarDatos, text="Regresar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(mostrar(ventana)),ejecutar(ocultar(eliminarDatos))]).place(relx=0.66, rely=0.7, relwidth=0.3, relheight=0.20)

#==================================================================================================
#==========            Configuración de la ventana Eliminar Datos Justificacion       =============
#==================================================================================================
justiEliminar.geometry("650x200") #Dimensiones: Anchura x ALtura  
justiEliminar.configure(background="white") #cambia de color el fondo

#========= Configuración del título ======================
Label(justiEliminar, text="Justificacion",fg = "black", bg = "white", font=("Arial Baltic",18)).grid(row=0, column=0, sticky="w") 

#======== Configuración de etiquetas y cajas de textos ============
#-----Etiqueta Cédula----
Label(justiEliminar,text="Ingrese la justificacion", fg="black",bg="white", font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")
#Caja de texto.
entry7 = Entry(justiEliminar,background="#ffa500",font=font.Font(family="Times", size=14))
entry7.grid(row=1, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#============== Configuración de los botones ===============
#----Boton Insertar----
insertar = tkinter.Button(justiEliminar, text="Insertar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(mostrar(SioNO2)),ejecutar(ocultar(justiEliminar))]).place(relx=0.04, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Limpiar----
limpiar = tkinter.Button(justiEliminar, text="Limpiar", fg = "white", bg = "black", font = "Arial", 
command = eliminarTextoEntry7).place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Regresar----
regresar = tkinter.Button(justiEliminar, text="Regresar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(mostrar(ventana)),ejecutar(ocultar(justiEliminar))]).place(relx=0.66, rely=0.7, relwidth=0.3, relheight=0.20)

#----------------------------------------------------------------------------------------------------
#=============== Ventana SI o NO ==================
#----------------------------------------------------------------------------------------------------
SioNO2.geometry("240x150") #Dimensiones: Anchura x ALtura  
SioNO2.configure(background="white") #cambia de color el fondo
Label(SioNO2, text="Desea continuar?", fg = "black",bg="white", font=("Arial Baltic",20),).grid(row=0,column=1) 

#----Boton SI----
si = Button(SioNO2, text="Si", fg = "white", bg = "black", font = "Arial",
command = lambda: recibeJusti()).place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton NO----
no = Button(SioNO2, text="No", fg = "white", bg = "black", font = "Arial",
command = lambda: [messagebox.showinfo(message="Se ha cancelado", title="Procedimiento cancelado"),
eliminarTextoEntry7(),eliminarTextoEntry6(),ejecutar(ocultar(SioNO2)),ejecutar(mostrar(ventana))]).place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.20)

#==================================================================================
#============        Configuración de la ventana Reportes     =====================
#==================================================================================
reportes.title("Reportes")
reportes.geometry("500x700") #Dimensiones: Anchura x ALtura  
reportes.configure(background="white") #cambia de color el fondo

#----Titulo---
Label(reportes, text="Reportes",fg = "black", bg = "white", font=("Arial Baltic",20)).pack(anchor=CENTER) 

#============== Configuración de los botones ===============
#----Boton de Personalidades---
personalidades = tkinter.Button(reportes,text= "Personalidades" ,fg = "white", bg = "black", font = "Arial", 
command= lambda: [grabaPersonalidades("personalidades-"+fecha+".html"),messagebox.showinfo(message="Se ha creado un HTML con los datos de las personalidades", title="Éxito")]
).place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1) #relwidth = x

#---Boton de Tipos de personalidades---
tiposPersonalidad = tkinter.Button(reportes,text= "Tipos de personalidad" ,fg = "white", bg = "black",font = "Arial", 
command= lambda: [ejecutar(ocultar(reportes)),ejecutar(mostrar(elegir))]
).place(relx=0.15, rely=0.17, relwidth=0.7, relheight=0.1)

#---Boton de Información de una persona--
informacionPersona = tkinter.Button(reportes,text= "Información de una persona" ,fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(ocultar(reportes)),ejecutar(mostrar(infoPersona))]
).place(relx=0.15, rely=0.29, relwidth=0.7,relheight=0.1)

#---Boton de Base de datos completa---
baseCompleta = tkinter.Button(reportes,text= "Base de datos completa" ,fg = "white", bg = "black", font = "Arial", 
command = lambda: [grabaBDcompleta("BDcompleta-"+fecha+".html"),messagebox.showinfo(message="Se ha creado un HTML con la base de datos completa", title="Éxito")]
).place(relx=0.15, rely=0.41, relwidth=0.7, relheight=0.1)

#---Boton de Retirados---
retirados = tkinter.Button(reportes,text= "Retirados" ,fg = "white", bg = "black", font = "Arial", 
command = lambda: [recibeRetirados()]
).place(relx=0.15, rely=0.53, relwidth=0.7, relheight=0.1)

#---Boton de Por país---
porPais = tkinter.Button(reportes,text= "Por país" ,fg = "white", bg = "black", font = "Arial", 
command = lambda: [grabaPorPais("Pais-"+fecha+".html"),messagebox.showinfo(message="Se ha creado un HTML con los datos de las personas por paises", title="Éxito")]
).place(relx=0.15, rely=0.65, relwidth=0.7, relheight=0.1)

#---Boton de salir---
salir = tkinter.Button(reportes, text="Salir", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))]
).place(relx=0.15, rely=0.85, relwidth=0.7, relheight=0.1)

#----------------------------------------------------------------------------------------------------
#=============== Ventana elegir personalidad ==================
#----------------------------------------------------------------------------------------------------
elegir.title("Elige la personalidad")
elegir.geometry("500x300") #Dimensiones: Anchura x ALtura  
elegir.configure(background="white") #cambia de color el fondo

#----Titulo---
Label(elegir, text="Elige la \npersonalidad",fg = "black",  bg = "white", font=("Arial Baltic",20)).grid(row=0, column=0, sticky="w") 

#-----Etiqueta Personalidad----
Label(elegir,text="Personalidad:", fg="black",bg="white", font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")
#Caja de selección.
personali2 = ttk.Combobox(elegir,state = "readonly",values = listaPer) #-------------------------------------------------------
personali2.grid(row=1, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#============== Configuración de los botones ===============
insertar = tkinter.Button(elegir, text="Insertar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [recibeElegir()]
).place(relx=0.1, rely=0.65, relwidth=0.7, relheight=0.1)

#---Boton de salir---
salir = tkinter.Button(elegir, text="Salir", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(ocultar(elegir)),ejecutar(mostrar(ventana))]
).place(relx=0.1, rely=0.85, relwidth=0.7, relheight=0.1)

#----------------------------------------------------------------------------------------------------
#=============== Ventana información de persona  ==================
#----------------------------------------------------------------------------------------------------
infoPersona.geometry("500x200") #Dimensiones: Anchura x ALtura  
infoPersona.configure(background="white") #cambia de color el fondo
infoPersona.resizable(width=0, height=0)

#========= Configuración del título ======================
Label(infoPersona,text="Buscar información de\n una persona",fg = "black",  bg = "white", font=("Arial Baltic",18),).grid(row=0, column=0, sticky="w") 

#========= Configuración de la etiqueta ======================
#-----Etiqueta Cantidad a generar----
Label (infoPersona,text="Ingrese la cedula de la \n persona a buscar", fg="black", bg="white", font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")

#Caja de texto.
entry8 = Entry(infoPersona,background="#ffa500",font=font.Font(family="Times", size=14))
entry8.grid(row=1, column=1, padx=1, ipadx=20, pady=15, ipady=10)

#============== Configuración de los botones ===============
#----Boton Insertar----
insertar = tkinter.Button(infoPersona, text="Insertar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [recibeInfoPersona()]).place(relx=0.04, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Limpiar----
limpiar = tkinter.Button(infoPersona, text="Limpiar",fg = "white", bg = "black", font = "Arial", 
command = eliminarTextoEntry3).place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Regresar----
regresar = tkinter.Button(infoPersona, text="Regresar", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(ocultar(infoPersona)),ejecutar(mostrar(ventana)),eliminarTextoEntry8()]).place(relx=0.66, rely=0.7, relwidth=0.3, relheight=0.20)

#==================================================================================
#==================================================================================
#=============         Configuración de la ventana PRINCIPAL            ===========
#==================================================================================
#==================================================================================
ventana.title("Personalidades") #da titulo a la ventana
ventana.geometry("500x750") #Dimensiones: Anchura x ALtura  
ventana.configure(background="white") #cambia de color el fondo
#ventana.resizable(width=0, height=0)#con esto no se puede modificar la ventana

#----Titulo---
Label(ventana, text="Tu personalidad",fg = "black",  bg = "white", font=("Arial Baltic",20)).pack(anchor=CENTER) 

#============== Configuración de los botones ===============
#----Boton de Cargar BD de personalidad---
#boton0 = tk.Button(ventana,text= "Cargar BD de personalidad", fg = "white", bg = "black", font = "Arial", 
#command = lambda: [cambiarEstado(),leerArchivoPerso("personalidades.txt")])
#boton0.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.09)

#----Boton de Registrar datos---
boton1 = tk.Button(ventana,text= "Registrar datos", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(mostrar(registraDatos)),ejecutar(ocultar(ventana))])
boton1.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.09)

#---Boton de Registro dinámico---
boton2 = tk.Button(ventana,text= "Registro dinámico", fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(mostrar(registroDina)),ejecutar(ocultar(ventana))]) 
boton2.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.09)

#---Boton de Modificar datos--
boton3 = tk.Button(ventana,text= "Modificar datos" ,state=tk.DISABLED, fg = "white", bg = "black", font = "Arial",
command = lambda: [ejecutar(mostrar(modificar)),ejecutar(ocultar(ventana))])
boton3.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.09)

#---Boton de Eliminar datos---
boton4 = tk.Button(ventana,text= "Eliminar datos",state=tk.DISABLED, fg = "white", bg = "black", font = "Arial", 
command = lambda: [ejecutar(mostrar(eliminarDatos)),ejecutar(ocultar(ventana))])
boton4.place(relx=0.15, rely=0.4, relwidth=0.7, relheight=0.09)

#---Boton de Crear XLM---
boton5 = tk.Button(ventana,text= "Crear XLM" ,state=tk.DISABLED, fg = "white", bg = "black", font = "Arial", 
command = lambda: [crearXml(),messagebox.showinfo(message="Se ha creado un XML con los datos de las personalidades", title="Éxito")])
boton5.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.09)

#---Boton de Reportes---
boton6 = tk.Button(ventana,text= "Reportes",state=tk.DISABLED, fg = "white", bg = "black",font = "Arial", 
command = lambda: [ejecutar(mostrar(reportes)),ejecutar(ocultar(ventana))])
boton6.place(relx=0.15, rely=0.6, relwidth=0.7, relheight=0.09)

#---Boton de salir---
salir = tk.Button(ventana, text="Salir", fg = "white", bg = "black", font = "Arial", 
command = ventana.destroy).place(relx=0.15, rely=0.85, relwidth=0.7, relheight=0.09)

#===== Bucle de la ventana ======
if diccPersonalidades != {}:
    ventana.mainloop() #llama a la ventana principal