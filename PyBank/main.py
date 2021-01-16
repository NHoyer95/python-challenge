# You are in PyBank

# Import the OS and CSV Reader Module
import os
import csv

# Find the file
pybank_csv = os.path.join('Resources', 'PyBank_FinancialData.csv')

# Read in the CSV

with open(pybank_csv, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

