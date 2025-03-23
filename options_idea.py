import requests
import datetime
import pandas as pd
import sys
from random import sample


# In[4]:


def get_option_chain(symbol,exp_date):
    response = requests.get('https://sandbox.tradier.com/v1/markets/options/chains',
    params={'symbol': symbol, 'expiration': exp_date, 'greeks': 'false'},
    headers={'Authorization': 'Bearer PP1XerfFMh97HbpxjkGpEf5FZvTL', 'Accept': 'application/json'})

    json_response = response.json()
    l1 = json_response['options']
    l2 = l1['option']
    return l2


# In[13]:


today = datetime.date.today()
friday = today + datetime.timedelta( (4-today.weekday()))
n2_friday = friday + datetime.timedelta(6)
#print(n2_friday)


# In[6]:


def get_last_price_single(symbol):

    response = requests.get('https://sandbox.tradier.com/v1/markets/quotes',
    params={'symbols': symbol},
    headers={'Authorization': 'Bearer PP1XerfFMh97HbpxjkGpEf5FZvTL', 'Accept': 'application/json'})
    json_response_quote = response.json()
    quote_l1=json_response_quote['quotes']
    last_price = quote_l1['quote']['last']
    return last_price


# In[7]:


def get_batch_quotes(symbol_string):
    response = requests.get('https://sandbox.tradier.com/v1/markets/quotes',
    params={'symbols': symbol_string },
    headers={'Authorization': 'Bearer PP1XerfFMh97HbpxjkGpEf5FZvTL', 'Accept': 'application/json'})
    json_response_quote = response.json()
    return json_response_quote


# In[8]:


def get_last_price(symbol,json_response_quote):
    l1=json_response_quote['quotes']
    l2= l1['quote']
    for i in range(len(l2)):
        if(l2[i]['symbol'] == symbol):
            last_price = l2[i]['last']
            return(last_price)


# In[9]:

# In[22]:


def main():
    for arg in sys.argv[1:]:
       argstr = arg
    
    arg_list = argstr.split("-")
    num_fri = arg_list[0]
    sort_col = arg_list[1]
    sort_ord = arg_list[2] 
    sector_op = arg_list[3]
    otm_op = arg_list[4]
    
    #snp500
    ticker_list = ['AAPL','ABBV','ABT','ACN','ADBE','AGN','AIG','ALL','AMGN','AMZN','AXP','BA','BAC','BIIB','BK','BKNG','BLK','BMY','C','CAT','CELG','CHTR','CL','CMCSA','COF','COP','COST','CSCO','CVS','CVX','DD','DHR','DIS','DOW','DUK','EMR','EXC','F','FB','FDX','GD','GE','GILD','GM','GOOG','GOOGL','GS','HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI','KO','LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE','NVDA','ORCL','OXY','PEP','PFE','PG','PM','PYPL','QCOM','RTN','SBUX','SLB','SO','SPG','T','TGT','TXN','UNH','UNP','UPS','USB','UTX','V','VZ','WBA','WFC','WMT','XOM']
    #ticker_full = ['A','AAL','AAP','AAPL','ABBV','ABC','ABMD','ABT','ACN','ADBE','ADI','ADM','ADP','ADS','ADSK','AEE','AEP','AES','AFL','AGN','AIG','AIV','AIZ','AJG','AKAM','ALB','ALGN','ALK','ALL','ALLE','ALXN','AMAT','AMCR','AMD','AME','AMG','AMGN','AMP','AMT','AMZN','ANET','ANSS','ANTM','AON','AOS','APA','APD','APH','APTV','ARE','ARNC','ATO','ATVI','AVB','AVGO','AVY','AWK','AXP','AZO','BA','BAC','BAX','BBT','BBY','BDX','BEN','BHGE','BIIB','BK','BKNG','BLK','BLL','BMY','BR','BRK.B','BSX','BWA','BXP','C','CAG','CAH','CAT','CB','CBOE','CBRE','CBS','CCI','CCL','CDNS','CE','CELG','CERN','CF','CFG','CHD','CHRW','CHTR','CI','CINF','CL','CLX','CMA','CMCSA','CME','CMG','CMI','CMS','CNC','CNP','COF','COG','COO','COP','COST','COTY','CPB','CPRI','CPRT','CRM','CSCO','CSX','CTAS','CTL','CTSH','CTVA','CTXS','CVS','CVX','CXO','D','DAL','DD','DE','DFS','DG','DGX','DHI','DHR','DIS','DISCA','DISCK','DISH','DLR','DLTR','DOV','DOW','DRE','DRI','DTE','DUK','DVA','DVN','DXC','EA','EBAY','ECL','ED','EFX','EIX','EL','EMN','EMR','EOG','EQIX','EQR','ES','ESS','ETFC','ETN','ETR','EVRG','EW','EXC','EXPD','EXPE','EXR','F','FANG','FAST','FB','FBHS','FCX','FDX','FE','FFIV','FIS','FISV','FITB','FLIR','FLS','FLT','FMC','FOX','FOXA','FRC','FRT','FTI','FTNT','FTV','GD','GE','GILD','GIS','GL','GLW','GM','GOOG','GOOGL','GPC','GPN','GPS','GRMN','GS','GWW','HAL','HAS','HBAN','HBI','HCA','HCP','HD','HES','HFC','HIG','HII','HLT','HOG','HOLX','HON','HP','HPE','HPQ','HRB','HRL','HSIC','HST','HSY','HUM','IBM','ICE','IDXX','IEX','IFF','ILMN','INCY','INFO','INTC','INTU','IP','IPG','IPGP','IQV','IR','IRM','ISRG','IT','ITW','IVZ','JBHT','JCI','JEC','JEF','JKHY','JNJ','JNPR','JPM','JWN','K','KEY','KEYS','KHC','KIM','KLAC','KMB','KMI','KMX','KO','KR','KSS','KSU','L','LB','LDOS','LEG','LEN','LH','LHX','LIN','LKQ','LLY','LMT','LNC','LNT','LOW','LRCX','LUV','LW','LYB','M','MA','MAA','MAC','MAR','MAS','MCD','MCHP','MCK','MCO','MDLZ','MDT','MET','MGM','MHK','MKC','MKTX','MLM','MMC','MMM','MNST','MO','MOS','MPC','MRK','MRO','MS','MSCI','MSFT','MSI','MTB','MTD','MU','MXIM','MYL','NBL','NCLH','NDAQ','NEE','NEM','NFLX','NI','NKE','NKTR','NLSN','NOC','NOV','NRG','NSC','NTAP','NTRS','NUE','NVDA','NWL','NWS','NWSA','O','OKE','OMC','ORCL','ORLY','OXY','PAYX','PBCT','PCAR','PEG','PEP','PFE','PFG','PG','PGR','PH','PHM','PKG','PKI','PLD','PM','PNC','PNR','PNW','PPG','PPL','PRGO','PRU','PSA','PSX','PVH','PWR','PXD','PYPL','QCOM','QRVO','RCL','RE','REG','REGN','RF','RHI','RJF','RL','RMD','ROK','ROL','ROP','ROST','RSG','RTN','SBAC','SBUX','SCHW','SEE','SHW','SIVB','SJM','SLB','SLG','SNA','SNPS','SO','SPG','SPGI','SRE','STI','STT','STX','STZ','SWK','SWKS','SYF','SYK','SYMC','SYY','T','TAP','TDG','TEL','TFX','TGT','TIF','TJX','TMO','TMUS','TPR','TRIP','TROW','TRV','TSCO','TSN','TSS','TTWO','TWTR','TXN','TXT','UA','UAA','UAL','UDR','UHS','ULTA','UNH','UNM','UNP','UPS','URI','USB','UTX','V','VAR','VFC','VIAB','VLO','VMC','VNO','VRSK','VRSN','VRTX','VTR','VZ','WAB','WAT','WBA','WCG','WDC','WEC','WELL','WFC','WHR','WLTW','WM','WMB','WMT','WRK','WU','WY','WYNN','XEC','XEL','XLNX','XOM','XRAY','XRX','XYL','YUM','ZBH','ZION','ZTS']
    #ticker_list = ['AAPL','GOOG']
    #ticker_list = sample(ticker_full,100)
    ticker_string = ','.join(ticker_list)
    ticker_response_quotes = get_batch_quotes(ticker_string)
    op_ideas = []

    for i in range(len(ticker_list)):
        ticker = ticker_list[i]
        last_price = get_last_price(ticker,ticker_response_quotes)
        if last_price is None: 
            continue
        if float(last_price) <= 10:
            continue
        try:
            today = datetime.date.today()
            friday = today + datetime.timedelta( (4-today.weekday()))
            n_friday = friday + datetime.timedelta(7)
            #print(n_friday)
            if(num_fri == 'n1'):
              option_chain = get_option_chain(ticker, friday)
              exp_date = friday
            if(num_fri == 'n2'):
              option_chain = get_option_chain(ticker, n_friday)
              exp_date = n_friday
        except:
            continue
    
        for i in range(len(option_chain)): 
            if(option_chain[i]['option_type'] == 'put'):
        
                strike_price = option_chain[i]['strike']
                #print(strike_price)
                if strike_price is None:
                    continue
                strike_diff = float(strike_price)-float(last_price)
                collateral = strike_price*100;
                #print(strike_diff)
                if -10.0 <= strike_diff <= 5.0:
                    bid = option_chain[i]['bid']
                    if bid is not None:
                      if strike_diff >= 0.0:
                        itm_put_profit = (last_price-strike_price)*100 + bid*100
                        itm_break_even = strike_price-bid
                        otm_put_profit = "NA"
                        otm_break_even = "NA"
                      if strike_diff < 0.0:
                        itm_put_profit = "NA"
                        itm_break_even = "NA"
                        otm_put_profit = bid*100
                        otm_break_even = (collateral - otm_put_profit)/100
                      if bid >= 0.9:    
                        price_to_prem = strike_price/bid
                        op_id_tup = (ticker, last_price, strike_price, collateral, bid, itm_put_profit,itm_break_even,otm_put_profit,otm_break_even,price_to_prem,exp_date) 
                        op_ideas.append(op_id_tup)
    ops_df = pd.DataFrame(op_ideas,columns=['Symbol','Last_Price','Strike_Price','Collateral','Bid','ITM_Profit','ITM_BE','OTM_Profit','OTM_BE','Price_Premium','Exp_Date'])
    ops_df.sort_values(by=[sort_col],inplace=True,ascending=sort_ord)
    print(ops_df.head())
    op_file_out = sector_op+'-'+otm_op+'_profit.csv'
    ops_df.to_csv(op_file_out,index=False)

if __name__ == "__main__":
    main()

