from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = 'LNQVKBRSPNOY2252'

class StockPortfolio:
    def __init__(self):
        self.stocks = {}  

    def add_stock(self, symbol):
        if symbol in self.stocks:
            print(f"{symbol} is already in the portfolio.")
        else:
            self.stocks[symbol] = self.get_stock_info(symbol)
            print(f"{symbol} added to the portfolio.")

    def remove_stock(self, symbol):
        
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"{symbol} removed from the portfolio.")
        else:
            print(f"{symbol} is not in the portfolio.")

    def get_stock_info(self, symbol):
        ts = TimeSeries(key=API_KEY, output_format='json')
        data, _ = ts.get_quote_endpoint(symbol=symbol)
        return data

    def plot_portfolio_performance(self):
        if not self.stocks:
            print("No stocks in the portfolio.")
            return

        plt.figure(figsize=(10, 6))
        for symbol, stock_info in self.stocks.items():
            current_price = float(stock_info['05. price'])
            plt.bar(symbol, current_price, label=symbol)
        plt.title("Real-Time Stock Prices")
        plt.xlabel("Stock Symbol")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.show()

    def display_portfolio(self):
        print("Stock Portfolio:")
        for symbol, stock_info in self.stocks.items():
            print(f"{symbol}: {stock_info['05. price']} USD")


if __name__ == "__main__":
    portfolio = StockPortfolio()

    # Examples 
    portfolio.add_stock('AAPL')  
    portfolio.add_stock('MSFT')  
    portfolio.add_stock('GOOGL')  
    portfolio.add_stock('AMZN') 
    portfolio.add_stock('TSLA')  
    portfolio.add_stock('FB') 

    portfolio.display_portfolio()  
    portfolio.plot_portfolio_performance()  
