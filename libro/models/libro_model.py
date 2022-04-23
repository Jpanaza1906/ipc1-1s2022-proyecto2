class Libro():
    def __init__(self, isbn, autores, ypubli, titulo, edicion, temas, descrip, ncopias, estanteria, fila):
        self.__isbn = isbn
        self.__autores = autores
        self.__ypubli = ypubli
        self.__titulo = titulo
        self.__edicion = edicion
        self.__temas = temas
        self.__descrip = descrip
        self.__ncopias = ncopias
        self.__estanteria = estanteria
        self.__fila = fila
        
    def agregarcopias(self, cantidad):
        if(cantidad>0):
            self.__ncopias += cantidad
        else:
            return{
                
            }
    def restarcopias(self):
        self.__ncopias = self.__ncopias - 1
    
    def getisbn(self):
        return self.__isbn
    def getautores(self):
        return self.__autores
    def getypubli(self):
        return self.__ypubli
    def gettitulo(self):
        return self.__titulo
    def getedicion(self):
        return self.__edicion
    def gettemas(self):
        return self.__temas
    def getdescrip(self):
        return self.__descrip
    def getncopias(self):
        return self.__ncopias
    def getestanteria(self):
        return self.__estanteria
    def getfila(self):
        return self.__fila        
    
    def getdatos(self):
        return{
            "isbn": self.__isbn,
            "autores": self.__autores,
            "ypubli": self.__ypubli,
            "titulo": self.__titulo,
            "edicion": self.__edicion,
            "temas": self.__temas,
            "descripcion": self.__descrip,
            "ncopias": self.__ncopias,
            "estanteria": self.__estanteria,
            "fila": self.__fila
        }