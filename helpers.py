import json


def write_json(data, time_hours, time_mins):
    print("Создаём json файл")
    with open(f'data{time_hours}-{time_mins}.txt', 'w') as out_file:
        json.dump(data, out_file, sort_keys=True, indent=4)
    print("JSON-файл создан!")


def volume_checker(time_hours, time_minutes, api_response):
    with open(f"data{time_hours}-{time_minutes}.txt", "r") as file:
        json_data = json.load(file)
    result = {}
    for key in json_data.keys():
        try:
            previous_volume = json_data[key]['volume']
            current_volume = api_response[key]['volume']
        except:
            pass
        finally:
            if ((current_volume / previous_volume) - 1) > 0.5:
                result[key] = {"change": ((current_volume / previous_volume) - 1) * 100, "cap": api_response[key]['cap']}
    return result



