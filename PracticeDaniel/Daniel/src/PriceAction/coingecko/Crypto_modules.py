from pycoingecko import CoinGeckoAPI
import time


class CryptoBS:
    cg = CoinGeckoAPI()

    def testingAPI(self, response):
        response = self.cg.ping()
        for key, value in response.items():
            print(key, ': ', value)

    def list_coin(self):  # todo no puedo usar self, why? --- Ya se puede importar.
        # opcion 1
        coinlist = self.cg.get_coins_list()  # esta porqueria es una lista y adentro diccionariossss
        for coin in coinlist:
            print(f'ID: ', coin.get('id', None), '- Symbol: ',
                  coin.get('symbol', None))  # si no se consigue id en los diccionarios retorna None1

    def info_crypto(self, Input_Crypto, Input_Currency):
        # opcion 2
        Input_Currency = Input_Currency.lower()
        Input_Crypto = Input_Crypto.lower()
        currencies = self.cg.get_price(ids=Input_Crypto, vs_currencies=Input_Currency)
        # currencies es un diccionario dentro de otro.
        if currencies == {}:
            print('Crypto Not found, please check your choice')
        else:
            for currency in currencies:
                # if currencies[currency][Input_Currency] not in currencies[currency][Input_Currency]
                #     print('currency pair invalid')
                # else:
                print(currency, currencies[currency][Input_Currency], Input_Currency)

    def crypto_search(self, Input_Crypto):
        # opcion 3
        coinlist = self.cg.get_coins_list()  # el resultado es una lista y adentro diccionarios.
        # print(coinlist.items())

        for coin in coinlist:

            # el if recorre el diccionario e imprime solo cuando encuentra el match, los registros donde no lo encuentre sigue al else
            if coin.get('name').lower() == Input_Crypto.lower() or coin.get(
                    'symbol').lower() == Input_Crypto.lower():  # el .lower es para formatear el input en minusculas

                print('This is: ', coin)
                break
            else:
                # print('No se encontro registro')
                continue
