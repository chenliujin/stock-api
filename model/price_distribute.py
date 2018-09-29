from conf import cursor 

class price_distribute:

  @staticmethod
  def index(params):
    where = []
    where_value = []

    if params['stock_code'] :
      where.append('stock_code = %s')
      where_value.append(params['stock_code'])

    if params['status'] :
      where.append('status = %s')
      where_value.append(params['status'])

    sql="SELECT price, SUM(if(deal_type='B', quantity, null)) as B, sum(if(deal_type='S', quantity, null)) as S FROM deal WHERE " + ' AND '.join(where) + " GROUP BY price ORDER BY price";
    cursor.execute(sql, (where_value))
    results = cursor.fetchall()

    data = []

    for result in results: 
      row = {}
      row["price"] = str(result[0])
      row["buy"] = str(result[1])
      row["sale"] = str(result[2])

      data.append(row)

    return data
