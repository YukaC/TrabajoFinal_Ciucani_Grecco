# Importamos la libreria SqLite3 para poder acceder a la base de datos
from sqlite3 import Cursor
# Importamos la libreria Flask para crear la API
from flask import Flask, jsonify, request
# Importamos la libreria HTTPStatus para poder usar los codigos de estado
from http import HTTPStatus
# Importar la libreria CORS para que se pueda hacer peticiones desde cualquier origen
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
import pymysql

def conection():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='rootyuk',
                                db='pelisencasa',
                                #Utilizamos el cursorclass para que nos devuelva un cursor que sea de tipo dict (array asociativo)
                                cursorclass=pymysql.cursors.DictCursor)    

@app.route('/')
def hello_world():
    return 'Allá te vamos netflix(?)'

@app.route('/peliculas', methods=['GET'])
def allfilms():
    con = conection()
    cursor = con.cursor()
    cursor.execute("""
                   SELECT 
                    films.id,
                    films.name,
                    films.image,
                    films.score,
                    films.year,
                    d1.name AS d1_name,
                    d2.name AS d2_name,
                    g1.name AS g1_name,
                    g2.name AS g2_name
                    FROM films
                    LEFT JOIN directors d1 ON films.director_id_1 = d1.id
                    LEFT JOIN directors d2 ON films.director_id_2 = d2.id
                    LEFT JOIN genders g1 ON films.gender_id_1 = g1.id
                    LEFT JOIN genders g2 ON films.gender_id_2 = g2.id
                   """
                   )
    peliculas = cursor.fetchall()
    con.close()
    return jsonify(peliculas)

@app.route('/peliculas/<id>', methods=['GET'])
def filmbyid(id):
    con = conection()
    cursor = con.cursor()
    cursor.execute("SELECT films.id FROM films WHERE id = %s",(id))
    pelicula = cursor.fetchone()
    con.close()
    if pelicula:
        return jsonify(pelicula), HTTPStatus.OK
    else:
        return jsonify("Pelicula no encontrada D:"), HTTPStatus.NOT_FOUND 
    
@app.route("/director/<id>", methods=['GET'])
def allfilmsbydirector(id):
    con = conection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM films WHERE director_id = %s",(id))
    peliculas = cursor.fetchall()
    con.close()
    return jsonify(peliculas)

@app.route("/genero/<id>", methods=['GET'])
def allfilmsbygenre(id):
    con = conection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM films WHERE gender_id = %s",(id))
    peliculas = cursor.fetchall()
    con.close()
    return jsonify(peliculas)

@app.route('/ultimas-peliculas', methods=['GET'])
def ult10():
    con = conection()
    cursor = con.cursor()
    cursor.execute("SELECT name FROM films ORDER BY id ASC LIMIT 10")
    peliculas = cursor.fetchall()
    return jsonify(peliculas)

@app.route('/imagen', methods=['GET'])
def allfilmswithimage():
    con = conection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM films WHERE image IS NOT NULL")
    peliculas = Cursor.fetchall()
    con.close()
    return jsonify(peliculas)
    
@app.route("/directores", methods=['GET'])
def alldirectors():
    con = conection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM directors")
    directores = cursor.fetchall()
    con.close()
    return jsonify(directores)

@app.route("/generos", methods=['GET'])
def allgenders():
    con = conection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM genders")
    generos = cursor.fetchall()
    con.close()
    return jsonify(generos)


app.run()