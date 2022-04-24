class Prestamista():
    def __init__(self, cui, last_name, first_name, lprestado):
        self.__cui = cui
        self.__last_name = last_name
        self.__first_name = first_name
        self.__lprestado  = lprestado
        
    def prestarlibro(self):
        self.__lprestado = True
    
    def devolverlibro(self):
        self.__lprestado = False
    
    def getcui(self):
        return self.__cui    
    def getlastname(self):
        return self.__last_name  
    def getfirstname(self):
        return self.__first_name
    def getprestado(self):
        return self.__lprestado
     
    def getdatos(self):
        return{
            "cui": self.__cui,
            "last_name": self.__last_name,
            "first_name": self.__first_name            
        }
    
    