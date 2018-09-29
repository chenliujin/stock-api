from conf import conn, cursor 

class deal:

  ##
  # @author: chenliujin <liujin.chen@qq.com>
  # @since:  2018-06-20
  ##

  @staticmethod
  def post(param):

    sql = "INSERT INTO deal(deal_date, stock_code, deal_type, price, quantity, total, stamp_tax, poundage, transfer_fee, sundry_fees, amount, customer_id, status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    fields = ( 
        param['deal_date'],
        param['stock_code'],
        param['deal_type'],
        param['price'],
        param['quantity'],
        param['total'],
        param['stamp_tax'],
        param['poundage'],
        param['transfer_fee'],
        param['sundry_fees'],
        param['amount'],
        param['customer_id'],
        param['status']
    )

    ret = cursor.execute(sql, fields)

    conn.commit()

    return {
      "status": ret
    }