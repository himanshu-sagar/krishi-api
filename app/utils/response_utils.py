import flask
from flask import json

def jsonify_and_cors(data, status_code=200):
    response = flask.jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status_code = status_code
    return response

def throw_error(error="Something went wrong", status=500, message=None):
    return jsonify_and_cors({"error": {"error": error, "statusCode": status, "message": message}}, status_code=status)

def throw_response(message):
    message = json.loads(json.dumps(message))
    return jsonify_and_cors({"data": message}, status_code=200)
