from calendar import weekday
import datetime
from dateutil.relativedelta import relativedelta
import pendulum
import requests
import json

x = datetime.datetime.now()
day = x.strftime("%A")
date = x.strftime("%d")
t6 = "Friday"
weekend = ["Saturday", "Sunday"]

now = pendulum.now()
dates = now.to_date_string()
url = "https://finfo-api.vndirect.com.vn/v4/trading_calendars?sort=date:asc&q=holiday:true~date:gte:2022-01-01&size=365"
payload={}
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Origin': 'https://dstock.vndirect.com.vn',
  'Pragma': 'no-cache',
  'Referer': 'https://dstock.vndirect.com.vn/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

daaa = "2023-01-01"

response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)
jsondata = data["data"]
for index, items in enumerate(jsondata):
    dayweek = items["endDayOfWeek"]
    date_holiday = str(items["date"])
    if dayweek == True:
        print(items["date"])
        
if daaa in date_holiday:
    print("Day off")
else:
    print("no day off")        

# print(now.day_of_week)
# print(x)
# print(Day)
# print(Weekend)
# print(type(Weekend))

# if day in weekend:
#     print("have day off")
# else:
#     print("no")
