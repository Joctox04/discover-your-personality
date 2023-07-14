#Elaborado por: Jocsan Pérez y José Andres Salazar
#Fecha de Creación: 30/05/2022 11:00am
#Fecha de última Modificación: 17/05/2022 10:00pm
#Versión: 3.10.2

#El programa define la clase "persona"
class persona:
    """Definición de Atributos de la clase"""
    """Definición de los métodos de la clase"""
    def __init__(self):
        """
        Método constructor = Crea la estructura de la clase 
        Método que se llama al instanciar
        """
        self.cedula = ""
        self.nombre = ""
        self.genero = 0
        self.personalidad = ""
        self.pais = ""
        self.estado = ""
        return

    def asignarCedula(self,cedula): 
        self.cedula = cedula
        return 

    def asignarNombre(self,nombre):
        self.nombre = nombre
        return 

    def asignarGenero(self,genero):
        self.genero = genero
        return 

    def asignarPersonalidad(self,personalidad): 
        self.personalidad = personalidad
        return 

    def asignarPais(self,pais):
        self.pais = pais
        return 

    def asignarEstado(self,estado):
        self.estado = estado
        return 

#=============================================================================================
    def indicarDatos(self):
        return [self.cedula,self.nombre,self.genero,self.personalidad ,self.pais ,self.estado]