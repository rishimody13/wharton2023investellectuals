import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from yahoo_fin import stock_info as si
# Define the list of stocks to collect data for


stocks = ['SPY', 'IVV', 'VOO', 'VTI', 'QQQ', 'VTV', 'VUG', 'IWF', 'VIG', 'IJH', 'IJR']

#stocks = ['AAPL', 'TSLA', 'MSFT', 'GOOGL','NVDA', 'META', 'NFLX', 'INTC', 'AMZN'] # Insert list of symbols to analyze





# Create an empty dataframe to store the data
stock_data = pd.DataFrame(columns=['Stock', 'Price', 'Momentum','PE Ratio'])

# Loop through each stock and collect the data
for stock in stocks:
   
    #Collect data using yfinance
    stock_price = yf.Ticker(stock).history(period="1d")["Close"][0]
    historical_data = yf.Ticker(stock).history(period="1y")
    start_price = historical_data["Close"][0]
    end_price = historical_data["Close"][-1]
    momentum = end_price - start_price
    # momentum = stock_info['momentum']
    # market_cap = (stock_info['marketCap'])/1000000000
    
    pe_ratio = si.get_quote_table(stock)["PE Ratio (TTM)"]
    # current_price = yf.Ticker(stock).history(period="1d")["Close"][0]
    # # Estimate the EPS using historical data (e.g., last 4 quarters)
    # historical_data = yf.Ticker(stock).history(period="1y")
    # average_earnings = historical_data["Close"].mean()
    # # Calculate the P/E ratio
    # pe_ratio = current_price / average_earnings
    

    

    # Add the data to the dataframe
    
    stock_data = stock_data.append({'Stock': stock, 'Price': stock_price,  'Momentum': momentum, 'PE Ratio': pe_ratio}, ignore_index=True)
# 'PE Ratio': pe_ratio
# 'Market Cap (Billions)': market_cap
       
# Export the data to an excel sheet
stock_data.to_excel('stockdata.xlsx', index=False)

#GRAPHING

# Generate a graph of the stock price over 5 months for each stock
def fivemonthpricechange():
    for stock in stocks:
        # Collect the data using yfinance
        stock_df = yf.download(stock, period='5mo', interval='1d')
        
        # Plot the data
        plt.plot(stock_df['Close'], label=stock)
        
    # Add labels and legend to the graph
    plt.title('Stock Price over 5 Months')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()

    # Show the graph
    plt.show()


#generate graphs for percentage change
def sixmonthpercentagechange():
    for stock in stocks:
        # Collect the data using yfinance
        stock_df = yf.download(stock, period='6mo', interval='1d')
        
        # Calculate the percentage change
        stock_df['Percentage Change'] = (stock_df['Close'] - stock_df['Close'].iloc[0]) / stock_df['Close'].iloc[0] * 100
        
        # Plot the percentage change
        plt.plot(stock_df.index, stock_df['Percentage Change'], label=stock)

    # Add labels and legend to the graph
    plt.title('Percentage Price Change Over 6 months')
    plt.xlabel('Date')
    plt.ylabel('Percentage Change')
    plt.legend()

    # Show the graph
    plt.show()
