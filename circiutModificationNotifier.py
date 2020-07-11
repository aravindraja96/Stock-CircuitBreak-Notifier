import requests
import time
from nsetools import Nse


IFTTT_WEBHOOKS_URL ='https://maker.ifttt.com/trigger/{}/with/key/<Key>'
stockSymbol=['infy','sbin']
eventName=''

currentInfo={}
nse=Nse()


def get_price_of_stock(stockSymbol):
    stockInfo=nse.get_quote(stockSymbol)
    currentInfo['upperCircuit']=stockInfo['pricebandupper']
    currentInfo['lowerCircuit']=stockInfo['pricebandlower']
    currentInfo['LTP']=stockInfo['lastPrice']
    return currentInfo
    
def ifttt_configure(eventName):
    event_url=IFTTT_WEBHOOKS_URL.format(eventName)
    data = {'value1':currentInfo['upperCircuit'] , 'value2': currentInfo['lowerCircuit'], 'value3': currentInfo['LTP']}
    requests.post(event_url, json=data)
    
    
    
def main():
    while True:
        time.sleep(10)
        for i in stockSymbol:
            get_price_of_stock(i)
            if currentInfo['upperCircuit'] or currentInfo['upperCircuit'] != currentInfo['LTP']:
                ifttt_configure(eventName)
            else:
                break
    
    
if __name__ == "__main__":
    main()