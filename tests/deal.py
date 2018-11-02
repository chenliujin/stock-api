#!/bin/python

import csv
import requests

def check_stock_code(stock_code):
  if len(stock_code) < 6:
    stock_code = '0' + stock_code

    return check_stock_code(stock_code)
  else:
    return stock_code

def import_deal(file):
  with open(file, 'r', encoding="utf-8") as fp:
    rows = csv.reader(fp)
    print(rows)

    for row in rows:
      if row[1] == '证券买入':
        deal_type = 'B'
      elif row[1] == '证券卖出':
        deal_type = 'S'
      else:
        #print(row)
        continue
      
      param = {
        'deal_date': row[0],
        'stock_code': check_stock_code(row[14]),
        'deal_type': deal_type,
        'price': row[5],
        'volume': row[4],
        'total': row[6],
        'stamp_tax': row[8],
        'poundage': row[7],
        'transfer_fee': 0,
        'sundry_fees': row[9],
        'amount': row[10],
        'customer_id': 1,
        'status': 0
      }

      ret = requests.post('http://stock.chenliujin.com/v1/stock/deal/', param);

      # print(param)
      print(ret)


files = [
  # "/root/s-api/tests/2015.csv", 
  # "/root/s-api/tests/2016Q1.csv", 
  # "/root/s-api/tests/2016Q2.csv", 
  # "/root/s-api/tests/2016Q3.csv", 
  # "/root/s-api/tests/2016Q4.csv", 
  # "/root/s-api/tests/2017.csv", 
  # "/root/s-api/tests/2018Q1.csv", 
  # "/root/s-api/tests/2018Q2.csv",
  # "/root/s-api/tests/20180701-20180704.csv"
  # "/root/s-api/tests/20180705-20180716.csv"
  #"/root/s-api/tests/20180717-20180814.csv"
  #"/root/s-api/tests/20180815-20180821.csv"
  #"/root/s-api/tests/20180822-20180910.csv"
  #"/root/s-api/tests/20180911-20180924.csv"
  "/root/stock-api/tests/20180925-20181101.csv"
]

for file in files:
  import_deal(file)


