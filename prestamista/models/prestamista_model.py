class Prestamista():
    lprestado = False
    def __init__(self, cui, nombre, apellido):
        self.__cui = cui
        self.__nombre = nombre
        self.__apellido = apellido
        
    def prestarlibro(self):
        global lprestado
        lprestado = True
    
    def devolverlibro(self):
        global lprestado
        lprestado = False
    
    def getcui(self):
        return self.__cui    
    def getnombre(self):
        return self.__nombre    
    def getapellido(self):
        return self.__apellido
     
    def getdatos(self):
        return{
            "cui": self.__cui,
            "nombre": self.__nombre,
            "apellido": self.__apellido            
        }
    
    