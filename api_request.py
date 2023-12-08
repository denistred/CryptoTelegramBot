import requests
from config import API_TOKEN


def get_cryptocurrency():
    # API ключ
    api_key = '491012c82def30cc37d92861f1dcf7f99b3f3ab4f2717cc59c33e508e49e'
    url = f'https://api.cryptorank.io/v1/currencies?api_key={api_key}&market_cap_min=50000000'

    # Отправка GET-запроса
    response = requests.get(url)
    count = 0

    raw_data = {}

    # Обработка ответа
    if response.status_code == 200:
        data = response.json()
        # Вывод списка имен криптовалют
        for coin in data['data']:
            try:
                # print(coin['name'], coin['values']['USD']['volume24h'])
                trade_volume_usd = coin['values']['USD']['volume24h']
                raw_data[coin['name']] = trade_volume_usd
            except TypeError:
                print("Ошибка обработки монеты: ", coin['name'])
    else:
        print("Ошибка:", response.status_code)

    print("Количество монет c ненулевым объемом торгов в USD:", count)
    print(type(raw_data))
    with open("data.txt", "w") as f:
        json.dump(raw_data, f)
    return raw_data





