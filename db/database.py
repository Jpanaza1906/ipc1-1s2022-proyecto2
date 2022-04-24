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
            return True
        return False

    def obtenerPrestamista(self, cui):
        if cui in self.__cuiprestamista:
            for prestam in self.__prestamistas:
                if(prestam.getcui() == cui):
                    return prestam
        return None

    # LIBROS
    def agregarLibro(self, libro):
        if not(libro.getisbn() in self.__isbnlibros):
            self.__libros.append(libro)
            self.__isbnlibros.append(libro.getisbn())
            return True
        return False

    def obtenerLibros(self):
        librosf = []
        for lbs in self.__libros:
            librosf.append(lbs.getdata())
        return librosf
    
    def obtenerLibrotitulo(self, title):
        librosf = []
        for lbs in self.__libros:
            if(lbs.gettitle() == title):
                librosf.append(lbs.getdata())
        return librosf
    def obtenerLibroautor(self, author):
        librosf = []
        for lbs in self.__libros:
            if(lbs.getauthor() == author):
                librosf.append(lbs.getdata())
        return librosf
    def obtenerLibrofechas(self, fechaini, fechafin):
        librosf = []
        for lbs in self.__libros:
            if(lbs.getyear() > fechaini and lbs.getyear() < fechafin):
                librosf.append(lbs.getdata())
        return librosf
    
    def modificarLibro(self, isbn, author, title, year):
        contador = 0
        if int(isbn) in self.__isbnlibros:
            for lbs in self.__libros:
                if(lbs.getisbn() == isbn):
                    self.__libros[contador].setauthor(author)
                    self.__libros[contador].settitle(title)
                    self.__libros[contador].setyear(year)
                    return True                    
                contador = contador + 1
        return False

    # PRESTAMOS

    def prestarLibro(self, prestamo):
        # verificar si el prestamista tiene prestado un libro
        cui = prestamo.getcui()        
        if cui in self.__cuiprestamista:
            for prestam in self.__prestamistas:
                if(prestam.getcui() == cui):
                    if(prestam.getprestado() == True):
                        return None  # no puede prestar libro
        else:
            return "i"

        # obtenemos isbn, y se le restan las copias
        contador = 0
        isbn = prestamo.getisbn()
        if isbn in self.__isbnlibros: #
            for libross in self.__libros:
                if(libross.getisbn() == isbn):
                    self.__libros[contador].restarcopias()
                contador = contador + 1
        else:
            return "e"
        # Si el prestamista no tiene prestado un libro
        cont = 0
        if cui in self.__cuiprestamista:
            for prestam in self.__prestamistas:
                if(prestam.getcui() == cui):
                    self.__prestamistas[cont].prestarlibro()
                cont = cont + 1
                
        self.__prestamos.append(prestamo)
        return prestamo.getuuidjs()
    
    def devolverLibro(self, cui, fecha):
        cont = 0
        if cui in self.__cuiprestamista:
            for prestam in self.__prestamistas:
                if(prestam.getcui() == cui):
                    prestam.devolverlibro()
                    self.__prestamistas.insert(cont,prestam)
                cont = cont + 1
        if cui in self.__cuiprestamista:
            cont3 = 0
            for prestamo in self.__prestamos:
                if(prestamo.getcui() == cui and prestamo.getfechadevuelt != 0):
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
        return True
                
    def consultarPrestamos(self, cui):
        prestamoscui = []
        for prestamo in self.__prestamos:
            if(prestamo.getcui() == cui):
                prestamoscui.append(prestamo)
                return prestamoscui
        return None
        
lbDatabase = Database()
        
                    
                            
                    
        
