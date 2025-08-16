import yfinance as yf # pandas e request já estão importados nessa biblioteca

ticker = yf.Ticker("GC=F")

df = ticker.history(period="1d", interval="1m")[['Close']]

print(df.tail())