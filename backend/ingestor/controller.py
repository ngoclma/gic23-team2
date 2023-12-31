from .services import *
from flask import Blueprint, request
from database import db
from response import unsupported_method

ingestor_blueprint = Blueprint("ingest", __name__)
instrumentsCollection = db.instruments
priceCollection = db.price
positionsCollection = db.positions

# @ingestor_blueprint.route("/insertFromCsv", methods=["POST"])
# def insertFromFilePD():
#     if request.method == "POST":
#         return insert_from_file_pd(request, instrumentsCollection, positionsCollection)
#     else:
#         return unsupported_method()

@ingestor_blueprint.route("/insertFromApi", methods=["POST"])
def insertFromApi():
    if request.method == "POST":
        return insert_from_api(request, collection)
    else:
        return unsupported_method()

@ingestor_blueprint.route("/insertFromDb", methods=["POST"])
def insertFromDb():
    if request.method == "POST":
        relative_path = "../inputs_db/master-reference.db"
        file_path = os.path.join(os.path.dirname(__file__), relative_path)
        return insert_from_db(file_path, instrumentsCollection, priceCollection)
    else:
        return unsupported_method()

@ingestor_blueprint.route("/insertFromCsv", methods=["POST"])
def readFromCSV():
    if request.method == "POST":
        return csv_to_db(positionsCollection)
    else:
        return unsupported_method()
