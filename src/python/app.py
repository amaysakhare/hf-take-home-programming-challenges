# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/test'

mongo = PyMongo(app)

#api to list the ingredients of given recipe
@app.route('/ingredients/<string:recipename>', methods=['GET'])
def get_all_ingredients(recipename):

  collection = mongo.db.wmenu

  s = collection.find_one_or_404({"recipe.name":recipename})
  i = s["recipe"]["ingredients"]


  return jsonify(i)

#api to delete the given recipe
@app.route('/deleteRecipe/<string:recipename>', methods=['DELETE'])
def delete_recipe(recipename):

  collection = mongo.db.wmenu

  s = collection.delete_one({'_id': recipename})

  return dumps(s.deleted_count)


#api to create a recipe

@app.route('/recipe', methods=['POST'])
def post_recipe():

  collection = mongo.db.wmenu
  id = request.json['_id']
  name = request.json['recipe']['name']
  instr = request.json['recipe']['instr']
  s = collection.insert({'_id': id, 'recipe':{'name': name, 'instr':instr}})

  return jsonify(s)

#api to read a recipe

@app.route('/recipe/<string:recipename>', methods=['GET'])
def get_recipe(recipename):

  collection = mongo.db.wmenu

  s = collection.find_one_or_404({"recipe.name":recipename})

  return jsonify(s["recipe"])

#api to update a recipe

@app.route('/updateRecipe/<string:recipename>', methods=['PUT'])
def update_recipe(recipename):

  collection = mongo.db.wmenu
  s = collection.find_one_or_404({"recipe.name": recipename})
  newval = (s['recipe']['instr'])
  newval:"hello new text"
  u = collection.update_one(s,newval)

  return dumps(s.modified_count)


