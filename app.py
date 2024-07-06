import streamlit as st
import streamlit.components.v1 as components

# List of top 10 Indian stocks
indian_stocks = {
    "Reliance Industries": "NSE:RELIANCE",
    "Tata Consultancy Services": "NSE:TCS",
    "HDFC Bank": "NSE:HDFCBANK",
    "Infosys": "NSE:INFY",
    "Hindustan Unilever": "NSE:HINDUNILVR",
    "ICICI Bank": "NSE:ICICIBANK",
    "State Bank of India": "NSE:SBIN",
    "Bharti Airtel": "NSE:BHARTIARTL",
    "Kotak Mahindra Bank": "NSE:KOTAKBANK",
    "Bajaj Finance": "NSE:BAJFINANCE"
}

# Streamlit app title
st.title("Top 10 Indian Stocks TradingView Chart")

# Dropdown menu for selecting a stock
selected_stock = st.selectbox("Select a stock to view its chart:", list(indian_stocks.keys()))

# Get the symbol for the selected stock
symbol = indian_stocks[selected_stock]

# HTML code for the TradingView widget
tradingview_widget = f"""
<div id="tradingview_chart"></div>
<script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
<script type="text/javascript">
    new TradingView.widget({{
        "width": "100%",
        "height": 610,
        "symbol": "{symbol}",
        "interval": "D",
        "timezone": "Etc/UTC",
        "theme": "light",
        "style": "1",
        "locale": "en",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_chart"
    }});
</script>
"""

# Display the TradingView widget in the Streamlit app
components.html(tradingview_widget, height=650)
