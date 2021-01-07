from compra_estado import app

from flask import render_template, request, url_for

import sqlite3

@app.route('/')
def tabla_incio():
    return render_template("incio.html")

@app.route('/purchase')
def interaccion():
    return render_template ("purchase.html")

@app.route('/status')  
def estado():
    return render_template("status.html")