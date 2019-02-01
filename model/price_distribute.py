from conf import cursor 
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

    url = 'http://www.chenliujin.com/kylin/api/query'

    auth=('ADMIN', 'KYLIN')

    headers = {
      "Content-Type": "application/json;charset=UTF-8"
    }
    
    data = {
      "sql": "SELECT customer_id, stock_code, price, deal_type, SUM(volume) AS volume FROM deal WHERE " + ' AND '.join(where) + " GROUP BY customer_id, stock_code, price, deal_type ORDER BY price ASC",
      "offset": 0,
      "limit": 50000,
      "acceptPartial": False,
      "project": "stock",
    }

    r = requests.post(url, headers=headers, auth=auth, data=json.dumps(data))

    if r.status_code != 200 :
      logging.critical('kylin error')
      return []
    
    results = r.json()['results']

    data = {}

    for result in results: 
      if result[2] in data:
        data[result[2]][result[3]] = result[4]
      else:
        data[result[2]] = {'price': result[2], result[3]: result[4]}

    data2 = []

    for key in data:
      data2.append(data[key])

    data2 = sorted(data2, key=lambda data2:Decimal(data2['price']))

    return data2
