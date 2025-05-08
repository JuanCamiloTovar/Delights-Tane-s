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
        return render_template("cesta.html")
        
    except Exception as err:
        print(err)

if __name__ == '__main__':
    app.run(debug=True)