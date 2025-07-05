from flask import Flask, request, render_template
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

def conectar(vhost, vuser, vpass, vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass,db=vdb,charset='utf8mb4')
    return conn

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/postres")
def postres():
    return render_template("postres.html")

@app.route("/cesta", methods=["GET"])
def cesta():
    cantidad=0
    productos=0
    total=0
    
    conn = conectar('localhost','root','290307','ejemplo_postres')
    cur = conn.cursor()
    cur.execute("SELECT * FROM postres WHERE id = 1")
    postres = cur.fetchone()
    cur.close()
    conn.close()
    
    if postres:
        postre = {
            'id': postres[0],
            'nombre': postres[1],
            'precio': postres[2],
            'descripcion': postres[3]
        }
        if request.args:
            cantidad = int(request.args['contador'])
            productos = cantidad*int(postre['precio'])
            total = productos+5000
            
    return render_template("cesta.html", cantidad=cantidad, productos=productos, total=total ,postre=postre)

@app.route("/info_napoleon")
def info_napoleon():
    return render_template("info_napoleon.html")

if __name__ == '__main__':
    app.run(debug=True)