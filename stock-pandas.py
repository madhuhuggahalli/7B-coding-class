import numpy
import pandas
import matplotlib.pyplot as plt
import pandas_datareader as web

names = ['aapl', 'goog', 'msft', 'dis', 'xom', 'fb', 'pnra']
def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)['Adj Close']
#put the stock prices in a pandas dataframe
px = pandas.DataFrame({n: get_px(n, '1/1/2010', '1/1/2017') for n in names})
px = px.asfreq('B').fillna(method='pad')

px.plot()
plt.show()

#create a dataframe of percent changes
rets = px.pct_change(1)
cumrets = ((1 + rets).cumprod() - 1)

rets.plot()
plt.show()
#((1 + rets).cumprod() - 1).plot()
cumrets.plot()
plt.show()
#gr1.plot(((1 + rets).cumprod() - 1))
#gr2.plot(rets)

#success
ticker = raw_input('ticker? ')
cumrets[ticker].plot()
rets[ticker].plot()
plt.show()


# fig = plt.figure()
# gr1 = fig.add_subplot(2,2,1)
# gr2 = fig.add_subplot(2,2,2)
# gr3 = fig.add_subplot(2,2,3)
# gr4 = fig.add_subplot(2,2,4)

# def single_series(collection, name):
#     df = collection[name]
#     return df
#success
# stock = pandas.DataFrame(single_series(rets,'fb'))
# stock.plot()
# plt.show()
# stockret = ((1 + stock).cumprod() - 1)
# stockret.plot()
# plt.show()




