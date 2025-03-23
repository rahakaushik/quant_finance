import requests
import pandas as pd 
import numpy as np
from datetime import datetime
from datetime import timedelta  
api_key = 'e45110e5ad1b97f10593851c71408113'

def earning_surprises_function(stock_dt):

  symb_date = stock_dt.split('_')    
  stock = symb_date[0]
  earn_date = symb_date[1]

  earning_surprises = requests.get(f'https://financialmodelingprep.com/api/v3/earnings-surprises/{stock}?apikey={api_key}').json()
  earning_surprises = earning_surprises[0:10]
  #print(earning_surprises)
  earn_ch = []
  price_ch = []
  earn_to_price=0

  for n in range(10):
    date = earning_surprises[n]['date']
    #convert object format to date
    date_0 = datetime.strptime(date , '%Y-%m-%d').date()
    actual_earnings =float(earning_surprises[n]['actualEarningResult'])
    estimated_earnings = float(earning_surprises[n]['estimatedEarning'])
    earnings_beat = ((actual_earnings - estimated_earnings)/estimated_earnings)*100

    #get close prices before the earnings and close price after the day of earnings announcement
    price = requests.get(f'https://financialmodelingprep.com/api/v3/historical-price-full/{stock}?serietype=line&apikey={api_key}').json()
    price = price['historical']
    price = pd.DataFrame(price)
    #price 0 is the close price before earnings announcement (I took stocks that announce earnings after the market is closed)
    price_0 = price[price['date'] == str(date_0)]['close'].iloc[0]

    #price 1 is the close price the day after the earnings announcement
    date_1 = date_0 + timedelta(days=1)
    price_1 = price[price['date'] == str(date_1)]['close'].iloc[0]

    price_change = ((price_1 - price_0)/price_0) * 100
    earn_ch.append(earnings_beat)
    price_ch.append(price_change)

    if(earnings_beat > 0.0 and price_change > 0.0):
        earn_to_price +=1 
        #print('on the '+ str(date_0) + ' ' + stock +' beat/miss earnings by ' + str(earnings_beat) +'%' +' and the price changed next day by ' + str(price_change) +'%')
    
  
  ech = np.linalg.norm(earn_ch)
  pch = np.linalg.norm(price_ch)

  norm_ech = earn_ch/ech
  norm_pch = price_ch/pch

  correl_prch = np.corrcoef(norm_ech,norm_pch)
  #print(norm_ech)
  #print(norm_pch)
  #print(earn_to_price)
  #print(correl_prch[0,1])
  if(earn_to_price >= 5):
    profile = requests.get(f'https://financialmodelingprep.com/api/v3/profile/{stock}?apikey={api_key}').json()
    current_price = profile[0]['price']
    range_52 = profile[0]['range']
    #print('The '+ stock +' stock price rose '+ str(earn_to_price) +' out of 10 times, after past earnings report beat estimated earnings')
    print(stock+','+str(earn_date)+','+str(earn_to_price)+','+str(correl_prch[0,1])+','+str(current_price)+','+str(range_52))

#----------------------------------------------------------------

start_date = datetime.today()
start_date = datetime.date(start_date)
end_date = start_date + timedelta(days=14)
#print(start_date,end_date)

tickers=[]
ticker_dates = []
screener = requests.get(f'https://financialmodelingprep.com/api/v3/earning_calendar?from={start_date}&to={end_date}&apikey={api_key}').json()
#screener = requests.get(f'https://financialmodelingprep.com/api/v3/earning_calendar?from=2021-04-26&to=2021-04-30&apikey={api_key}').json()
for item in screener:
  symbol_date = item['symbol']+"_"+item['date']
  ticker_dates.append(symbol_date)
  tickers.append(item['symbol'])

#tickers = ['AAPL','MSFT','ETSY','V','AMZN','FB','JNJ','GOOG']
#print(tickers)

for ticker_dt in ticker_dates:
  try:
    earning_surprises_function(ticker_dt)
  except:
    pass