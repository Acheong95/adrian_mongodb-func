import os
import json
from bson.json_util import dumps
import pymongo
import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()
    if request:
        try:
            url = os.environ['mongodb-connstring']
            client = pymongo.MongoClient(url)

            database = client['lab2db']
            collection = database['notes']

            # replace the insert_one variable with what you think should be in the bracket
            collection.insert_one(request)

            # we are returnign the request body so you can take a look at the results
            return func.HttpResponse(req.get_body())
        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400
        )