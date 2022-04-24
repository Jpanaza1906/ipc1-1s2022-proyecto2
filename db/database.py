from distutils.command.build_scripts import first_line_re


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
    
    def devolverLibro(self, uuid):
        #se obtiene el numero de cui que le pertenece al prestamo
        cui = "" 
        isbn = 0  
        conti = 0       
        for prestamo in self.__prestamos:
            if(str(prestamo.getuuid()) == uuid):
                if(prestamo.getdevuelto() == False):
                    cui = prestamo.getcui()
                    isbn = prestamo.getisbn()
                    self.__prestamos[conti].devolver()
                    break
                else:
                    return "ya"
            conti = conti + 1
                
        #Si no encontro ningun prestamos con ese id, el cui no va a tener nada, por lo que devuelve none
        if cui in self.__cuiprestamista:
            cont = 0
            for prestam in self.__prestamistas:
                if(prestam.getcui() == cui):
                    self.__prestamistas[cont].devolverlibro()
                    break
                cont = cont + 1
        else:
            return None
        # Ahora se realiza el algoritmo para devolver la copia
        if isbn in self.__isbnlibros:
            cont3 = 0
            for lbs in self.__libros:
                if(lbs.getisbn() == isbn):
                    self.__libros[cont3].devolvercopia()
                    break
                cont3 = cont3 + 1
        return True
                
    def consultarPrestamos(self, cui):
        if(cui in self.__cuiprestamista):
            first_name = ""
            last_name = ""
            for prestamista in self.__prestamistas:
                if(prestamista.getcui() == cui):
                    first_name = prestamista.getfirstname()
                    last_name = prestamista.getlastname()
            # Mostrar los prestramos        
            record = []
            for prestamo in  self.__prestamos:
                if(prestamo.getcui() == cui):
                    title = ""
                    isbn = prestamo.getisbn()
                    for lbs in self.__libros:
                        if(lbs.getisbn() == isbn):
                            title = lbs.gettitle()
                            break
                    record.append(prestamo.getdatos(title))
                    
            return {
                "cui" : cui,
                "first_name":first_name,
                "last_name": last_name,
                "record": record    
            }
        else:
            return None
        
lbDatabase = Database()
        
                    
                            
                    
        
