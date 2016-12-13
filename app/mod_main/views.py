from flask import Blueprint, render_template, request

from app import mongo
from bson import json_util,ObjectetID

from app import
mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
       db = mongo.db.arkep

   if request.method == 'GET':
       return "You request a document with the id:" +id
       
