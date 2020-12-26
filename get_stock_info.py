import datetime
import requests
import pymysql
from bs4 import BeautifulSoup

# get html request
url = "https://api.finmindtrade.com/api/v3/data"
parameter = {
    "dataset": "TaiwanStockPriceMinute",
    "stock_id": "2610",
}
# parameter["date"] = datetime.datetime.now().strftime("%Y-%m-%d")
parameter["date"] = "2020-12-23"

data = requests.get(url, params=parameter).json()

# while True:
#     time.sleep(300)  # sleep 5 minute
