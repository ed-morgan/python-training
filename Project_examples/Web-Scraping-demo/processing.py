import requests
import pandas
import numpy

def download_pdf(pdf_link, file_name):

    print(f"Downloading {file_name} PDF...")
    
    # Get response for the pdf link
    response = requests.get(pdf_link)

    # Write the contents to a pdf file
    pdf = open("Data/"+ file_name, "wb")
    pdf.write(response.content)
    pdf.close

    print(f"Finished downloading: {file_name}")


def add_data_to_tracker(file_name):

    print(f"Updating ReviewData.csv...")
    
    tracker_file = pandas.read_csv("Data/ReviewData.csv")

    updated_file = tracker_file.append({"Data": file_name}, ignore_index=True)

    updated_file.to_csv("Data/ReviewData.csv", index=False)

    print(f"Finished updating ReviewData.csv...")

