from bs4 import BeautifulSoup
import requests
url ="https://www.flipkart.com/realme-xt-pearl-blue-64-gb/p/itm731360fdbd273?pid=MOBFJYBE9FHXFEFJ&lid=LSTMOBFJYBE9FHXFEFJNVQVIV&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=2cb30593-8761-40ba-9059-d9534d86829d.MOBFJYBE9FHXFEFJ.SEARCH&ppt=sp&ppn=sp&ssid=rfvywlv88g0000001600754465925&qH=32048be54ef1204f"

req_data=requests.get(url)#we request a data to get url


