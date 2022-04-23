class Database():
    def __init__(self):
        self.__cuiprestamista = []
        self.__isbnlibros = []
        self.__libros = []
        self.__prestamistas = []
        self.__prestamos = []

    # PRESTAMISTAS
    def agregarPrestamista(self, prestamista):
        if not(prestamista.getcui() in self.__cuiprestamista):
            self.__prestamistas.append(prestamista)
            self.__cuiprestamista.append(prestamista.getcui())
            print(self.__prestamistas)
            return True
        return False

    def obtenerPrestamista(self, cui):
        if int(cui) in self.__cuiprestamista:
            for prestam in self.__prestamistas:
                if(prestam.getcui() == int(cui)):
                    return prestam
        return None

    # LIBROS
    def agregarLibro(self, libro):
        if not(libro.getisbn() in self.__isbnlibros):
            self.__libros.append(libro)
            self.__isbnlibros.append(libro.getisbn())
            return True
        return False

    def obtenerLibro(self, isbn):
        if isbn in self.__libros:
            for lbs in self.__libros:
                if(lbs.getisbn() == isbn):
                    return lbs
        return None
    
    def modificarLibro(self, libro, copias): 
        libro.agregarcopias(copias)       
        contador = 0
        for lbs in self.__libros:
            if(lbs.getisbn() == libro.getisbn()):
                self.__libros.insert(contador,libro)
            contador = contador + 1    

    # PRESTAMOS

    def prestarLibro(self, prestamo):
        # verificar si el prestamista tiene prestado un libro
        cui = prestamo.getcui()        
        if int(cui) in self.__cuiprestamista:
            for prestam in self.__prestamistas:
                if(prestam.getcui() == int(cui)):
                    if(prestam.getprestado() == True):
                        return None  # no puede prestar libro

        # obtenemos isbn, y se le restan las copias
        contador = 0
        isbn = prestamo.getisbn()
        if isbn in self.__libros:
            for libross in self.__libros:
                if(libross.getisbn() == isbn):
                    libross.restarcopias()
                    self.__libros.insert(contador,libross)
                contador = contador + 1
        # Si el prestamista no tiene prestado un libro
        cont = 0
        if int(cui) in self.__cuiprestamista:
            for prestam in self.__prestamistas:
                if(prestam.getcui() == int(cui)):
                    prestam.prestarlibro()
                    self.__prestamistas.insert(cont,prestam)
                cont = cont + 1
                
        self.__prestamos.append(prestamo)
    
    def devolverLibro(self, cui, fecha):
        cont = 0
        if int(cui) in self.__cuiprestamista:
            for prestam in self.__prestamistas:
                if(prestam.getcui() == int(cui)):
                    prestam.devolverlibro()
                    self.__prestamistas.insert(cont,prestam)
                cont = cont + 1
        if int(cui) in self.__cuiprestamista:
            cont3 = 0
            for prestamo in self.__prestamos:
                if(prestamo.getcui() == int(cui) and prestamo.getfechadevuelt != 0):
                    isbn = prestamo.getisbn()
                    conti = 0
                    for libro in self.__libros:
                        if(libro.getisbn() == isbn):
                            libro.devolvercopia()
                            self.__libros.insert(conti, libro)
                        conti = conti + 1
                    prestamo.putfechadevuelto(fecha)
                    self.__prestamos.insert(cont3,prestamo)
                cont3 = cont3 + 1
                
    def consultarPrestamos(self, cui):
        prestamoscui = []
        for prestamo in self.__prestamos:
            if(prestamo.getcui() == cui):
                prestamoscui.append(prestamo)
        return prestamoscui
                    
                            
                    
        
