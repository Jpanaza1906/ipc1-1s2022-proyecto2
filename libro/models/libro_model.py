class Libro():
    def __init__(self, isbn, author, title, year, no_copies, no_available_copies):
        self.__isbn = isbn
        self.__author = author        
        self.__title = title
        self.__year = year    
        self.__no_copies = no_copies
        self.__no_available_copies = no_available_copies        

    def restarcopias(self):
        self.__no_available_copies = self.__no_available_copies - 1
    def devolvercopia(self):
        self.__no_available_copies = self.__no_available_copies + 1
    
    def getisbn(self):
        return self.__isbn
    def getauthor(self):
        return self.__author
    def gettitle(self):
        return self.__title
    def getyear(self):
        return self.__year      
    def getnocopies(self):
        return self.__no_copies
    def getnoavailablecopies(self):
        return self.__no_available_copies  
    
    def setauthor(self, author):
        self.__author = author
    def settitle(self, title):
        self.__title = title
    def setyear(self, year):
        self.__year = year
    
    def getdata(self):
        return{
            "isbn": self.__isbn,
            "author": self.__author,
            "title": self.__title,
            "year": self.__year,
            "no_copies": self.__no_copies,
            "no_available_copies": self.__no_available_copies
        }