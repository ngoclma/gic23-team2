import csv
import json
import requests
from flask import make_response
from bson import json_util
from bson.objectid import ObjectId
from response import make_json_response
import pandas as pd

from database import db
collection2 = db.positions

def get_all(collection):
    cursor = collection.find()
    return make_json_response(json_util.dumps(cursor), 200)


def get_by_id(id, instrument_id, collection):
    cursor = collection.find_one({"_id": ObjectId(id), "instrument_id": instrument_id})
    return make_json_response(json_util.dumps(cursor), 200)

def unsupported_method():
    return make_json_response("Request type not supported", 400)