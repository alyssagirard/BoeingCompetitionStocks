# https://www.npr.org/2024/03/20/1239132703/boeing-timeline-737-max-9-controversy-door-plug
# https://www.dailymail.co.uk/news/article-13198157/boeing-airlines-dont-fly-737-jets-fears-site-booking.html
# https://www.forbes.com/sites/marisagarcia/2024/03/11/faa-issues-new-warning-of-wiring-issue-on-737-max-wing-spoilers/?sh=6a5c12ad6d97
import yfinance as yf

tickers_list = ['EADSY', 'DAL', 'JBLU']

# 30k each, 10k left

start_date = "2024-03-18"
end_date = "2024-09-30"

for ticker in tickers_list:
    data = yf.download(ticker, start=start_date, end=end_date)

    close_price = data['Close']
    open_price = data['Open']

    print(f"Stock: {ticker}")
    print(f"Open Price: ${open_price}")
    print(f"Close Price: ${close_price}")

    start_date = "2024-03-18"
    end_date = "2024-03-19"
    data = yf.download(ticker, start=start_date, end=end_date)
    low_price = data['Low']
    print(f"Stock: {ticker}")
    print(f"Low Price: ${low_price}")
    start_date = "2024-03-18"
    end_date = "2024-03-19"
    data = yf.download(ticker, start=start_date, end=end_date)
    low_price = data['Low']
    print(f"Stock: {ticker}")
    print(f"Low Price 3/20: ${low_price}")

    start_date = "2024-03-22"
    end_date = "2024-03-23"
    data = yf.download(ticker, start=start_date, end=end_date)
    high_price = data['High']
    print(f"Stock: {ticker}")
    print(f"High Price 3/22: ${high_price}")

    data = yf.download(ticker, start=start_date, end=end_date, interval="15m")
    close_price = data['Close']
    print(f"Stock: {ticker}")
    print(f"Price by 15 min start date: ${close_price}")

    print("\n")
