import requests
import pymysql
import sys

# get html request
url = "https://api.finmindtrade.com/api/v3/data"
parameter = {
    "dataset": "TaiwanStockPrice",
    "stock_id": sys.argv[1],
}
parameter["date"] = sys.argv[2]

data = requests.get(url, params=parameter).json()["data"]

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "<your account>",
    "password": "your password",
    "db": "your data base name",
    "charset": "utf8"
}

try:
    conn = pymysql.connect(**db_settings)
    with conn.cursor() as cursor:
        command = "INSERT INTO <table>(columns) VALUES (values)"
        cursor.execute(command, ())  # secand parameter is columns value
        conn.commit()
except Exception as e:
    print(e)
