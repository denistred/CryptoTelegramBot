import requests
from config import API_TOKEN


def get_cryptocurrency():
    # API ключ
    api_key = API_TOKEN
    url = f'https://api.cryptorank.io/v1/currencies?api_key={api_key}&market_cap_min=50000000&limit=569'

    # Отправка GET-запроса
    response = requests.get(url)

    raw_data = {}

    # Обработка ответа
    if response.status_code == 200:
        data = response.json()
        # Вывод списка имен криптовалют
        for coin in data['data']:
            try:
                trade_volume_usd = coin['values']['USD']['volume24h']
                raw_data[coin['name']] = {"volume24h": trade_volume_usd, "cap": int(coin['values']['USD']['marketCap'])}
            except TypeError:
                print("Ошибка обработки монеты: ", coin['name'])
    else:
        print("Ошибка:", response.status_code)
    print("Получили JSON")
    print(raw_data)
    return raw_data
