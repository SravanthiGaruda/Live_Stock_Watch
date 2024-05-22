import yfinance as yf
import time
from cassandra.cluster import Cluster
from datetime import datetime

def getStockPrice(symbol):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(period='1d', interval='1m')
    if not stock_info.empty:
        latest_data = stock_info.iloc[-1]
        stock_price = latest_data['Open']
        return stock_price
    return None

def realTimeStockPrice():
    company_names = ['RELIANCE.NS', 'HDFCBANK.NS', 'TCS.NS', 'INFY.NS', 'SBIN.NS', 'KOTAKBANK.NS', 'LT.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS']
    stock_prices = {}
    for name in company_names:
        price = getStockPrice(name)
        stock_prices[name] = price
    
    cluster = Cluster(['localhost'])
    session = cluster.connect('stock_db')

    def store_stock_price(name, price):
        timestamp = datetime.now()
        session.execute(
            """
            INSERT INTO stockprice (name, price, timestamp)
            VALUES (%s, %s, %s)
            """,
            (name, price, timestamp)
        )

    for symbol, price in stock_prices.items():
        if price is not None:
            store_stock_price(symbol, price)
    print(stock_prices)

if __name__ == '__main__':
    try:
        while True:
            realTimeStockPrice()
            time.sleep(60) 
    except KeyboardInterrupt:
        print("Script terminated by user")
