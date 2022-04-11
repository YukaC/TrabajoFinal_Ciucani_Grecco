# Importamos la libreria Flask para crear la API
from re import A
from flask import Flask, jsonify, request
# Importamos la libreria HTTPStatus para poder usar los codigos de estado
from http import HTTPStatus
# Importar la libreria CORS para que se pueda hacer peticiones desde cualquier origen
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

with open('db.json', encoding='utf-8') as json_file:
    db = json.load(json_file)

@app.route('/')
def hello_world():
    return 'Allá te vamos netflix(?)'

@app.route('/peliculas', methods=['GET'])
def allfilms():
    peliculas = db['peliculas']
    generos = db['generos']
    directores = db['directores']
    respuesta = []
    for pelicula in peliculas:
        for genero in generos:
            if (pelicula['genero'] == genero['id']):
                pelicula['genero'] = genero['nombre']
            if (pelicula['genero2'] == genero['id']):
                pelicula['genero2'] = genero['nombre']
        for director in directores:
            if (pelicula['director'] == director['id']):
                pelicula['director'] = director['nombre']
            if (pelicula['director2'] == director['id']):
                pelicula['director2'] = director['nombre']
        respuesta.append(pelicula)
    return jsonify(respuesta)

@app.route('/ultimas-peliculas', methods=['GET'])
def last10():
        peliculas = db['peliculas'][-10:]
        generos = db['generos']
        directores = db['directores']
        respuesta = []
        for pelicula in peliculas:
            for genero in generos:
                if (pelicula['genero'] == genero['id']):
                    pelicula['genero'] = genero['nombre']
                if (pelicula['genero2'] == genero['id']):
                    pelicula['genero2'] = genero['nombre']
            for director in directores:
                if (pelicula['director'] == director['id']):
                    pelicula['director'] = director['nombre']
                if (pelicula['director2'] == director['id']):
                    pelicula['director2'] = director['nombre']
            respuesta.append(pelicula)
        return jsonify(respuesta)

@app.route('/peliculas/<id>', methods=['GET'])
def films_by_id(id):
        id = int(id)
        for pelicula in db['peliculas']:
            if pelicula['id'] == id:
                return jsonify(pelicula)
            

@app.route("/director/<id>", methods=['GET'])
def all_films_by_director(id):
    id = int(id)
    peliculas_by_dir = []
    for pelicula in db['peliculas']:
        if (pelicula['director'] == id or pelicula['director2'] == id):
            peliculas_by_dir.append(pelicula)
    return jsonify(peliculas_by_dir)


@app.route("/genero/<id>", methods=['GET'])
def all_films_by_gender(id):
    id = int(id)
    peliculas_by_gen = []
    for pelicula in db['peliculas']:
         if (pelicula['genero'] == id or pelicula['genero2'] == id):
            peliculas_by_gen.append(pelicula)
    return jsonify(peliculas_by_gen)
            
 
@app.route('/imagen', methods=['GET'])
def allfilmswithimage():
    filmswimg=[]
    for pelicula in db['peliculas']:
        try :
            f=open("./static/" + str( pelicula['id'])+'.jpg')
            filmswimg.append(pelicula)
            f.close()
        except FileNotFoundError:
            continue
            
    return jsonify(filmswimg)
    
@app.route("/directores", methods=['GET'])
def alldirectors():
    return jsonify(db['directores'])
    

@app.route("/generos", methods=['GET'])
def allgenders():
    return jsonify(db['generos'])

@app.route('/ult3', methods=['GET'])
def ult_3():
    return jsonify(db['peliculas'][-3:])

@app.route('/random', methods=['GET'])
def random_last_3():
    import random
    return jsonify(db['peliculas'][-3:][random.randint(0,2)])

@app.route('/peliculas/<id>/comentarios', methods=['GET'])
def comments_by_films(id):
    id = int(id)
    comentarios = db['comentarios']
    respuesta = []
    for comentario in comentarios:
            if (comentario['pelicula'] == id):              
                respuesta.append(comentario)
    return jsonify(respuesta)

@app.route('/login-user', methods=["POST"])
def login_user(): #devolver los datos del usuario
    data_user = request.form
    username = data_user.get('username')
    password = data_user.get('password')
    for user in db['usuarios']:
        if user['nombre'] == username and user['passw'] == password:
            return jsonify(HTTPStatus.OK)
    return jsonify( HTTPStatus.UNAUTHORIZED)

@app.route('/subir-pelicula', methods=["POST"])
def add_film():
    data_user = request.form
    
    nombre_pelicula = data_user.get('nombre_pelicula')
    sinopsis = data_user.get('sinopsis')
    genero = data_user.get('genero')
    genero2 = data_user.get('genero2')
    director = data_user.get('director')
    director2 = data_user.get('director2')
    duracion = data_user.get('duracion')
    year = data_user.get('year')
    score = data_user.get('score')
    
    for film in db['peliculas']:
        if film['nombre'] == nombre_pelicula:
            return jsonify(False), HTTPStatus.CONFLICT
        else :
            pelicula = {
                'id': len(db['peliculas']) + 1,
                'nombre': nombre_pelicula,
                'sinopsis': sinopsis,
                'genero': genero,
                'genero2': genero2,
                'director': director,
                'director2': director2,
                'duracion': duracion,
                'year': year,
                'score': score,
            }
            db['peliculas'].append(pelicula)
            return jsonify(db['peliculas']), HTTPStatus.OK
    
app.run()