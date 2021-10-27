from bs4 import BeautifulSoup
import requests
import time
oldapartment=" "

def scroll():
	print("scroll")
	return

while True:
	page = requests.get("https://divar.ir/s/tehran/buy-apartment")
	soup = BeautifulSoup(page.content, 'html.parser')
	home_items = soup.find_all(class_="post-card-item kt-col-6 kt-col-xxl-4")
	for newapartment in home_items:
		if  'جنت آباد' in newapartment.get_text():
			if oldapartment!=newapartment.get_text():
				print(newapartment.get_text())
				oldapartment=newapartment.get_text()
	# scroll()
	time.sleep(20)
