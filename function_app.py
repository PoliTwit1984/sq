import azure.functions as func
import logging
import json 
import random

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="sq")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:

    with open('quotes.json') as f:
        quotes = json.load(f)
        
    # Select a random quote
    random_quote = random.choice(quotes)
    random_quote.pop('image', None)

    return func.HttpResponse(
        body=json.dumps(random_quote),
        mimetype="application/json"
    )
