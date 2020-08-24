import yfinance

def check_price (stock_symbol='MSFT'):
    stock_details = yfinance.Ticker(stock_symbol)
    stock_details_dict = stock_details.info
    # print(stock_details.info)
    # stock_longName = stock_details.info['longName']
    # stock_fullTimeEmployees = stock_details.info['fullTimeEmployees']
    # print(stock_fullTimeEmployees)
    # return stock_longName, stock_fullTimeEmployees
    return stock_details_dict

#     stock_details.history(start = "2020-01-01", end = "2020-07-30" )
# print(old)
# # stock.download()
# # stock.info
# # print(APPL.history(period="max"))
# stocklist = stock.dividends
# print(stocklist)
