from utils import extract_pdf


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for month in months:
    extract_pdf("2022_PDFs/" + month + ".pdf", month)