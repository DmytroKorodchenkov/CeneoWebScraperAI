from app import app
import os
from flask import render_template

@app.route('/')
def index():
    lis = []
    num = os.listdir('./opinions/')
    for i in range(len(num)):
        lis.append(num[i].split('.')[0])
    return render_template("index.html.jinja", dirs = lis)

@app.route('/new')
def new():
    name = "Dmytro Korodchenkov"
    field_of_study = "Applied Informatics"
    group_number = "ZZIAS1-1211"
    return render_template("new.html.jinja", name = name, field_of_study = field_of_study, group_number = group_number)
