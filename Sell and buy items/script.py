import sqlite3
from flask import request
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/home")
def home():
    con = sqlite3.connect("sellBuyProj.db")
    cur = con.cursor()
    sqlQuery = "SELECT * FROM items LIMIT 20"
    allProducts = cur.execute(sqlQuery).fetchall()
    return allProducts


@app.route("/add", methods=['POST'])
def addItem():
    name = request.form.getlist('name')[0]
    desc = request.form.getlist('desc')[0]

    con = sqlite3.connect("sellBuyProj.db")
    cur = con.cursor()
    sqlQuery = "INSERT INTO items ('name', 'desc') VALUES ('" + name + "', '" + desc + "')"
    cur.execute(sqlQuery)
    con.commit()

    return "success"

@app.route("/update/<id>", methods=['POST'])
def update(id):
    name = request.form.getlist('name')[0]
    desc = request.form.getlist('desc')[0]

    con = sqlite3.connect("sellBuyProj.db")
    cur = con.cursor()
    sqlQuery = "UPDATE items SET name='" + name + "', desc='" + desc + "' WHERE itemid=" + str(id)
    cur.execute(sqlQuery)
    con.commit()

    return "success"

@app.route("/view/<id>")
def viewItem(id):
    con = sqlite3.connect("sellBuyProj.db")
    cur = con.cursor()
    sqlQuery = "SELECT * FROM items i WHERE i.itemid=" + str(id)
    viewSelectedItem = cur.execute(sqlQuery).fetchall()
    
    return viewSelectedItem

@app.route("/delete/<id>")
def deleteItem(id):
    con = sqlite3.connect("sellBuyProj.db")
    cur = con.cursor()
    sqlQuery = "DELETE FROM items WHERE itemid=" + str(id)
    cur.execute(sqlQuery)
    con.commit()
    
    return "success"

