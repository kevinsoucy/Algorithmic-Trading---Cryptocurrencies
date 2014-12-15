import requests
import time
import csv
import ast

while True:

    doge = requests.get('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132')
    ltdict = ast.literal_eval(doge.text)
    
    ltret = ltdict.get('return').values()[0].values()[0]  

    price = float(ltret.get('lasttradeprice'))
    BuyOrders = ltret.get('buyorders')[0:20] #list of dicts
    SellOrders = ltret.get('sellorders')[0:20] #list of dicts
    volume = float(ltret.get('volume'))

    BuyOrders = [dict([a, float(x)] for a, x in b.iteritems()) for b in BuyOrders]
    SellOrders = [dict([a, float(x)] for a, x in b.iteritems()) for b in SellOrders]
    
# for lists: [float(i) for i in lst]
# for dict: [map(float, x) for x in dict] 
# for values in dicts within list [dict([a, float(x)] for a, x in b.iteritems()) for b in list]

#Start loop of updating and appending    
    #btstick = requests.get('https://www.bitstamp.net/api/ticker/')
    #btsorder = requests.get('https://www.bitstamp.net/api/order_book/')
    #btstick1 = ast.literal_eval(ltc.text).values() #ask, bid, high, last, low, timestamp, volume, vwap
    #btstick2 = [float(x) for x in btstick1] #convert to float
    #btsbids = ast.literal_eval(btsorder.text).get('bids')[0:20]  #list of bids [price, vol]
    #btsbids = [map(float, x) for x in btsbids] 
    #btsasks = ast.literal_eval(btsorder.text).get('asks')[0:20]  
    #btsasks = [map(float, x) for x in btsasks] #convert to int
    

    
    bidpv1 = BuyOrders[0].get('price')*BuyOrders[0].get('quantity') + BuyOrders[1].get('price')*BuyOrders[1].get('quantity') + BuyOrders[2].get('price')*BuyOrders[2].get('quantity') + BuyOrders[3].get('price')*BuyOrders[3].get('quantity') + BuyOrders[4].get('price')*BuyOrders[4].get('quantity')

    bidv1 = BuyOrders[0].get('quantity') + BuyOrders[1].get('quantity') + BuyOrders[2].get('quantity') + BuyOrders[3].get('quantity') + BuyOrders[4].get('quantity')

    bidp1 = bidpv1/bidv1

    bidpv2 = (BuyOrders[5].get('price')*BuyOrders[5].get('quantity')+ BuyOrders[6].get('price')*BuyOrders[6].get('quantity') + BuyOrders[7].get('price')*BuyOrders[7].get('quantity')+ BuyOrders[8].get('price')*BuyOrders[8].get('quantity')+ BuyOrders[9].get('price')*BuyOrders[9].get('quantity'))

    bidv2 = BuyOrders[5].get('quantity') + BuyOrders[6].get('quantity') + BuyOrders[7].get('quantity') + BuyOrders[8].get('quantity') + BuyOrders[9].get('quantity')

    bidp2 = bidpv2/bidv2

    bidpv3 = (BuyOrders[10].get('price')*BuyOrders[10].get('quantity')+ BuyOrders[11].get('price')*BuyOrders[11].get('quantity')+ BuyOrders[12].get('price')*BuyOrders[12].get('quantity')+ BuyOrders[13].get('price')*BuyOrders[13].get('quantity')+ BuyOrders[14].get('price')*BuyOrders[14].get('quantity'))

    bidv3 = BuyOrders[10].get('quantity')+ BuyOrders[11].get('quantity')+ BuyOrders[12].get('quantity')+ BuyOrders[13].get('quantity')+ BuyOrders[14].get('quantity')

    bidp3 = bidpv3/bidv3

    bidpv4 = (BuyOrders[15].get('price')*BuyOrders[15].get('quantity') + BuyOrders[16].get('price')*BuyOrders[16].get('quantity') + BuyOrders[17].get('price')*BuyOrders[17].get('quantity')+ BuyOrders[18].get('price')*BuyOrders[18].get('quantity')+ BuyOrders[19].get('price')*BuyOrders[19].get('quantity'))

    bidv4 = BuyOrders[15].get('quantity') + BuyOrders[16].get('quantity') + BuyOrders[17].get('quantity') + BuyOrders[18].get('quantity') + BuyOrders[19].get('quantity')

    bidp4 = bidpv4/bidv4
        
    askpv1 = SellOrders[0].get('price')*SellOrders[0].get('quantity') + SellOrders[1].get('price')*SellOrders[1].get('quantity') + SellOrders[2].get('price')*SellOrders[2].get('quantity') + SellOrders[3].get('price')*SellOrders[3].get('quantity') + SellOrders[4].get('price')*SellOrders[4].get('quantity')

    askv1 = SellOrders[0].get('quantity') + SellOrders[1].get('quantity') + SellOrders[2].get('quantity') + SellOrders[3].get('quantity') + SellOrders[4].get('quantity')

    askp1 = askpv1/askv1

    askpv2 = (SellOrders[5].get('price')*SellOrders[5].get('quantity') + SellOrders[6].get('price')*SellOrders[6].get('quantity') + SellOrders[7].get('price')*SellOrders[7].get('quantity') + SellOrders[8].get('price')*SellOrders[8].get('quantity') + SellOrders[9].get('price')*SellOrders[9].get('quantity'))
    askv2 = SellOrders[5].get('quantity') + SellOrders[6].get('quantity') + SellOrders[7].get('quantity') + SellOrders[8].get('quantity') + SellOrders[9].get('quantity')

    askp2 = askpv2/askv2

    askpv3 = (SellOrders[10].get('price')*SellOrders[10].get('quantity') + SellOrders[11].get('price')*SellOrders[11].get('quantity') + SellOrders[12].get('price')*SellOrders[12].get('quantity') + SellOrders[13].get('price')*SellOrders[13].get('quantity') + SellOrders[14].get('price')*SellOrders[14].get('quantity'))

    askv3 = SellOrders[10].get('quantity')+ SellOrders[11].get('quantity')+ SellOrders[12].get('quantity')+ SellOrders[13].get('quantity')+ SellOrders[14].get('quantity')

    askp3 = askpv3/askv3

    askpv4 = (SellOrders[15].get('price')*SellOrders[15].get('quantity') + SellOrders[16].get('price')*SellOrders[16].get('quantity') + SellOrders[17].get('price')*SellOrders[17].get('quantity') + SellOrders[18].get('price')*SellOrders[18].get('quantity') + SellOrders[19].get('price')*SellOrders[19].get('quantity'))

    askv4 = SellOrders[15].get('quantity') + SellOrders[16].get('quantity') + SellOrders[17].get('quantity') + SellOrders[18].get('quantity') + SellOrders[19].get('quantity')

    askp4 = askpv4/askv4

#Output: Volume last time bid vwap high low ask bid1 bidv1 bid2 bidv2 bid3 bidv3 bid4 bidv4
    Addrow = [time.time()]+[price] + [volume] +  [bidp1] + [bidv1] + [bidp2] + [bidv2] + [bidp3] + [bidv3] + [bidp4] + [bidv4] + [askp1] + [askv1] + [askp2] + [askv2] + [askp3] + [askv3] + [askp4] + [askv4]
    
    toadd = open('doge.csv', 'a')
    wr = csv.writer(toadd, quoting=csv.QUOTE_MINIMAL)
    wr.writerow(Addrow)

    time.sleep(15)