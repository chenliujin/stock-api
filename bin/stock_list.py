#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import traceback
import re
import time


#获得所需的网页源代码
def getHTMLText(url):
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def getFileName():
    dirname = time.strftime('%Y%m%d',time.localtime(time.time()))
    dirname+='sh'
    return  dirname
    
    

# 东方财富网
def getStockList(): 
  stock_list = []

  html = getHTMLText('http://quote.eastmoney.com/stocklist.html')
  soup = BeautifulSoup(html, 'html.parser')
  a = soup.find_all('a')

  for link in a:
    try:
      code = re.findall(r"s[zh]\d{6}", link.attrs['href'])[0]
      stock_code = re.sub(r"s[zh]", '', code)

      stock = {
        'stock_code': stock_code,
        'stock_name': re.sub(r"\("+ stock_code +"\)", '', link.string)
      # '类型': 'sh上海证券/sz深圳证券'
      }

      stock_list.append(stock)
    except:
      continue

  return stock_list


def getStockInfo(lst, fpath):
  ndate = time.strftime('%Y%m%d',time.localtime(time.time()))

  for stock in lst:
      url = 'http://gupiao.baidu.com/stock/' + stock + '.html' # 拼接url
      html = getHTMLText(url)
      try:
          if html == "":
              continue
          infoDict = {}
          soup = BeautifulSoup(html, 'html.parser')
          stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
          if stockInfo == None:  # 判断为空，返回
              continue
          # print(stockInfo)
          # name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
          # print(name)
          #infoDict.update({'股票编码':stock})
          #inp=name.text.split()[0]+":"
          keyList = stockInfo.find_all('dt')
          valueList = stockInfo.find_all('dd')
          inp=stock+ndate+","+stock+","+ndate+","
          for i in range(len(keyList)):
              key = keyList[i].text
              val = valueList[i].text
              infoDict[key] = val
          #print(inp)
          inp+=infoDict['最高']+","+infoDict['换手率']+","+infoDict['成交量']+","+infoDict['成交额']+"\n"
          print(inp)
          with open(fpath, 'a', encoding='utf-8') as f:
              
              #f.write(str(infoDict) + '\n')
              f.write(inp)
      except:
          traceback.print_exc()
          continue



def main(): # 主方法调用上面的函数
    output_file = './'+getFileName()+'.txt'
    rs = getStockList()

    print(rs)
    #getStockInfo(slist, output_file)


main()
