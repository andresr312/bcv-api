# scrapper for https://www.bcv.org.ve/ getting the exchange rate for USD

import requests
from bs4 import BeautifulSoup

def get_exchange_rate():
    """Get the exchange rate for USD from https://bcv.org.ve"""
    url = "https://bcv.org.ve"
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    div_dolar = soup.find(id='dolar')
    div_amount = div_dolar.find_all(class_="col-sm-6 col-xs-6 centrado")[0].get_text()
    format_amount = round(float(div_amount.strip().replace(",",".")), 2)
    return format_amount

if __name__ == "__main__":
    print(get_exchange_rate())
    