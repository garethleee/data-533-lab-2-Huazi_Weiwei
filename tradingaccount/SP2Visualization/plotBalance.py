from plotStock import *
import plotStock


class plotBalance(plotStock.PlotStock):
    """
    class for reading stock balance data and plot it.
    """

    def __init__(self, filePath):
        super(plotBalance, self).__init__(filePath)

    def plot(self):
        data = self.readData()  # get data
        try:
            # check if Open, Highest, Lowest, Adj_close exsit in data.columns
            stock_info = {'Open', 'High', 'Low', 'Adj Close', 'balance'}
            is_subset = stock_info.issubset(set(data.columns.tolist()))

            # plot stock data and the balance
            plt.plot(data['Date'], data['balance'])
            plt.xlabel('time')
            plt.ylabel('$')
            plt.title('balance against time')
            plt.show()

            # fig = go.Figure(data=[go.Candlestick(x=data['Date'],
            #                                      balance=data['balance'])])
            # fig.show()

        except:
            print('"{}" is Error data'.format(self.filePath))
