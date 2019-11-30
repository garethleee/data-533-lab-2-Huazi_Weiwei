import sub_package2.plotStock as pls
import sub_package2.plotBalance as plb


if __name__ == "__main__":
    filepath1 = 'BABA.csv'
    stock_plot = pls.PlotStock(filepath1)
    stock_plot.plot()

    filepath2 = 'BABA_balance.csv'
    balance_plot = plb.plotBalance(filepath2)
    balance_plot.plot()
