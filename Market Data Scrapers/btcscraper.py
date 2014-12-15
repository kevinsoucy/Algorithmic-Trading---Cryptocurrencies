import requests
import time
import csv
import ast
import time

start_time = time.time()

while True:
#Start loop of updating and appending

    btstick = requests.get('https://www.bitstamp.net/api/ticker/')
    btsorder = requests.get('https://www.bitstamp.net/api/order_book/')

    btstick1 = ast.literal_eval(btstick.text).values() #ask, bid, high, last, low, timestamp, volume, vwap
    btstick2 = [float(x) for x in btstick1] #convert to float
    btsbids = ast.literal_eval(btsorder.text).get('bids')[0:20]  #list of bids [price, vol]
    btsbids = [map(float, x) for x in btsbids] 
    btsasks = ast.literal_eval(btsorder.text).get('asks')[0:20]  
    btsasks = [map(float, x) for x in btsasks] #convert to int
    btstime = ast.literal_eval(btsorder.text).get('timestamp')

    bidpv1 = (btsbids[0][1]*btsbids[0][0] + btsbids[1][1]*btsbids[1][0] + btsbids[2][1]*btsbids[2][0] + btsbids[3][1]*btsbids[3][0] + btsbids[4][1]*btsbids[4][0])
    bidv1 = btsbids[0][1] + btsbids[1][1] + btsbids[2][1] + btsbids[3][1] + btsbids[4][1]
    bidpv1 = bidpv1/bidv1
    
    bidpv2 = (btsbids[5][1]*btsbids[5][0] + btsbids[6][1]*btsbids[6][0] + btsbids[7][1]*btsbids[7][0] + btsbids[8][1]*btsbids[8][0] + btsbids[9][1]*btsbids[9][0])
    bidv2 = btsbids[5][1] + btsbids[6][1] + btsbids[7][1] + btsbids[8][1] + btsbids[9][1]
    bidpv2 = bidpv2/bidv2
    
    bidpv3 = (btsbids[10][1]*btsbids[10][0] + btsbids[11][1]*btsbids[11][0] + btsbids[12][1]*btsbids[12][0] + btsbids[13][1]*btsbids[13][0] + btsbids[14][1]*btsbids[14][0])
    bidv3 = btsbids[10][1] + btsbids[11][1] + btsbids[12][1] + btsbids[13][1] + btsbids[14][1]
    bidpv3 = bidpv3/bidv3

    bidpv4 = (btsbids[15][1]*btsbids[15][0] + btsbids[16][1]*btsbids[16][0] + btsbids[17][1]*btsbids[17][0] + btsbids[18][1]*btsbids[18][0] + btsbids[19][1]*btsbids[19][0])
    bidv4 = btsbids[15][1] + btsbids[16][1] + btsbids[17][1] + btsbids[18][1] + btsbids[19][1]
    bidpv4 = bidpv4/bidv4

    askpv1 = (btsasks[0][1]*btsasks[0][0] + btsasks[1][1]*btsasks[1][0] + btsasks[2][1]*btsasks[2][0] + btsasks[3][1]*btsasks[3][0] + btsasks[4][1]*btsasks[4][0])
    askv1 = btsasks[0][1] + btsasks[1][1] + btsasks[2][1] + btsasks[3][1] + btsasks[4][1]
    askpv1 = askpv1/askv1

    askpv2 = (btsasks[5][1]*btsasks[5][0] + btsasks[6][1]*btsasks[6][0] + btsasks[7][1]*btsasks[7][0] + btsasks[8][1]*btsasks[8][0] + btsasks[9][1]*btsasks[9][0])
    askv2 = btsasks[5][1] + btsasks[6][1] + btsasks[7][1] + btsasks[8][1] + btsasks[9][1]
    askpv2 = askpv2/askv2

    askpv3 = (btsasks[10][1]*btsasks[10][0] + btsasks[11][1]*btsasks[11][0] + btsasks[12][1]*btsasks[12][0] + btsasks[13][1]*btsasks[13][0] + btsasks[14][1]*btsasks[14][0])
    askv3 = btsasks[10][1] + btsasks[11][1] + btsasks[12][1] + btsasks[13][1] + btsasks[14][1]
    askpv3 = askpv3/askv3

    askpv4 = (btsasks[15][1]*btsasks[15][0] + btsasks[16][1]*btsasks[16][0] + btsasks[17][1]*btsasks[17][0] + btsasks[18][1]*btsasks[18][0] + btsasks[19][1]*btsasks[19][0])
    askv4 = btsasks[15][1] + btsasks[16][1] + btsasks[17][1] + btsasks[18][1] + btsasks[19][1]
    askpv4 = askpv4/askv4


#Output: Time Volume last time bid vwap high low ask bid1 bidv1 bid2 bidv2 bid3 bidv3 bid4 bidv4
    Addrow = [int(btstime)] + btstick2 + [bidpv1] + [bidv1] + [bidpv2] + [bidv2] + [bidpv3] + [bidv3] + [bidpv4] + [bidv4] + [askpv1] + [askv1] + [askpv2] + [askv2] + [askpv3] + [askv3] + [askpv4] + [askv4]

    myfile = open('coin.csv', 'a')
    wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
    wr.writerow(Addrow)
    time.sleep(4)

#END OF LOOP
# update every two seconds

