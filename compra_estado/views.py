from compra_estado import app

from flask import render_template, request, url_for

import sqlite3

from requests import Request, Session

from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import json


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
'start':'1',
'limit':'5000',
'convert':'USD'
}
headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': 'f4306891-4e3c-4072-98d0-3a649dd0c2f4',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

@app.route('/')
def tabla_incio():

    return render_template("incio.html")

@app.route('/purchase', methods=['GET','POST'])
def interaccion():

    return render_template ("purchase.html")

@app.route('/status')  
def estado():
    return render_template("status.html")