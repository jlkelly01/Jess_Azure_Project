import azure.functions as func
import logging
import pandas as pd


app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", 
                  path="contjesstest/Read/{name}",
                  connection="mldatastoragedevuksouth_STORAGE") 
def blobTrigger1(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    



#@app.route(route="HttpTrigger", auth_level=func.AuthLevel.FUNCTION)
#def HttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
#    logging.info('Python HTTP trigger function processed a request.')
#
#    name = req.params.get('name')
#    if not name:
#        try:
#            req_body = req.get_json()
#        except ValueError:
#            pass
#        else:
#            name = req_body.get('name')
#
#    if name:
#        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#    else:
#        return func.HttpResponse(
#             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#             status_code=200
#        )