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
                            return{'msg': "Libro creado existosamente"}, 200
                        else:
                            return{'msg': 'ISBN ya se encuentra registrado.'}, 404
                    else:
                        return{'msg': 'La fecha no se encuentra en los rangos válidos'}, 404
                else:
                    return{'msg': 'Existe un error en el número de copias'}, 404
            else:
                return{'msg': 'El contenido de los campos no es válido'}, 404
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},404
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500

@libro.route('', methods = ['PUT'])
def modificar():
    body = request.get_json()
    try:
        if("isbn" in body and "author" in body and "title" in body and "year" in body):
            if(body["isbn"] != "" and body["author"] != "" and body["title"] != "" and body["year"] != ""):
                if(body["year"] > 0 and body["year"] < 2023):
                    if(lbDatabase.modificarLibro(body["isbn"],body["author"],body["title"],body["year"])):
                        return{'msg': "Libro modificado existosamente"}, 200
                    else:
                        return{'msg': "El isbn del libro no fue encontrado"}, 404
                else:
                        return{'msg': 'La fecha no se encuentra en los rangos válidos'}, 404
            else:
                return{'msg': 'El contenido de los campos no es válido'}, 404
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'},404
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500

@libro.route('', methods = ['GET'])
def buscar():
    title = request.args.get('title')
    year_from = request.args.get('year_from')
    year_to = request.args.get('year_to')
    author = request.args.get('author')
    
    try:
        if(title != None):
            librot = lbDatabase.obtenerLibrotitulo(title)
            return jsonify(librot), 200
        elif(author != None):
            librot = lbDatabase.obtenerLibroautor(author)
            return jsonify(librot), 200
        elif(year_from != None and year_to != None):
            if(int(year_from) > 0 and int(year_to) > 0):
                if(int(year_from) < int(year_to)):
                    librot = lbDatabase.obtenerLibrofechas(int(year_from), int(year_to))
                    return jsonify(librot), 200
                else:
                    return{'msg': 'La fecha final no puede ser menor a la inicial'},404
            else:
                return{'msg': 'Las fechas deben tener valores lógicos'},404
        elif(title == None and author == None and year_from == None and year_to == None):
            listalb = lbDatabase.obtenerLibros()
            return jsonify(listalb),200
        else:
            librot = []
            return jsonify(librot), 200     
            
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500
    
