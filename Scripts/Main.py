from TradeGenerator import *


t = TradeGenerator()
tList = t.prepareTradeList(2)
df = t.tradeListConvert2DataFrame(tList)
print ("output:")
print(df.head())