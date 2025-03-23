import requests
import pandas as pd
import json
import numpy as np
import scipy.optimize as sco
from random import sample, randint
from datetime import datetime
import sys
from io import StringIO 


api_key = 'e45110e5ad1b97f10593851c71408113'


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns*weights ) *252
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return std, returns


# In[181]:


def random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate):
    results = np.zeros((5,num_portfolios))
    weights_record = []
    for i in range(num_portfolios):
        weights = np.random.random(4)
        weights /= np.sum(weights)
        weights_record.append(weights)
        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(weights, mean_returns, cov_matrix)
        results[0,i] = portfolio_std_dev
        results[1,i] = portfolio_return
        results[2,i] = (portfolio_return - risk_free_rate) / portfolio_std_dev
    return results, weights_record


# In[182]:


def display_simulated_ef_with_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate):
    results, weights = random_portfolios(num_portfolios,mean_returns, cov_matrix, risk_free_rate)
    
    max_sharpe_idx = np.argmax(results[2])
    sdp, rp = results[0,max_sharpe_idx], results[1,max_sharpe_idx]
    max_sharpe_allocation = pd.DataFrame(weights[max_sharpe_idx],index=table.columns,columns=['allocation'])
    max_sharpe_allocation.allocation = [round(i*100,2)for i in max_sharpe_allocation.allocation]
    max_sharpe_allocation = max_sharpe_allocation.T
    
    min_vol_idx = np.argmin(results[0])
    sdp_min, rp_min = results[0,min_vol_idx], results[1,min_vol_idx]
    min_vol_allocation = pd.DataFrame(weights[min_vol_idx],index=table.columns,columns=['allocation'])
    min_vol_allocation.allocation = [round(i*100,2)for i in min_vol_allocation.allocation]
    min_vol_allocation = min_vol_allocation.T
    
    print("-"*80)
    print("Maximum Sharpe Ratio Portfolio Allocation\n")
    print("Annualised Return:", round(rp,2))
    print("Annualised Volatility:", round(sdp,2))
    print("\n")
    print(max_sharpe_allocation)
    print("-"*80)
    print("Minimum Volatility Portfolio Allocation\n")
    print("Annualised Return:", round(rp_min,2))
    print("Annualised Volatility:", round(sdp_min,2))
    print("\n")
    print(min_vol_allocation)


# In[232]:


ticker_list = ['AAPL','ABBV','ABT','ACN','ADBE','AIG','ALL','AMGN','AMZN','AXP','BA','BAC','BIIB','BK','BKNG','BLK','BMY','C','CAT','CHTR','CL','CMCSA','COF','COP','COST','CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE','GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI','KO','LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL','OXY','PEP','PFE','PG','PM','PYPL','QCOM','SBUX','SLB','SO','SPG','T','TGT','TXN','UNH','UNP','UPS','USB','V','VZ','WBA','WFC','WMT','XOM']



def neg_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate):
    p_var, p_ret = portfolio_annualised_performance(weights, mean_returns, cov_matrix)
    return -(p_ret - risk_free_rate) / p_var

def max_sharpe_ratio(mean_returns, cov_matrix, risk_free_rate):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix, risk_free_rate)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bound = (0.0,1.0)
    bounds = tuple(bound for asset in range(num_assets))
    result = sco.minimize(neg_sharpe_ratio, num_assets*[1./num_assets,], args=args,
                        method='SLSQP', bounds=bounds, constraints=constraints)
    return result




def portfolio_volatility(weights, mean_returns, cov_matrix):
    return portfolio_annualised_performance(weights, mean_returns, cov_matrix)[0]

def min_variance(mean_returns, cov_matrix):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bound = (0.0,1.0)
    bounds = tuple(bound for asset in range(num_assets))

    result = sco.minimize(portfolio_volatility, num_assets*[1./num_assets,], args=args,
                        method='SLSQP', bounds=bounds, constraints=constraints)

    return result


def efficient_return(mean_returns, cov_matrix, target):
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix)

    def portfolio_return(weights):
        return portfolio_annualised_performance(weights, mean_returns, cov_matrix)[1]

    constraints = ({'type': 'eq', 'fun': lambda x: portfolio_return(x) - target},
                   {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0,1) for asset in range(num_assets))
    result = sco.minimize(portfolio_volatility, num_assets*[1./num_assets,], args=args, method='SLSQP', bounds=bounds, constraints=constraints)
    return result


def efficient_frontier(mean_returns, cov_matrix, returns_range):
    efficients = []
    for ret in returns_range:
        efficients.append(efficient_return(mean_returns, cov_matrix, ret))
    return efficients


# In[224]:


def display_calculated_ef_with_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate):
    results, _ = random_portfolios(num_portfolios,mean_returns, cov_matrix, risk_free_rate)
    
    max_sharpe = max_sharpe_ratio(mean_returns, cov_matrix, risk_free_rate)
    sdp, rp = portfolio_annualised_performance(max_sharpe['x'], mean_returns, cov_matrix)
    max_sharpe_allocation = pd.DataFrame(max_sharpe.x,index=table.columns,columns=['allocation'])
    max_sharpe_allocation.allocation = [round(i*100,2)for i in max_sharpe_allocation.allocation]
    max_sharpe_allocation = max_sharpe_allocation.T
    max_sharpe_allocation

    min_vol = min_variance(mean_returns, cov_matrix)
    sdp_min, rp_min = portfolio_annualised_performance(min_vol['x'], mean_returns, cov_matrix)
    min_vol_allocation = pd.DataFrame(min_vol.x,index=table.columns,columns=['allocation'])
    min_vol_allocation.allocation = [round(i*100,2)for i in min_vol_allocation.allocation]
    min_vol_allocation = min_vol_allocation.T
    
    print("-"*80)
    print("Maximum Sharpe Ratio Portfolio Allocation\n")
    print("Annualised Return:", round(rp,2))
    print("Annualised Volatility:", round(sdp,2))
    print("\n")
    print(max_sharpe_allocation)
    print("-"*80)
    print("Minimum Volatility Portfolio Allocation\n")
    print("Annualised Return:", round(rp_min,2))
    print("Annualised Volatility:", round(sdp_min,2))
    print("\n")
    print(min_vol_allocation)


iter_op = 20
count = 0
best_sharpe_return = 0.0

while count < int(iter_op):
    

    companies = sample(ticker_list,4)
    price = {}

    for company in companies:
        prices_retrieval = requests.get(f'https://financialmodelingprep.com/api/v3/historical-price-full/{company}?timeseries=350&apikey={api_key}').json()
        symbol = prices_retrieval['symbol']
        prices_retrieval = prices_retrieval['historical']
        price[company] = {}
        for item in prices_retrieval:
            price_date = item['date']
            price[company][price_date] = item['adjClose']
        price_DF = pd.DataFrame.from_dict(price)
    
    table = price_DF.iloc[1: , :]
    table = table.iloc[::-1]
    
    returns = table.pct_change()
    
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    num_portfolios = 25000
    risk_free_rate = 0.0178

    
    
    with Capturing() as output:
        display_calculated_ef_with_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate)
    
    
    returns_list = output[3].split()
    max_sharpe_return = float(returns_list[2])
    volatity_list = output[4].split()
    max_sharpe_vola = float(volatity_list[2])
    sharpe_ticker_list = output[7]
    sharpe_allocation_list = output[8]
    if(max_sharpe_return > best_sharpe_return):
        chkz = sharpe_allocation_list.split()
        prod_chkz = float(chkz[randint(1,4)])*float(chkz[randint(1,4)])*float(chkz[randint(1,4)])
        #print(prod_chkz)
        if(prod_chkz > 0.0):
            best_allocation_list = sharpe_allocation_list.split()
            best_sharpe_return = max_sharpe_return
            best_sharpe_vola = max_sharpe_vola
            best_ticker_list = sharpe_ticker_list.split()
        

    #wts_list = output[1]
    #returns_list = output[3].split()
    #this_expected_returns = float(returns_list[5])
    #sharpe_list = output[5].split()
    #this_sharpe_ratio = float(sharpe_list[3])
    #print(this_expected_returns)
    
    #if(metric_op == "returns"):
    #    if(this_expected_returns > best_expected):
    #        best_expected = round(float(this_expected_returns),2)
    #        best_wts_list = wts_list
    #        best_ticker_list = tickers

    #if(metric_op == "sharpe"):
    #    if(this_sharpe_ratio > best_expected):
    #        best_expected = round(float(this_sharpe_ratio),2)
    #        best_wts_list = wts_list
    #        best_ticker_list = tickers

    count += 1


print("<hr><table border=1><tr>")    
print("<td>",best_ticker_list[0],"</td><td>",best_ticker_list[1],"</td><td>",best_ticker_list[2],"</td><td>",best_ticker_list[3],"</td></tr>")
print("<tr><td>",best_allocation_list[1],"</td><td>",best_allocation_list[2],"</td><td>",best_allocation_list[3],"</td><td>",best_allocation_list[4],"</td></tr></table>")
print("<br><b>")    
print("Maximum Sharpe Return:",best_sharpe_return)
print("</b><br>")
print("Volatility:",best_sharpe_vola)


