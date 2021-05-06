import os
import json
from bson.json_util import dumps
import pymongo
import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    id = req.params.get('id')
    if not id:
        return func.HttpResponse("This HTTP triggered function executed successfully. Pass an id in the query string or in the request body for a proper response.", status_code=400)
    else:
        try:
            url = os.environ['mongodb-connstring']
            client = pymongo.MongoClient(url)
            database = client['lab2db']
            collection = database['notes']
            print(id)
            myquery = {'_id': id}

            result = collection.find(myquery)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf8', status_code=200)
        except:
            return func.HttpResponse("bad request", status_code=400)

    #if not id:
    #    try:
    #        req_body = req.get_json()
    #    except ValueError:
    #        pass
    #    else:
    #        id = req_body.get('id')
#
    #if name:
    #    return func.HttpResponse(result, mimetype="application/json", charset='utf8', status_code=200)
    #else:
    #    return func.HttpResponse(
    #         "This HTTP triggered function executed successfully. Pass an id in the query string or in the request body for a proper response.",
    #         status_code=400
    #    )
