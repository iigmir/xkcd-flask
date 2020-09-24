from flask import Flask, render_template, jsonify, request
import requests
import re
import APIModule

app = Flask(__name__)

@app.route("/")
def hello_world():
    is_json_request = re.search("json", request.headers.get("Accept"))
    if is_json_request:
        return get_tasks()
    else:
        return render_template("f2e.html")

@app.route("/api", methods=["GET"])
@app.route("/api/<id>", methods=["GET"])
def get_tasks(id=None):
    response = requests.get( APIModule.original_url(id) )
    if response.status_code == 404:
        response = requests.get( "https://xkcd.com/info.0.json" )
    return jsonify({
        "response": response.json(),
        "id": id,
        "request_url": APIModule.original_url(id),
        "explain": APIModule.explain(id),
        "tw": APIModule.tw(id)
    })