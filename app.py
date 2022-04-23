from python.resources.recipe import UserRecipe
from flask import render_template

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api =  Api(app)

@app.route('/')
def index():
    return render_template('index.html')


api.add_resource(UserRecipe,'/api/v1/resources/ogrenciler/<string:username>')
