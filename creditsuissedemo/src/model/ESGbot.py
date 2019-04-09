#https://finance.yahoo.com/quote/AAPL/sustainability?p=AAPL

from lxml import html  
import requests
from time import sleep
import json
import argparse
from collections import OrderedDict


def parse(ticker):
	#url = "http://finance.yahoo.com/quote/%s?p=%s"%(ticker,ticker)
	url = "https://finance.yahoo.com/quote/%s/sustainability?p=%s"%(ticker, ticker)
	response = requests.get(url, verify=False)
	print ("Parsing %s"%(url))
	sleep(4)
	parser = html.fromstring(response.text)
	print(parser)
		
if __name__=="__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument('ticker',help = '')
	args = argparser.parse_args()
	ticker = args.ticker
	print ("Fetching data for %s"%(ticker))
	parse(ticker)
	#scraped_data = parse(ticker)
	#print ("Writing data to output file")
	#with open('%s-summary.json'%(ticker),'w') as fp:
#json.dump(scraped_data,fp,indent = 4)