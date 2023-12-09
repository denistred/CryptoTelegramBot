import json
from config import PERCENTAGE


def write_json(data, time_hours, time_mins):
    print(f"Создаём JSON файл под названием data{time_hours}-{time_mins}")
    with open(f'data{time_hours}-{time_mins}.txt', 'w') as out_file:
        json.dump(data, out_file, indent=4)
    print("JSON-файл создан!")


def volume_checker(time_hours, time_minutes, api_response):
    try:
        with open(f"data{time_hours}-{time_minutes}.txt", "r") as file:
            json_data = json.load(file)
    except:
        json_data = None
        print("Ошибка при чтении JSON файла")
    if json_data:
        result = {}
        for key in list(json_data.keys()):
            try:
                previous_volume = json_data[key]['volume24h']
                current_volume = api_response[key]['volume24h']
                if previous_volume > 0:
                    if ((current_volume / previous_volume) - 1) > (PERCENTAGE / 100):
                        result[key] = {"change": ((current_volume / previous_volume) - 1) * 100,
                                       "cap": api_response[key]['cap']}
            except Exception as e:
                print(f"Возникла ошибка на этапе проверки ключей :( \n{e}")
        return result
