import os
import json
from bson.json_util import dumps
import pymongo
import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python getposts trigger function.')
    try:
        url = os.environ['mongodb_connstring']
        client = pymongo.MongoClient(url)
        database = client['lab2db']
        collection = database['notes']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf8', status_code=200)
    except:
        return func.HttpResponse("bad request", status_code=400)
