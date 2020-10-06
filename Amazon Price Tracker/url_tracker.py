import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/realme-RMA108-Realme-Buds-Wireless/dp/B07XJWTYM2/ref=sr_1_1?dchild=1&keywords=realme+wireless+earphones&qid=1589532606&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def check_price():
    page = requests.get(url, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()

    title = title.strip()
    price = price[2:].split(',')
    price = float("".join(price))

    expected = int(input('What price are you expecting? (in INR)\n'))
    if(price <= expected):
        print("The current price of " + title + " is Rs " + str(price))
        print(f"You can buy the product at:\n{url}")
    else:
        print("Sorry the price didn't fell down.")
        print("The current price of " + title + " is Rs " + str(price))

if __name__ == '__main__':
    check_price()
