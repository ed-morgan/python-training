# Imports pypi libaries
import requests
import pandas
import numpy
import tabula
from bs4 import BeautifulSoup

'''
This file includes functions that are generic and can be used across multiple scripts
Each function should have a specific purpose and be reusable
'''

def retrieve_webpage(url):
    '''
    Get the content of the webpage using the request library. This content is the HTML structure of the webpage that can be seen through inspect element
    '''
    result = requests.get(url)
    return result.content

def transform_into_soup(content):
    '''
    Turn this content into a soup using beautiful soup library. A soup allows us to search the HTML structure of the webpage for specific elements
    '''
    return BeautifulSoup(content, features="html.parser")

def download_pdf(pdf_link, file_name):

    print(f"Downloading {file_name} PDF...")
    
    '''
    Use request library to download the PDF
    '''
    response = requests.get(pdf_link)
    
    '''
    Save the response content to a local file
    Reponse.content holds the actual PDF data without the metadata information we dont care about
    '''
    with open(file_name, 'wb') as f:
        f.write(response.content)

def extract_pdf(pdf_file, month):

    '''
    Fix for broken pdfs
    '''
    broken_months = ["May", "June", "July", "August", "October", "November", "December"]
    data_locations = 2

    if month in broken_months:
        data_locations = 6


    '''
    Retrieve our existing output file
    '''
    accumlation_df = pandas.read_csv("output/TTB_2022_stats.csv", index_col=0)

    '''
    Add our new month columns to the dataframe
    '''

    accumlation_df[month + " 2021"] = numpy.nan
    accumlation_df[month + " 2022"] = numpy.nan
    accumlation_df[month + " % Change"] = numpy.nan
    
    '''
    This will create a list of dataframes but these pdfs all contain a single page so we can just use the first dataframe in the list (dfs[0])
    '''
    dfs = tabula.read_pdf(pdf_file, pages=1, guess=True)
    ''' 
    We can save the dataframe to a csv file in case we want to use it again
    '''
    dfs[0].to_csv("output/" + month + ".csv")

    '''
    In this example we will extract the the 2022 info, the 2021 and the calculate the % change
    '''
    df = dfs[0]

    if month == "May" or month == "August" or month == "November" or month == "December":
        bottles_cans_2022 = int(df["Unnamed: 2"][data_locations].replace(",", ""))
        kegs_2022 = int(df["Unnamed: 2"][data_locations + 1].replace(",", ""))
    else:
        bottles_cans_2022 = int(df["Unnamed: 3"][data_locations].replace(",", ""))
        kegs_2022 = int(df["Unnamed: 3"][data_locations + 1].replace(",", "")) 

    if month == "May" or month == "August" or month == "November" or month == "December":
        bottles_cans_prev = int(df["Unnamed: 3"][data_locations].replace(",", ""))
        kegs_prev = int(df["Unnamed: 3"][data_locations + 1].replace(",", ""))
    else:
        bottles_cans_prev = int(df["Unnamed: 4"][data_locations].replace(",", ""))
        kegs_prev = int(df["Unnamed: 4"][data_locations + 1].replace(",", ""))

    accumlation_df[month + " 2022"][0] = bottles_cans_2022
    accumlation_df[month + " 2022"][1] = kegs_2022
    accumlation_df[month + " 2021"][0] = bottles_cans_prev
    accumlation_df[month + " 2021"][1] = kegs_prev
    accumlation_df[month + " % Change"] = accumlation_df.pct_change(axis="columns")[month + " 2022"]

    accumlation_df.to_csv("output/TTB_2022_stats.csv", index=True)