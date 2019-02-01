#!/usr/bin/python3
#!/usr/bin/env python

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class priceDistribute(Resource):
  def get(self):
    from model import price_distribute

    parser = reqparse.RequestParser()
    parser.add_argument('stock_code')
    parser.add_argument('start_time')
    parser.add_argument('end_time')
    parser.add_argument('status')

    params =  parser.parse_args()

    result =  price_distribute.index(params)

    return jsonify(result)

class Deal(Resource):

  def post(self):
    from model import deal 

    parser = reqparse.RequestParser()
    parser.add_argument('deal_date')
    parser.add_argument('stock_code')
    parser.add_argument('deal_type')
    parser.add_argument('price')
    parser.add_argument('volume')
    parser.add_argument('total')
    parser.add_argument('stamp_tax')
    parser.add_argument('poundage')
    parser.add_argument('transfer_fee')
    parser.add_argument('sundry_fees')
    parser.add_argument('amount')
    parser.add_argument('customer_id')
    parser.add_argument('status')

    param = parser.parse_args()

    ret = deal.post(param)

    return jsonify({})


api.add_resource(priceDistribute, '/v1/stock/price_distribute/')
api.add_resource(Deal, '/v1/stock/deal/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)


