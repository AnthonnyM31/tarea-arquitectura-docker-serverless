import json

def hello(event, context):
    # En Serverless, los parámetros vienen en el diccionario 'queryStringParameters'
    name = "Usuario"
    if event.get('queryStringParameters') and event['queryStringParameters'].get('name'):
        name = event['queryStringParameters']['name']

    body = {
        "message": f"Hola {name} desde Serverless"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }