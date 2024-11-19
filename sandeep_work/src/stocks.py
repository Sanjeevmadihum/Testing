from datetime import datetime,timedelta 
import pandas as pd 
import pandas as pd 
import yfinance as yf


def download_stock(stock_list:list,startdate: datetime,enddate: datetime):
    
    data = yf.download(stock_list,start=startdate,end=enddate,group_by='ticker')
    data = data.stack(level=0).rename_axis(['date','stock']).reset_index(level=1)
    data = data.reset_index()
    data = data.sort_values(['stock','date']).reset_index(drop=True)
    return data