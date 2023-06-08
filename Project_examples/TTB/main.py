# Imports pypi libaries
import time
from bs4 import BeautifulSoup

#Imports from local files
from utils import download_pdf, extract_pdf, retrieve_webpage, transform_into_soup


'''
Search URL for the top level webpage we want to scrape
We may eventually want to turn this into a parameter we can run with the script so this is customisable
e.g python main.py www.example.com

Use retrieve_webpage from util.py to grab the html structure of the webpage
'''
searchURL = "https://www.ttb.gov/statistics/ttb-beer-2022-statistics"
content = retrieve_webpage(searchURL)

'''
use transform_into_soup from utils.py to turn the content into a soup which is done by beatiful soup. We can then use this soup to search the HTML structure of the webpage
'''
soup = transform_into_soup(content)

'''
Using the soup we can search for the specific elements on the webpage.
In this case we are looking for the div with the class "item-page" which contains the list of PDFs we want to download
We grab the unordered list from this div which is the complete list
Then grab all the list items complete list
'''
containerDiv = soup.find("div", {"class": "item-page"})
unorderedList = containerDiv.find("ul")
listItems = unorderedList.findAll("li")


'''
Next we want to loop through each list item and grab the link to the PDF
We then use the download_pdf function we created in utils.py to download the PDF
Then we use the extract_pdf function we created in utils.py to extract the data from the PDF
'''
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for item in listItems:

    '''
    Retrieve the month name from the list item text so we can name the PDF file correctly
    '''
    month = ""

    for monthName in months:
        if monthName in item.text:
            month = monthName

    download_pdf("https://www.ttb.gov" + item.findAll("a")[0].attrs["href"], "2022_PDFs/" + month + ".pdf")

    '''
    Use the time libary to sleep the program for 5 seconds after each download so we don't get rejected for spamming the website
    '''
    time.sleep(5)

    extract_pdf("2022_PDFs/" + month + ".pdf", month)