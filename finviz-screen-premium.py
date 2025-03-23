
# coding: utf-8

# In[19]:


import requests 
import pandas as pd
from datetime import datetime
import sys

for arg in sys.argv[1:]:
       argstr = arg



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


# In[15]:


def get_screener(version,arglist):

    arg_list = arglist.split("-")
    mcap = arg_list[0]
    priceuo = arg_list[1]
    hl20d = arg_list[2]
    screen = requests.get(f'https://finviz.com/screener.ashx?v=111&f=cap_{mcap},geo_usa,sh_price_{priceuo},ta_changeopen_u5,ta_highlow20d_{hl20d}&ft=4&o=-volume', headers = headers).text

    tables = pd.read_html(screen)
    tables = tables[-2]
    tables.columns = tables.iloc[0]
    tables = tables[1:]

    return tables


# In[16]:


tables111 = get_screener('111',argstr)
tables161 = get_screener('161',argstr)
tables121 = get_screener('121',argstr)


# In[29]:


now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
#print(dt_string)


# In[30]:


consolidatedtables = pd.merge(tables111,tables161,how='outer',left_on='Ticker',right_on='Ticker')
consolidatedtables = pd.merge(consolidatedtables,tables121,how='outer',left_on='Ticker',right_on='Ticker')

file_outcsv = "finviz-screen_premium_"+dt_string+".csv"
consolidatedtables.to_csv(file_outcsv)

#print(consolidatedtables)


# In[18]:

arg_list = argstr.split("-")

price_underover = arg_list[1]
if (price_underover == "u10"):
    price_title = "Under $10"
if (price_underover == "o10"):
    price_title = "Over $10"

only_date = dt_string.split('_')

title_string = "Intraday | Date: "+only_date[0]+" | Price: "+price_title

htm_file = open('intraday-premium-'+argstr+'.html','w+')

htmOut = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
    html, body, #container {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
}
    </style>
</head>
<body>

    <div id="anychart-embed-NqAPYRCG" class="anychart-embed anychart-embed-NqAPYRCG">
        <script src="https://cdn.anychart.com/releases/v8/js/anychart-base.min.js"></script>
        <script src="https://cdn.anychart.com/releases/v8/js/anychart-tag-cloud.min.js"></script>
        <div id="ac_style_NqAPYRCG" style="display:none;">
        </div>
        <script>(function(){
        function ac_add_to_head(el){
            var head = document.getElementsByTagName('head')[0];
            head.insertBefore(el,head.firstChild);
        }
        function ac_add_link(url){
            var el = document.createElement('link');
            el.rel='stylesheet';el.type='text/css';el.media='all';el.href=url;
            ac_add_to_head(el);
        }
        function ac_add_style(css){
            var ac_style = document.createElement('style');
            if (ac_style.styleSheet) ac_style.styleSheet.cssText = css;
            else ac_style.appendChild(document.createTextNode(css));
            ac_add_to_head(ac_style);
        }
        
        ac_add_style(document.getElementById("ac_style_NqAPYRCG").innerHTML);
        ac_add_style(".anychart-embed-NqAPYRCG{width:600px;height:450px;}");
        })();</script>
        <div id="container"></div>
        <script>
        anychart.onDocumentReady(function () {
      
          var data = [
              //Copy and paste your data here!!!!!!!
'''

htm_file.write(htmOut)

#price_earnings.drop(price_earnings.tail(1).index, inplace = True) 
for idx, row in consolidatedtables.iterrows(): 
    percent_change = float(row["Change"][:-1])
    sector_str = row["Sector"].split()
    if idx == consolidatedtables.index[-1]:
        #last row
        if(percent_change > 0.0):
            print("{\"x\":","\""+row["Ticker"]+"\""+",","\"value\":", row["Volume"],",category:\"", sector_str[0],"\"}",file=htm_file)      
    else:
        if (percent_change > 0.0):
            print("{\"x\":","\""+row["Ticker"]+"\""+",","\"value\":", row["Volume"],",category:\"", sector_str[0],"\"},",file=htm_file)   

        
htmOut2 = '''
];
        
          // create a tag cloud chart
          var chart = anychart.tagCloud(data);
'''
htm_file.write(htmOut2)

print("chart.title('{}')".format(title_string), file=htm_file)        

htmOut3 = '''
          // set the chart title
          //chart.title('')
          // set array of angles, by which words will be placed
          chart.angles([0])
          // enable color range
          chart.colorRange(true);
          // set color range length
          chart.colorRange().length('80%');
        
        // add an event listener
          chart.listen("pointClick", function(e){
          var url = "https://finance.yahoo.com/quote/" + e.point.get("x");
          window.open(url, "_blank");
        });  
          // display chart
          chart.container("container");
          chart.draw();
        });
        </script>
        </div>

</body>
</html>


'''
htm_file.write(htmOut3)

htm_file.close()

