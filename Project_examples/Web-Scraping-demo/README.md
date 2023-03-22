# Web Scraping Bot:

# Requirements:

* pip install the following:
    * requests (A library that handles making HTTP api requests)
    * beautifulsoup4 (A library which handles searching, iterating and parsing the information from requests)
    * numpy (A library that handles math operations)
    * pandas (A library that handles data manipulation)

* Website/HTLM you want to scrap:
    * On line 8 inside `main.py` (`result = requests.get("https://www.ukfinance.org.uk/data-and-research/data/business-finance-review")`), Input the webpage URL here.
    * On line 13 inside `main.py` (`archivedData = soup.find("ul", "documents__list")`) we list the elements of the page where we want to scrap data from. On the webpage we can find it, right click and press inspect. This will bring you an element that looks like that following. `<ul class='documents__list'> TEST LIST </ul>. You can then replace the values on line 13 with the values you find here. First the tag element (ul), and followed by the class value (documents__list).    

# Running the program

Once the requirements have been furfulled, the program can be run by navigating to the folder `main.py` is saved in, using the command line prompt. Then executing `python ./main.py`

This program will download the webpage supplied on line 8 of `main.py`. It will then search all that code for the specified parts you would like to scrap supplied on line 13 of `main.py`.  Once it has that information, it will loop through the values inside the list. Comparing each value against the CSV file stored in the `Data` folder. If it does not find the value inside that CSV file, it will download it into the `Data` folder and append the value into the CSV file so it doesn't download it a second time.

This program could be scheduled to run at set time intervals, so that it regularly scraps and downloads useful information for you.

# Structure

`main.py` - The entry file that can be called to run the program.
`processing.py` - A file that holds utility functions that are used by main.py during the webscraping process.
`Data` - A folder which holds a CSV file which tracks which PDFs we have already processed. Also the location that will be used to store downloaded PDFs
`requirements.txt` - A file that can be used by pip to mass install all the libraries necessary. The following command will install all the libraries listed in this file: `pip install -r requirements.txt`

# Expansion

This is the entry point for web-scraping. It can draw information directly from webpage, or download files. These files can then be passed onto another python program for further processing, analyse, or visualisation. E.g If a PDF stores information, it is possible to grab this information, save/append this into other csv files which can be used.