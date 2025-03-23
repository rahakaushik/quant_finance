from trafalgar import *
from random import sample
from io import StringIO 
import sys
import requests



class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


for arg in sys.argv[1:]:
       argstr = arg
arg_list = argstr.split("-")

ticker_op = arg_list[0]
metric_op = arg_list[1]
iter_op = arg_list[2]
date_start = arg_list[3]
date_end = arg_list[4]

date_start = date_start.replace("_","-")
date_end = date_end.replace("_","-")

#tickers = ["AAPL", "FB", "MSFT", "AMD", "TSLA", "NFLX", "SBUX", "GOOG"]
ticker_tradable = []
screener = requests.get(f'https://financialmodelingprep.com/api/v3/available-traded/list?apikey=e45110e5ad1b97f10593851c71408113').json()
for item in screener:
  ticker_tradable.append(item['symbol'])

ticker_nasdaq100 = []
screener = requests.get(f'https://financialmodelingprep.com/api/v3/nasdaq_constituent?apikey=e45110e5ad1b97f10593851c71408113').json()
for item in screener:
  ticker_nasdaq100.append(item['symbol'])

ticker_snp500 = ['AAPL','ABBV','ABT','ACN','ADBE','AIG','ALL','AMGN','AMZN','AXP','BA','BAC','BIIB','BK','BKNG','BLK','BMY','C','CAT','CHTR','CL','CMCSA','COF','COP','COST','CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE','GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI','KO','LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL','OXY','PEP','PFE','PG','PM','PYPL','QCOM','SBUX','SLB','SO','SPG','T','TGT','TXN','UNH','UNP','UPS','USB','V','VZ','WBA','WFC','WMT','XOM']


count = 0
output = []
best_expected = 0.0
best_sharpe_ratio = 0.0

if(ticker_op == "tradable"):
    ticker_list = ticker_tradable
if(ticker_op == "nas100"):
    ticker_list = ticker_nasdaq100
if(ticker_op == "snp500"):
    ticker_list = ticker_snp500

while count < int(iter_op):
    tickers = sample(ticker_list,10)
    #print(tickers)
    
    with Capturing() as output:
        efficient_frontier(tickers, date_start, date_end, 10000)
    
    wts_list = output[1]
    returns_list = output[3].split()
    this_expected_returns = float(returns_list[5])
    sharpe_list = output[5].split()
    this_sharpe_ratio = float(sharpe_list[3])
    #print(this_expected_returns)
    
    if(metric_op == "returns"):
        if(this_expected_returns > best_expected):
            best_expected = round(float(this_expected_returns),2)
            best_wts_list = wts_list
            best_ticker_list = tickers

    if(metric_op == "sharpe"):
        if(this_sharpe_ratio > best_expected):
            best_expected = round(float(this_sharpe_ratio),2)
            best_wts_list = wts_list
            best_ticker_list = tickers

    count += 1
        
#print(best_ticker_list)
#print(best_wts_list)
#print(best_expected)


best_wts_list = (best_wts_list[1:])
best_wts_list = (best_wts_list[:-1])

#print(best_wts_list)

best_wts_float  = []

for item in best_wts_list.split(','):
    best_wts_float.append(round(float(item),2))

best_dict = dict(zip(best_ticker_list,best_wts_float))

#print (str(best_dict))

#htm_file = open('efp_v1.html','w+')

htmOut = '''

<html>
<head>  
<script>
window.onload = function () {

var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	title:{
		text: "Portfolio Allocation",
		horizontalAlign: "center"
	},
	data: [{
		type: "doughnut",
		startAngle: 60,
		//innerRadius: 60,
		indexLabelFontSize: 17,
		indexLabel: "{label} - #percent%",
		toolTipContent: "<b>{label}:</b> {y} (#percent%)",
		dataPoints: [
'''
#htm_file.write(htmOut)
#htm_file.close()
print(htmOut)

key_count = 0
num_keys = len(best_dict.keys())

for key in best_dict:
    key_count += 1
    if(key_count == num_keys):
        print("{ y: "+str(best_dict[key])+", label: \""+key+"\" }")
    else:
        print("{ y: "+str(best_dict[key])+", label: \""+key+"\" },")

htmOut2 = '''

		]
	}]
});
chart.render();

}
</script>
</head>
<body>
<font face="verdana">
'''
print(htmOut2)

print("<p align='center'>Period: "+date_start+" to "+date_end)

if(metric_op == "returns"):
    print("<br>Expected Returns (%): "+str(best_expected))
if(metric_op == "sharpe"):
    print("<br>Sharpe Ratio: "+str(best_expected))

htmOut2 = '''
</p></font>
<div id="chartContainer" style="height: 370px; width: 100%;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>

'''

print(htmOut2)
