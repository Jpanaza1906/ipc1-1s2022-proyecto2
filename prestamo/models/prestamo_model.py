from uuid import uuid4;
import datetime
class Prestamo():
    def __init__(self, cui, isbn, devuelto):
        self.__cui = cui
        self.__isbn = isbn
        self.__uuid = uuid4()
        self.__devuelto = devuelto 
        self.__lend_date = datetime.date.today()
        self.__return_date = "NA"     
    
    def devolver(self):
        self.__devuelto = True
        self.__return_date = datetime.date.today()
    def getcui(self):
        return self.__cui
    def getisbn(self):
        return self.__isbn
    def getuuid(self):
        return self.__uuid
    def getdevuelto(self):
        return self.__devuelto
    def getreturndate(self):
        return self.__return_date
    def getlenddate(self):
        return self.__lend_date
    def getuuidjs(self):
        return{
            "uuid": self.__uuid
        }
    
    def getdatos(self, title):
        return{
            "uuid": self.__uuid,
            "isbn": self.__isbn,
            "title": title,
            "lend_date": str(self.__lend_date),
            "return_date": str(self.__return_date)
        }    
