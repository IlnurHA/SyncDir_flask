import requests
import json
from urllib.parse import quote


def get_api_url():
    try:
        with open("api_url") as f:
            data = f.read().strip()
            f.close()
            return data
    except (FileExistsError, FileNotFoundError):
        api_url = input("Введите api_url")
        with open("api_url", "w") as f:
            f.write(api_url)
            f.close()
        return api_url


def find_file_by_name(name, path):
    try:
        f = open(path + '//' + name, 'rb')
        data = f.read()
        f.close()
        return data
    except (FileNotFoundError, FileExistsError):
        raise FileNotFoundError(f"Not found file name: {name}")


def send_file(name: str, path):
    api_url = get_api_url()
    file = find_file_by_name(name, path)
    print(name)
    requests.post(api_url + f'/api/send/{quote(name)}', files={'file': file})


def download_file(name, path):
    api_url = get_api_url()
    data = requests.get(api_url + '/api/download', json=json.dumps({"name": name})).content
    f = open(path + "//" + name, "wb")
    f.write(data)
    f.close()


def get_hash(name):
    api_url = get_api_url()
    data = requests.get(api_url + '/api/get_hash', json=json.dumps({"name": name})).content
    return data


def get_time(name):
    api_url = get_api_url()
    data = requests.get(api_url + '/api/get_time', json=json.dumps({"name": name})).content
    return int(data)


def get_size(name):
    api_url = get_api_url()
    data = requests.get(api_url + '/api/get_size', json=json.dumps({"name": name})).content
    return int(data)


def get_all_files_name():
    api_url = get_api_url()
    items = requests.get(api_url + '/api/get_all_files_name').content.decode().split("&AF*")
    return items


def remove_file_on_cloud(name):
    api_url = get_api_url()
    return requests.get(api_url + '/api/delete_file', json=json.dumps({"name": name}))
