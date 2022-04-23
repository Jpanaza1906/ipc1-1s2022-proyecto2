from uuid import uuid4;

class Prestamo():
    def __init__(self, cui, nombre, apellido, isbn, titulo, fechaprestamo, fechadevuelto):
        self.__uuid = uuid4()
        self.__cui = cui
        self.__nombre = nombre
        self.__apellido = apellido
        self.__isbn = isbn
        self.__titulo = titulo
        self.__fechaprestamo = fechaprestamo
        self.__fechadevuelto = fechadevuelto
    
    def getcui(self):
        return self.__cui
    def getnombre(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido
    def getisbn(self):
        return self.__isbn
    def gettitulo(self):
        return self.__titulo
    def getfechaprestamo(self):
        return self.__fechaprestamo
    def getfechadevuelto(self):
        return self.__fechadevuelto
    def putfechadevuelto(self, fecha):
        self.__fechadevuelto = fecha
    
    def getdatos(self):
        return{
            "uuid": self.__uuid,
            "cui": self.__cui,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "isbn": self.__isbn,
            "titulo": self.__titulo,
            "fechaprestamo": self.__fechaprestamo,
            "fechadevuelto": self.__fechadevuelto
        }    
