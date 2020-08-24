from Crypto_modules import CryptoBS  # todo revisar porque no funciona - Solucion: colocar carpetas como source root!!!!

if __name__ == '__main__':
    crypto = CryptoBS()  # crypto es un objeto de la clase CryptoBS

    # print(getcoinlist)

    print(f'Testing CoingeckoAPI: ')
    user_choice = input(f'Select your option:\n'
                        f'1 - Retreive a list of coins\n'
                        f'2 - Check the price of a Crypto\n'
                        f'3 - Search for a CryptoCurrency info\n'
                        f'Option: ')
    # testingAPI('')

    if user_choice == '1':
        print('Ok.. looking into Coingecko')
        crypto.list_coin()
    elif user_choice == '2':

        Crypto = input('Please write the name of Crypto: ')
        Fiat = input('Please write the fiat pair: ')
        crypto.info_crypto(Crypto, Fiat)

    elif user_choice == '3':
        Crypto = input('Please write the name or Symbol of the CryptoCurrency: ')
        crypto.crypto_search(Crypto)
        # print('Function currently in development')
    else:
        print('Select a valid option')
