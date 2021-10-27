from bs4 import BeautifulSoup
import requests
page = requests.get("http://cybele.ir/")
soup = BeautifulSoup(page.content, 'html.parser')
forecast_items = soup.find(id="back")
print(forecast_items.prettify())
print(forecast_items.get_text())
