from compra_estado import app

from flask import render_template, request, url_for

import sqlite3

@app.route('/')
def tabla_incio():
    return render_template("incio.html")