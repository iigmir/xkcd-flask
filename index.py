from flask import Flask, render_template, jsonify, request
import requests
import re

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
    # Varaibles
    # Python has issues about objects:
    # "TypeError: Object of type method is not JSON serializable" is you add the by a object.
    if id is None:
        id_api = ""
        explain = "https://www.explainxkcd.com"
        tw = "https://xkcd.tw"
    else:
        id_api = id + "/"
        explain = "https://www.explainxkcd.com/wiki/index.php/" + id
        tw = "https://xkcd.tw/" + id
    # Request
    url = "https://xkcd.com/" + id_api + "info.0.json"
    response = requests.get( url )
    if response.status_code == 404:
        response = requests.get( "https://xkcd.com/info.0.json" )
    return jsonify({
        "response": response.json(),
        "id": id,
        "request_url": url,
        "explain": explain,
        "tw": tw
    })