# B1: lấy DS ngày nghỉ từ API của VND
# B2: In ra ngày nghỉ
# B3: check ngày hiện tại với ngày nghỉ
# B4: nếu ngày hiện hiện tại là ngày nghỉ => break; nếu không phải ngày nghỉ => B5
# B5: lấy DS ngày GD từ API của VND tiếp theo theo ngày hôm nay
# B6: lấy ngày GD tiếp theo lưu lại

from ast import Return, main
import datetime
from dateutil.relativedelta import relativedelta
import pendulum
import requests
import json
import numpy

x = datetime.datetime.now()
day = x.strftime("%A")
date = x.strftime("%d")

now = pendulum.now()
dates = now.to_date_string()
# dates = "2022-09-02"

day_off = []
nexttranday = ""

# lấy DS ngày nghỉ từ API
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

# get data DS nghỉ từ API
response_holiday = requests.request("GET", url, headers=headers, data=payload)
data_holiday = json.loads(response_holiday.text)
jsondata_holiday = data_holiday["data"]

# lấy DS ngày nghỉ từ list Data    
for index, items in enumerate(jsondata_holiday):
    day_off.append(str(items["date"]))

# Check ngày hôm nay với DS ngày nghỉ
def next_tranday():
    dayoff_exist = dates in day_off
    if dayoff_exist == True:
        dayoff = None
        return dayoff
    else: # lấy DS ngày tiếp theo từ API
        url = "https://finfo-api.vndirect.com.vn/v4/trading_calendars?sort=date:asc&q=holiday:false~date:gte:{}&size=2".format(dates)
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
    
    response_nonholiday = requests.request("GET", url, headers=headers, data=payload)
    data_nonholiday = json.loads(response_nonholiday.text)
    jsondata_nonholiday = data_nonholiday["data"]
    global nexttranday
    
    for index, item in enumerate(jsondata_nonholiday):
        if dates != item["date"]:
            nexttranday = (str(item["date"]))
            # print(nexttranday)
            return nexttranday
        
next_tranday()
