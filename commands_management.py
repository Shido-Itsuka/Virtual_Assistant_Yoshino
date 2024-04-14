import json

# Путь к JSON-файлу
JSON_PATH = "commands.json"


def create_record(command_type, command_name, command_string, voice_request):
    """
  Создает новую запись в JSON-файле.

  Args:
    command_type: Тип команды (например, "exec").
    command_name: Название команды.
    command_string: Строка команды.
    voice_request: Голосовой запрос
  """
    with open(JSON_PATH, 'r+') as f:
        data = json.load(f)
        max_id = 0
        for record in data:
            # print('data->', data)
            # print('\nrecord->', record)
            # print('-' * 20)
            if int(record) > max_id:
                max_id = int(record)
        # Автоматическое создание нового ID
        new_id = max_id + 1
        data[str(new_id)] = {  # Преобразовать new_id в строку
            "id": new_id,
            "command_type": command_type,
            "command_name": command_name,
            "command_string": command_string,
            "voice_request": voice_request
        }
        f.seek(0)
        json.dump(data, f, indent=4)


def read_records():
    """
  Читает все записи из JSON-файла.

  Returns:
    Список записей в виде словарей.
  """
    with open(JSON_PATH, 'r') as f:
        return json.load(f)


def update_record(id, command_type, command_name, command_string, voice_request):
    """
  Обновляет существующую запись в JSON-файле.

  Args:
    id: Идентификатор записи.
    command_type: Новый тип команды.
    command_name: Новое название команды.
    command_string: Новая строка команды.
    voice_request: Голосовой запрос
  """
    with open(JSON_PATH, 'r+') as f:
        data = json.load(f)
        for i, record in enumerate(data):
            if record["id"] == id:
                data[str(id)] = {  # Преобразовать id в строку
                    "id": id,
                    "command_type": command_type,
                    "command_name": command_name,
                    "command_string": command_string,
                    "voice_request": voice_request
                }
                break
        f.seek(0)
        json.dump(data, f, indent=4)


def delete_record(id):
    """
  Удаляет запись из JSON-файла по идентификатору.

  Args:
    id: Идентификатор записи.
  """
    with open(JSON_PATH, 'r+') as f:
        data = json.load(f)
        for i, record in enumerate(data):
            if record["id"] == id:
                del data[str(id)]  # Преобразовать id в строку
                break
        f.seek(0)
        json.dump(data, f, indent=4)


print(read_records())

