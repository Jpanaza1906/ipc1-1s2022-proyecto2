from uuid import uuid4;

class Prestamo():
    def __init__(self, cui, isbn):
        self.__cui = cui
        self.__isbn = isbn
        self.__uuid = uuid4()
        
    def getcui(self):
        return self.__cui
    def getisbn(self):
        return self.__isbn
    def getuuid(self):
        return self.__uuid
    def getuuidjs(self):
        return{
            "uuid": self.__uuid
        }
    
    def getdatos(self):
        return{
            "cui": self.__cui,
            "isbn": self.__isbn,
            "uuid": self.__uuid
        }    
