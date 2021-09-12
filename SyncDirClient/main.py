import api
import time


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


def main():
    lfp = initialize()
    print("Initialized")
    while True:
        api.func("", lfp)
        time.sleep(10)


if __name__ == '__main__':
    main()
