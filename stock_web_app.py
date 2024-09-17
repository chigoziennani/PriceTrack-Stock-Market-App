"""My first attempt to create a stock market app using Flask and yfinance.
This is a full-stack web application that fetches stock data from Yahoo Finance and displays it in a simple line chart.
The app uses Flask to serve the front-end and back-end, and yfinance to fetch stock data.
The app fetches intraday stock data for a given stock symbol and displays it in a line chart.
The app also displays the company name, market capitalization, and P/E ratio.
The app uses the Jinja templating engine to render the front-end and AJAX to fetch stock data from the back-end.
The app uses the Chart.js library to display the line chart. The app uses the Bootstrap library for styling.
The app uses the yfinance library to fetch stock data from Yahoo Finance. The app uses the Flask library to serve the front-end and back-end.
The app uses the request library to fetch data from the front-end. The app uses the jsonify function to return JSON data to the front-end.
The app uses the render_template function to render the front-end. The app uses the Ticker class from yfinance to fetch stock data."""

from flask import Flask, render_template, request, jsonify
import yfinance as yf

app = Flask(__name__)

# fetch stock data from yahoo finance using yfinance
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    
    # fetch intraday history
    hist = stock.history(period="1d", interval="5m")
    
    if not hist.empty:
        # prepare data for front-end use
        times = hist.index.strftime("%Y-%m-%d %H:%M:%S").tolist()  # format dates as strings
        prices = hist['Close'].tolist()  # get closing prices
        highs = hist['High'].tolist()    # get high prices
        lows = hist['Low'].tolist()      # get low prices
        volume = hist['Volume'].tolist() # get volume
        
        # get company info
        info = stock.info
        market_cap = info.get("marketCap", "N/A")  # default to "N/A" if data is not available
        pe_ratio = info.get("trailingPE", "N/A")   # default to "N/A"
        name = info.get("shortName", symbol)       # default to stock symbol if name is not available

        # return multiple sets of data for the front-end
        return {
            "times": times,
            "prices": prices,
            "highs": highs,
            "lows": lows,
            "volume": volume,
            "name": name,
            "market_cap": market_cap,
            "pe_ratio": pe_ratio
        }
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock', methods=['POST'])
def stock():
    symbol = request.form['symbol']
    data = get_stock_data(symbol)
    
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Error fetching stock data. Please check the stock symbol and try again."})

if __name__ == '__main__':
    app.run(debug=True)