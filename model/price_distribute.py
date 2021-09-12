from conf import conn, cursor 
from decimal import *
import requests
import json
import logging

logging.basicConfig(
  level=logging.INFO,
  filename='/var/log/stock-api.log'
)

class price_distribute:

  @staticmethod
  def index(params):
    where = []
    where_value = []

    where.append('customer_id = 1')

    if params['stock_code'] :
      where.append("stock_code = '" + params['stock_code'] + "'")

    if params['status'] :
      where.append('status = ' + params['status'])

    if params['start_time'] :
      where.append("deal_date >= '" + params['start_time'] + "'")

    if params['end_time'] :
      where.append("deal_date <= '" + params['end_time'] + "'")

    sql = "SELECT price, deal_type, sum(volume) FROM deal WHERE " + " AND ".join(where) + " GROUP BY price, deal_type"

    conn.ping(reconnect=True)

    ret = cursor.execute(sql)

    results = cursor.fetchall()

    #if r.status_code != 200 :
      #logging.critical('kylin error')
      #return []
    

    data = {}

    for result in results: 
      if result[0] in data:
        data[result[0]][result[1]] = result[2]
      else:
        data[result[0]] = {'price': result[0], result[1]: result[2]}

    data2 = []

    for key in data:
      data2.append(data[key])

    data2 = sorted(data2, key=lambda data2:Decimal(data2['price']))

    return data2
