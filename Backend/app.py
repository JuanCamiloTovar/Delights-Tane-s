from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pymysql
from flasgger import Swagger


app = Flask(__name__)
CORS(app)

def conectar(vhost, vuser, vpass, vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset='utf8mb4')
    return conn

@app.route("/", methods=["GET"])
def cesta():
    try:
        conn = conectar('localhost','root','290307','ejemplo_postres')
        cur = conn.cursor()
        cur.execute("SELECT * FROM postres WHERE id = 1")
        datos = cur.fetchone()
        cur.close()
        conn.close()
        
        if datos:
            dato = {
                'id': datos[0],
                'nombre': datos[1],
                'precio': datos[2],
                'descripcion': datos[3]
            }
            print(dato)
            return jsonify(dato)
        else: 
            return jsonify({'mensaje': 'Registro no encontrado'})
        
    except Exception as err:
        print(err)

if __name__ == '__main__':
    app.run(debug=True)