# BITCOIN TO USD OR GBP

# this script scrapes a website to get the value of bitcoin and another website to convert currencies.

import requests
from bs4 import BeautifulSoup as bs
from function import convert_to_gbp, time

# urls of website we are scraping
bitcoin_url = requests.get("https://www.coindesk.com/price/bitcoin") # website return bitcoin worth to USD
currency_url = requests.get("https://transferwise.com/gb/currency-converter/usd-to-gbp-rate?amount=1") # USD to GBP currency website

# convert bitcoin website to a beautifulsoup object/varaible
soup = bs(bitcoin_url.content, "html.parser")
# convert currency website to a beautifulsoup object/varaible
soup2 = bs(currency_url.content, "html.parser")

#------ extracting price of bitcoin
# find div tag that contains class="price-large" (we price is located)
price = soup.find('div', attrs={'class': 'price-large'})
# price = (<div class="price-large"><span class="symbol">$</span>32,107.94</div>)

# we want the string value of price (within the div tag)
# for every item in price
for item in price:
    bitcoin_to_usd = (item.string) #all string values inside price variable (div tag)

# to convert to a float we have to remove the comma
bitcoin_to_usd = bitcoin_to_usd.replace(",", "")
bitcoin_to_usd = float(bitcoin_to_usd)

#------ extracting currency conversion
# find span element containing class='text-success'
gbp = soup2.find('span', attrs={'class': 'text-success'})

# only returning the string inside the span tag but converting to a float (for calculations)
usd_to_gbp = float(gbp.string)

#------ user input/output
while True:

    options = input("""
        BITCOIN VALUE CHECKER

        - Enter "1" for Bitcoin to USD
        - Enter "2" for Bitcoin to GBP
        - Enter "3" for USD to GBP
        - Enter "Q" to Quit

    """).upper()

    if options == "1":
        print(f"""
        Current Date & Time: {time()},

        > 1 bitcoin = ${bitcoin_to_usd}


        """)


    elif options == "2":
        print(f"""
        Current Date & Time: {time()},

        > 1 bitcoin = £{convert_to_gbp(bitcoin_to_usd, usd_to_gbp)}


        """)

    elif options == "3":
        print(f"""
        Current Date & Time: {time()},

        According to TranferWise.com
        Mid-market exchange rate:

        > 1 USD = {usd_to_gbp} GBP


        """)

    elif options == "Q":
        print()
        print("""
        See you soon...
        """)
        break

    else:
        print()
        print("Value Incorrect.")
