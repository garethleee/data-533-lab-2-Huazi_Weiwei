import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


class PlotStock:
    """
    class for reading stock data and plot it.
    """
    def __init__(self, filePath):
        """
        get file path for the stock data.
        """
        self.filePath = filePath

    def readData(self):
        """
        read stock data, and return the DataFrame type for this data.
        :return:
        """
        stockData = pd.read_csv(self.filePath)
        stockData['Date'] = pd.to_datetime(stockData['Date'])  # transfer string date to pandas Date type
        stockData = stockData.sort_values(['Date'])  # sort the data by date ascending order

        return stockData

    def plot(self):
        data = self.readData()  # get data
        try:
            # check if Open, Highest, Lowest, Adj_close exsit in data.columns
            stock_info = {'Open', 'High', 'Low', 'Adj Close'}
            is_subset = stock_info.issubset(set(data.columns.tolist()))

            # plot stock data
            fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                                 open=data['Open'],
                                                 high=data['High'],
                                                 low=data['Low'],
                                                 close=data['Adj Close'])])
            fig.show()
            #         plt.figure(figsize=(15, 5))
            #         plt.plot(data['Date'], data['Open'], label='Open')
            #         plt.plot(data['Date'], data['High'], label='High')
            #         plt.plot(data['Date'], data['Low'], label='Close')
            #         plt.plot(data['Date'], data['Adj Close'], label='AdjClose')
            #         plt.legend()
            #         plt.xlabel('time')
            #         plt.ylabel('stock price')
            #         plt.title('stock trend')

            #         plt.show()
        except:
            print('"{}" is Error data'.format(self.filePath))

