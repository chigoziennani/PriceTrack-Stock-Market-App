# PriceTrack - Stock Market Analysis Tool

This repository contains all the files for a full-stack web application that fetches and visualizes real-time and historical stock market data. The application was developed using Flask and Python for the back-end, with Plotly.js handling the front-end visualizations. The data is sourced from the Yahoo Finance API using the `yfinance` library. Below is a breakdown of the features and techniques involved in the project.

## Real-time Stock Data Retrieval
**Goal**: Fetch live stock market data from Yahoo Finance  
**Algorithms/Techniques In Focus**: API integration, JSON serialization

**Description**: The app retrieves real-time and intraday stock data using the Yahoo Finance API (`yfinance`). It allows users to input any stock symbol (e.g., AAPL for Apple, TSLA for Tesla) and fetch the latest price data, including high, low, and close prices over the last 24 hours.

## Dynamic Data Visualization
**Goal**: Visualize stock price movements with interactive charts  
**Technologies**: Plotly.js, JavaScript

**Description**: The stock price data is visualized in an interactive line chart using Plotly.js. Users can view the historical stock price at different time intervals, including the open, close, high, and low prices for the day. The chart updates dynamically based on user input and is rendered without requiring a page refresh, thanks to JavaScript and the Fetch API.

## Financial Metrics Display
**Goal**: Display relevant financial data for each stock  
**Technologies**: Python (Flask), yfinance

**Description**: For each stock, the app displays the company's market capitalization and P/E ratio, retrieved via the Yahoo Finance API. The app handles missing or unavailable data by providing default values (e.g., "N/A").

## Stock Data Retrieval and API Integration
**Goal**: Use the Yahoo Finance API (`yfinance`) to fetch intraday stock data  
**Description**: The app uses the `yfinance` library to pull stock data for any user-entered stock symbol. It retrieves various financial metrics such as market capitalization, P/E ratio, and real-time price movements. The data is returned in JSON format and processed on the front-end for visualization.

## Interactive Stock Charts with Plotly.js
**Goal**: Implement interactive stock price charts using Plotly.js  
**Description**: Plotly.js is used to create interactive line charts that plot the stock's intraday prices, including the high, low, and close prices. The charts update dynamically whenever the user submits a new stock symbol. Users can hover over the chart to see detailed information about the stock's price at specific timestamps.

## Front-End and Back-End Integration
**Goal**: Use Flask to manage the back-end and Fetch API for seamless front-end integration  
**Description**: The Flask framework powers the back-end, handling requests for stock data. The front-end uses HTML/CSS and JavaScript, with asynchronous requests sent via the Fetch API to retrieve stock data from the server. This architecture allows the app to update the displayed stock information and charts without refreshing the page, providing a smooth user experience.

## Technologies and Tools Used

**Languages & Web Technologies**:  
- Python (Flask, yfinance)  
- JavaScript (Plotly.js, Fetch API)  
- HTML/CSS
  
**Developer Tools**:  
- Git/GitHub  
- Visual Studio Code  
- Chrome DevTools
  
## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-market-app.git
   cd stock-market-app
2. Install dependencies:
   ```bash
   pip install Flask
   pip install yfinance
   pip install pandas
   pip install plotly
3. Run the Flask app:
   ```bash
   python stock_web_app.py
4. Open your browser and visit:
   ```arduino
   http://127.0.0.1:5000

## Future Enhancements
- Multiple Stock Comparison: Add functionality to compare multiple stocks on the same chart.
- User Authentication: Implement a user login system for saving and tracking favorite stocks.
- Extended Time Frames: Add options for viewing stock data over longer periods (e.g., weekly, monthly).
