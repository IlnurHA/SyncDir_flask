from engine import engine
import time

items_api = []
GB = 34359738368


def func(file_path, file_path_lan):
    global GB
    items = engine.get_files(file_path)
    items_lan = engine.get_files_lan(file_path_lan)

    items_name = [item for item in items]
    for item in items:
        if item not in items_lan and item:
            if item in items_api and engine.get_item_size(item) < GB:
                print(f"Удаление файла {item} на облаке")
                engine.remove_file(file_path, item)
                print(f"Файл {item} удалён")
                items_api.pop(items_api.index(item))
                items = engine.get_files(file_path)
                break
            elif engine.get_item_size(item) < GB:
                print("Загрузка файла:", item)
                engine.get_file(item, file_path, file_path_lan)
                print(f'Файл {item} загружен')
                items_api.append(item)
                items_lan.append(item)
        for item_lan in items_lan:
            if not item == item_lan:
                if item_lan not in items_name and engine.get_local_size(file_path_lan, item_lan) < GB:
                    if item_lan in items_api:
                        print(f"Удаление файла {item_lan} на устройстве")
                        engine.remove_local_file(file_path_lan, item_lan)
                        print(f"Файл {item_lan} удалён")
                        items_api.pop(items_api.index(item_lan))
                        items_lan.pop(items_lan.index(item_lan))
                        break
                    elif engine.get_local_size(file_path_lan, item_lan) < GB:
                        print(f"Отправление файла: {item_lan}")
                        engine.send_file(item_lan, file_path, file_path_lan)
                        print(f'Файл {item_lan} отправлен')
                        items_name.append(item_lan)
                        items_api.append(item_lan)
                continue
            if item and not engine.get_hash(item) == engine.get_local_hash(file_path_lan, item_lan):
                if engine.get_time_modify(item) >= engine.get_local_time_modify(file_path_lan, item_lan):
                    print("Загрузка файла:", item)
                    engine.get_file(item, file_path, file_path_lan)
                    print(f'Файл {item} загружен')
                    if item not in items_api:
                        items_api.append(item)
                elif engine.get_time_modify(item) <= engine.get_local_time_modify(file_path_lan, item_lan):
                    print(f"Отправление файла: {item}")
                    engine.send_file(item, file_path, file_path_lan)
                    print(f'Файл {item} отправлен')
                    if item not in items_api:
                        items_api.append(item)
                else:
                    raise TimeoutError("Hash разный, а время одинаковое")
            else:
                if item not in items_api:
                    items_api.append(item)
