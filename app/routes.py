from array import array
from click import open_file
from app import app
import os
from flask import render_template, request
from utils.scraper import scraper
if not os.path.exists("opinions"):
    os.makedirs("opinions")

@app.route('/')
def index():
    return render_template("index.html.jinja")

@app.route('/extract')
def extract():
    return render_template("extract.html.jinja")

@app.route('/products')
def products():
    return render_template("products.html.jinja")

@app.route('/author')
def author():
    name = "1"
    field = "2"
    univ = "3"
    return render_template("author.html.jinja", name=name, field=field, univ=univ)