import requests
import pandas as pd 
import numpy as np
from datetime import datetime
from datetime import timedelta  
import json
api_key = 'e45110e5ad1b97f10593851c71408113'



tickers=[]
screener = requests.get(f'https://financialmodelingprep.com/api/v4/insider-trading-rss-feed?&apikey={api_key}').json()
for item in screener:
  tickers.append(item['symbol'])

#tickers = ['AAPL','MSFT','ETSY','V','AMZN','FB','JNJ','GOOG']
tickers = list(set(tickers))
#print(tickers)

WhlList = []
for ticker in tickers:
  #print(ticker)
  try:
    WhlMetrics = {}
    whaledata = requests.get(f'https://financialmodelingprep.com/api/v4/insider-trading?symbol={ticker}&limit=1&apikey={api_key}').json()
    WhlList.append(whaledata[0])
    #print(whaledata)
    transDate = whaledata[0]['transactionDate']
    transType = whaledata[0]['transactionType']
    stocksOwned = whaledata[0]['securitiesOwned']
    execName = whaledata[0]['reportingName']
    execTitle = whaledata[0]['typeOfOwner']
    stockstrans = whaledata[0]['securitiesTransacted']
    stockprice = whaledata[0]['price']

    WhlMetrics[ticker] = {}
    WhlMetrics[ticker]['Symbol'] = ticker
    WhlMetrics[ticker]['Transaction_Date'] = transDate
    WhlMetrics[ticker]['Transaction_Type'] = transType
    WhlMetrics[ticker]['Executive_Name'] = execName
    WhlMetrics[ticker]['Executive_Title'] = execTitle
    WhlMetrics[ticker]['Stocks_Transacted'] = stockstrans
    WhlMetrics[ticker]['Stocks_Owned'] = stocksOwned

  except:
    pass


#print(WhlList)
#pd.read_json(json.dumps(WhlList)).to_csv('json-test.csv')
WhlWatchFrame = pd.DataFrame.from_records(WhlList)
WhlWatchFrame.drop(['reportingCik','companyCik','acquistionOrDisposition','formType','securityName','link'],axis=1,inplace=True)
WhlWatchFrame.rename(columns={'symbol':'SYMBOL','transactionDate':'DATE','transactionType':'TYPE','securitiesOwned':'#OWNED','reportingName':'NAME','typeOfOwner':'TITLE','securitiesTransacted':'#TRANSACT','price':'PRICE'},inplace=True)
#print(WhlWatchFrame)
WhlWatchFrame.to_csv('whale-watch-out.csv',index=False)
#WhlWatchFrame.to_html('whale-watch-out.html',classes='table table-striped')

