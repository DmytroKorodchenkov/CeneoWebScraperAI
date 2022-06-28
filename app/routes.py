from dataclasses import dataclass
from lib2to3.pgen2.grammar import opmap_raw
from pickle import TRUE
from unittest import expectedFailure
from numpy import product
from app import app
import os
import json
import pandas as pd
from flask import render_template, request, redirect, send_file
from app.utils.scraper import scraper
from app.utils.analyzer import analyzer
if not os.path.exists("opinions"):
    os.makedirs("opinions")

@app.route('/')
def index():
    return render_template("index.html.jinja")

@app.route('/extract', methods=['GET', 'POST'])
def extract():
    if request.method=='GET':
        products = [filename.split(".")[0] for filename in os.listdir("./opinions")]
        return render_template("extract.html.jinja")
    if request.method == 'POST':
        id = request.form['product_id']
        try:
            if int(id) and int(id) > 0:
                scraper(id)
                return redirect(f"http://www.ceneo.pl/{id}", code=302)
            else:
                data = "Enter a valid id."
                return render_template("extract.html.jinja", data=data)
        except:
            data = "Enter a valid id."
            return render_template("extract.html.jinja", data=data)

@app.route('/products')
def products():
    data = []
    for opinion in os.listdir('./opinions/'):
        if opinion.split('.')[1] == 'json':
            data.append(analyzer(opinion.split('.')[0]))
    return render_template("products.html.jinja", products=data)


@app.route('/author')
def author():
    return render_template("author.html.jinja")


@app.route("/products/getJSON/<product_id>")
def getJSON(product_id):
    f = f"../opinions/{product_id}.json"
    return send_file(f, as_attachment=True)


@app.route("/products/getCSV/<product_id>")
def getCSV(product_id):
    import pandas as pd
    with open(f"opinions/{product_id}.json", "r", encoding='utf-8') as f:
        data = pd.read_json(f)
        data.to_csv(f"opinions/{product_id}.csv", encoding='utf-8', index=True)
    return send_file(f"../opinions/{product_id}.csv", as_attachment=True)


@app.route("/products/getEXCEL/<product_id>")
def getEXCEL(product_id):
    import pandas as pd
    with open(f"opinions/{product_id}.json", "r", encoding="utf-8") as f:
        ed = pd.read_json(f)
        ed.to_excel(f"opinions/{product_id}.xlsx", encoding="utf-8", index=True)
    return send_file(f"../opinions/{product_id}.xlsx", as_attachment=True)
