from sanic import Sanic
from sanic.response import json, text
from googlefinance import getQuotes
import time
from aoiklivereload import LiveReloader
import os

app = Sanic(__name__)


@app.route("/getQuotes", methods=['GET','POST'])
async def get_quotes(request):
    x = request.query_string.replace("stocks=","")
    y = x.split(",")
    z = getQuotes(y)
    print(z)
    return json(z)

@app.route("/price", methods=['GET','POST'])
async def get_price(request):
    raw_stocks = request.query_string.replace("stocks=","")
    stocklist = raw_stocks.split(",")
    get_stocks = getQuotes(stocklist)
    price_list = []
    for stock in get_stocks:
        price = stock['LastTradePrice']
        symbol = stock['StockSymbol']
        price_list.append({symbol:price})
    print(price_list)
    return json(price_list)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=os.environ['PORT'])