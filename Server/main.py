from flask import Flask, request, send_file
import json
import os
import func as all_functions
from urllib.parse import unquote

SERVER_SYNC_PATH = all_functions.initialize()

app = Flask(__name__)


@app.route('/')
def main():
    return "<p>hello_world</p>"


@app.route('/api/send/<name>', methods=['GET', 'POST'])
def send(name):
    if request.method == "POST":
        global SERVER_SYNC_PATH
        data = request
        name = unquote(name)
        path = SERVER_SYNC_PATH + '//' + name
        with open(path, 'wb') as f:
            f.write(data.files['file'].read())
            f.close()
        return """Hello"""


@app.route('/api/download')
def download():
    global SERVER_SYNC_PATH
    data = json.loads(request.json)
    name = data['name']
    file = all_functions.find_file_by_name(name, SERVER_SYNC_PATH)
    return send_file(SERVER_SYNC_PATH + '/' + name)


@app.route('/api/get_hash')
def get_hash():
    global SERVER_SYNC_PATH
    data = json.loads(request.json)
    name = data['name']
    file_hash = all_functions.get_hash(name, SERVER_SYNC_PATH)
    return file_hash


@app.route('/api/get_time')
def get_modify_time():
    global SERVER_SYNC_PATH
    data = json.loads(request.json)
    name = data['name']
    file_time_modify = all_functions.get_local_time_modify(name, SERVER_SYNC_PATH)
    return str(file_time_modify)


@app.route('/api/get_size')
def get_file_size():
    global SERVER_SYNC_PATH
    data = json.loads(request.json)
    name = data['name']
    file_size = all_functions.get_local_size(name, SERVER_SYNC_PATH)
    return str(file_size)


@app.route('/api/get_all_files_name')
def get_files_name():
    global SERVER_SYNC_PATH
    data = "&AF*".join(all_functions.get_files_name(SERVER_SYNC_PATH))
    return str(data).encode()


@app.route('/api/delete_file')
def delete_file():
    global SERVER_SYNC_PATH
    data = json.loads(request.json)
    name = data["name"]
    flag = name in all_functions.get_files_name(SERVER_SYNC_PATH)
    all_functions.remove_file(name, SERVER_SYNC_PATH)
    return str(flag)
