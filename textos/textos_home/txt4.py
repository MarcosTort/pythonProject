from bs4 import BeautifulSoup
import requests

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://www.somniosoftware.com")
# assert driver.title == 'Somnio Software | Flutter App & Web Development Company'
r = requests.get('http://www.somniosoftware.com')
soup = BeautifulSoup(r.text, 'lxml')
res = soup.find_all("p")
lista = []
for c in res:
    print(c.string)
    lista.append(c.string)


