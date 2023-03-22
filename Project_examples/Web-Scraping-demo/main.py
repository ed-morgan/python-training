import requests
import pandas
import numpy
from bs4 import BeautifulSoup

import processing as p

result = requests.get("https://www.ukfinance.org.uk/data-and-research/data/business-finance-review")
content = result.content

soup = BeautifulSoup(content)

archivedData = soup.find("ul", "documents__list")

archivedList = archivedData.ul.find_all("li")

alreadyProcessData = pandas.read_csv("Data/ReviewData.csv")


for li in archivedList:

    processed = False

    for alreadyRead in alreadyProcessData.iloc:

        if li.text == alreadyRead.values[0]:
            print(f"Already read this pdf: {li.text}")
            processed = True
            break
    
    if not processed:
        print(f"Need to process: {li.text}")
        p.download_pdf(li.a["href"], li.text + ".pdf")
        p.add_data_to_tracker("Q2 2022")