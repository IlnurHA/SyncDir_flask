import os
import hashlib
import datetime
import engine.req_client as req


def send_file(file, path, path_lan):
    req.send_file(file, path_lan)


def get_file(file, path, path_lan):
    req.download_file(file, path_lan)


def get_files(path):
    files = req.get_all_files_name()
    return files


def create_dir(path, api):
    return api.mkdir(path)


def check_dir_exist(path, api):
    return api.exists(path)


def get_files_lan(path):
    return os.listdir(path=path)


def get_local_hash(file_path, item):
    return hashlib.sha256(open(os.path.join(file_path, item), 'rb').read()).hexdigest()


def get_local_time_modify(file_path, item):
    data = int(os.path.getmtime(os.path.join(file_path, item)))
    return int(os.path.getmtime(os.path.join(file_path, item)))


def get_hash(item):
    return req.get_hash(item).decode()


def get_item_size(item):
    return req.get_size(item)


def get_time_modify(item):
    return req.get_time(item)


def remove_file(path, file):
    return req.remove_file_on_cloud(file)


def remove_local_file(path, item):
    return os.remove(os.path.join(path, item))


def get_local_size(path, item):
    file_stats = os.stat(os.path.join(path, item))
    return file_stats.st_size
