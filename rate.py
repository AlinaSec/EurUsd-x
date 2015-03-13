# -*- coding: utf-8 -*-
import requests
import re
import time
import sys
if __name__ == "__main__":
	headers = {'Host':'query.yahooapis.com',
				'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0',
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language':'en-US,en;q=0.5',
				'Accept-Encoding':'gzip, deflate',
				'Connection':'keep-alive'
				}

	url='http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20%28%22EURUSD%22%29&env=store://datatables.org/alltableswithkeys'
	old_rate=''
	while 1==1:
	
		try:
			r = requests.get(url,headers=headers)
			content=r.content
			rate=re.findall(r'<Rate>(.*?)</Rate>',content.replace('\n','').replace('\t',''))			
			#sys.stdout.write(rate[0] + ' ')
			if rate[0]!=old_rate:
				print rate[0]
			time.sleep(15)
			old_rate=rate[0]
		except Exception as e:
			# print e
			time.sleep(10)
			pass
			
	
	
