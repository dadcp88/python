from Price import check_price

input_stock = input(f'Hello Please write your company Stock Symbol (Ticker) - default value: MSFT (Microsoft Corp): ')
stock_info = check_price(input_stock)
print(f'',stock_info)
