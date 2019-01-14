#!/bin/bash

sqoop import \
  --connect jdbc:mysql://mysql.chenliujin.com/stock?tinyInt1isBit=false \
  --username root \
  --password chenliujin \
  --table deal \
  --columns 'deal_id, customer_id, stock_code, deal_type, price, volume, total, stamp_tax, poundage, transfer_fee, sundry_fees, amount, status, date_added, last_modified' \
  --where 'deal_date = "'$1'"' \
  -m 1 \
  --direct \
  --hive-import \
  --hive-overwrite \
  --hive-database olap_stock \
  --hive-table deal \
  --hive-partition-key deal_date \
  --hive-partition-value $1 \
  --delete-target-dir 
