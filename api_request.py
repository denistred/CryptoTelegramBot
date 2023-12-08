import requests
from config import API_TOKEN


def get_cryptocurrency():
    # API ключ
    api_key = API_TOKEN
    url = f'https://api.cryptorank.io/v0/coins?api_key={api_key}'

    # Отправка GET-запроса
    response = requests.get(url)
    count = 0

    raw_data = {}

    # Обработка ответа
    if response.status_code == 200:
        print("Начинаем обработку запроса")
        data = response.json()
        # Вывод списка имен криптовалют
        for coin in data['data']:
            try:
                if coin['volume24h'] != 0 and coin['isTraded'] == True and coin['marketCap'] != None:
                    # Предполагаем, что поле price содержит цену в USD
                    trade_volume_usd_str = str(coin['volume24h'] * coin['price']['USD']).split(".")
                    if len(trade_volume_usd_str[0]) <= 3:
                        trade_volume_usd = coin['volume24h'] * coin['price']['USD']
                    else:
                        trade_volume_usd = coin['volume24h'] * coin['price']['USD'] / 1000
                    print(f"{coin['name']}: {trade_volume_usd} USD")
                    raw_data[coin['name']] = {"volume": trade_volume_usd, 'cap': coin['marketCap']}
                    count += 1
            except KeyError as e:
                print("Ошибка обработки монеты:", coin['name'])
    else:
        print("Ошибка:", response.status_code)

    print("Количество монет с ненулевым объемом торгов в USD:", count)
    return raw_data





