import os
import hashlib


def find_file_by_name(name, path):
    try:
        f = open(path + '//' + name, 'rb')
        data = f.read()
        f.close()
        return data
    except (FileNotFoundError, FileExistsError):
        return bytes("")


def get_hash(name, path):
    return hashlib.sha256(open(os.path.join(path, name), 'rb').read()).hexdigest()


def get_local_time_modify(name, path):
    return int(os.path.getmtime(os.path.join(path, name)))


def get_local_size(name, path):
    file_stats = os.stat(os.path.join(path, name))
    return file_stats.st_size


def get_files_name(path):
    return os.listdir(path=path)


def remove_file(name, path):
    return os.remove(os.path.join(path, name))

def initialize():
    try:
        with open("paths.txt") as f:
            file_path_lan = f.readlines()[0]
            f.close()
        return file_path_lan.strip()
    except (FileExistsError, FileNotFoundError, ValueError):
        with open("paths.txt", 'w') as f:
            file_path_lan = input("Input local file path for sync: \n")
            f.write(file_path_lan)
            return file_path_lan