import json
from flask import Blueprint, jsonify, request
from db.database import lbDatabase
from libro.models.libro_model import Libro

libro = Blueprint('libro', __name__, url_prefix="/book")

#------------------------------------------------------------------------

@libro.route('', methods = ['POST'])
def crear():
    body = request.get_json()
    try:
        if("isbn" in body and "author" in body and "title" in body and "year" in body and "no_copies" in body and "no_available_copies" in body):
            if(body["isbn"] != "" and body["author"] != "" and body["title"] != "" and body["year"] != ""):          
                if(body["no_copies"] > 0 and body["no_available_copies"] > 0 ):
                    if(body["year"] > 0 and body["year"] < 2023):
                        libro = Libro(int(body["isbn"]),body["author"],body["title"],int(body["year"]),int(body["no_copies"]),int(body["no_available_copies"]))
                        if(lbDatabase.agregarLibro(libro)):
                            return{'msg': "Libro creado existosamente"}, 201 #Created
                        else:
                            return{'msg': 'ISBN ya se encuentra registrado.'}, 406 #Not acceptable
                    else:
                        return{'msg': 'La fecha no se encuentra en los rangos válidos'}, 406 #Not acceptable
                else:
                    return{'msg': 'Existe un error en el número de copias'}, 406 #Not acceptable
            else:
                return{'msg': 'El contenido de los campos no es válido'}, 400 #bad request
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500 #Internal server error

@libro.route('', methods = ['PUT'])
def modificar():
    body = request.get_json()
    try:
        if("isbn" in body and "author" in body and "title" in body and "year" in body):
            if(body["isbn"] != "" and body["author"] != "" and body["title"] != "" and body["year"] != ""):
                if(body["year"] > 0 and body["year"] < 2023):
                    if(lbDatabase.modificarLibro(body["isbn"],body["author"],body["title"],body["year"])):
                        return{'msg': "Libro modificado existosamente"}, 200 # ok
                    else:
                        return{'msg': "El isbn del libro no fue encontrado"}, 404 #not found
                else:
                        return{'msg': 'La fecha no se encuentra en los rangos válidos'}, 406 #not acceptable
            else:
                return{'msg': 'El contenido de los campos no es válido'}, 400 #bad request
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},400 #bad request
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500 #internal server error

@libro.route('', methods = ['GET'])
def buscar():
    title = request.args.get('title')
    year_from = request.args.get('year_from')
    year_to = request.args.get('year_to')
    author = request.args.get('author')
    
    try:
        if(title != None):
            librot = lbDatabase.obtenerLibrotitulo(title)
            return jsonify(librot), 200 #ok
        elif(author != None):
            librot = lbDatabase.obtenerLibroautor(author)
            return jsonify(librot), 200 #ok
        elif(year_from != None and year_to != None):
            if(int(year_from) > 0 and int(year_to) > 0):
                if(int(year_from) < int(year_to)):
                    librot = lbDatabase.obtenerLibrofechas(int(year_from), int(year_to))
                    return jsonify(librot), 200 #ok
                else:
                    return{'msg': 'La fecha final no puede ser menor a la inicial'},400 #bad request
            else:
                return{'msg': 'Las fechas deben tener valores lógicos'},400 #bad request
        elif(title == None and author == None and year_from == None and year_to == None):
            listalb = lbDatabase.obtenerLibros()
            return jsonify(listalb),200 #ok
        else:
            librot = []
            return jsonify(librot), 200 #ok  
            
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500 #internal server error
    
