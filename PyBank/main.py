# You are in PyBank

# Import the OS and CSV Reader Module
import os
import csv

# Find the file
pybank_csv = os.path.join('Resources', 'PyBank_FinancialData.csv')

bank_data = []

# Define the function and have it accept 'bank_data' as its sole parameter
def print_bank_data(bank_data):
    
    # Assign values to usefully named variables
    ProfLoss = 0
    
    for months in bank_data:
        ProfLoss += int(months[1])

    print(ProfLoss)
    # set total months
    total_months = len(bank_data)

    print(total_months)


# Read in the CSV
with open(pybank_csv, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
    
        bank_data.append(row)

    # Print required output
    print(f"Financial Analysis")
    print(f"--------------------------")    
    # print(f"Total months: {total_months}")
    print_bank_data(bank_data)

