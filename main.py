import json

import requests

cache = {}


def currency_you_have():
    your_currency_code = input()
    return your_currency_code.lower()


def currency_you_exchange():
    exchange_currency = input()
    return exchange_currency.lower()


def money_amount():
    amount = input()
    return amount


def converter():
    your_currency = currency_you_have()
    while True:
        exchange = currency_you_exchange()
        if exchange == "":
            break
        else:
            response = requests.get(f'http://www.floatrates.com/daily/{your_currency}.json').json()
            response_json_str = json.dumps(response)
            rates = json.loads(response_json_str)
            if your_currency == "usd":
                cache.update({rates["eur"]["code"]: rates["eur"]["rate"]})
                amount = money_amount()
                print("Checking the cache...")
                if exchange.upper() in cache:
                    print("Oh! It is in the cache!")
                    exchanged_amount = float(amount) * cache[exchange.upper()]
                    print(f'You received {round(exchanged_amount, 2)} {exchange.upper()}.')
                elif exchange.upper() not in cache:
                    print("Sorry, but it is not in the cache!")
                    cache.update({rates[exchange.lower()]["code"]: rates[exchange.lower()]["rate"]})
                    exchanged_amount = float(amount) * cache[exchange.upper()]
                    print(f'You received {round(exchanged_amount, 2)} {exchange.upper()}.')

            elif your_currency == "eur":
                cache.update({rates["usd"]["code"]: rates["usd"]["rate"]})
                amount = money_amount()
                print("Checking the cache...")
                if exchange.upper() in cache:
                    print("Oh! It is in the cache!")
                    exchanged_amount = float(amount) * cache[exchange.upper()]
                    print(f'You received {round(exchanged_amount, 2)} {exchange.upper()}.')
                elif exchange.upper() not in cache:
                    print("Sorry, but it is not in the cache!")
                    cache.update({rates[exchange.lower()]["code"]: rates[exchange.lower()]["rate"]})
                    exchanged_amount = float(amount) * cache[exchange.upper()]
                    print(f'You received {round(exchanged_amount, 2)} {exchange.upper()}.')
            else:
                cache.update({rates["eur"]["code"]: rates["eur"]["rate"]})
                cache.update({rates["usd"]["code"]: rates["usd"]["rate"]})
                amount = money_amount()
                print("Checking the cache...")
                if exchange.upper() in cache:
                    print("Oh! It is in the cache!")
                    exchanged_amount = float(amount) * cache[exchange.upper()]
                    print(f'You received {round(exchanged_amount, 2)} {exchange.upper()}.')
                elif exchange.upper() not in cache:
                    print("Sorry, but it is not in the cache!")
                    cache.update({rates[exchange.lower()]["code"]: rates[exchange.lower()]["rate"]})
                    exchanged_amount = float(amount) * cache[exchange.upper()]
                    print(f'You received {round(exchanged_amount, 2)} {exchange.upper()}.')


converter()
