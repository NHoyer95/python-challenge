# You are in PyBank

# Import the OS and CSV Reader Module
import os
import csv

# Find the file
pybank_csv = os.path.join('Resources', 'PyBank_FinancialData.csv')

# Make bank_data a list
bank_data = []

# Define the function and have it accept 'bank_data' as its sole parameter
with open(pybank_csv, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
    
        bank_data.append(row)
    
    # Print static header rows
    print(f'Financial Analysis')
    print(f'--------------------------')

    # set total months
    total_months = len(bank_data)

    print(f'Total Months: {total_months}')

    # Find Profit/Loss Total
    ProfLoss = 0
    
    for months in bank_data:
        ProfLoss += int(months[1])

    print(f'Total: ${ProfLoss}')

    # Create lists that only include the profits/losses and the change in profits/losses
    pl_list = []
    change_in_pl_list = []

    # Loop through PL column of the data
    for months in bank_data:
        pl_list.append(int(months[1]))

    #Create variable to identify where we are at in the list
    i = 0

    # Loop through and calculate the change between rows in the pl list
    for numbers in range(len(pl_list) - 1):
        change_in_pl_list.append(int(pl_list[i + 1]) - int(pl_list[i]))
        i += 1

    # Calculate the Avg Change
    AvgChange = sum(change_in_pl_list) / len(change_in_pl_list)
    AvgChange = round(AvgChange, 2)

    print(f'Average Change: ${AvgChange}')

    # Calculate the greatest increase in profits
    GreatestProfIncrease = max(change_in_pl_list)
    index_increase_change = change_in_pl_list.index(GreatestProfIncrease) + 1

    print(f'Greatest Increase in Profits: {bank_data[index_increase_change][0]} (${GreatestProfIncrease})')

    # Calculate the greatest decrease in profits
    GreatestProfDecrease = min(change_in_pl_list)
    index_decrease_change = change_in_pl_list.index(GreatestProfDecrease) + 1

    print(f'Greatest Decrease in Profits: {bank_data[index_decrease_change][0]} (${GreatestProfDecrease})')


# Write to the txt file
output_path = os.path.join('Analysis', 'PyBankAnalysis.txt')

# Open the file using "write" mode.
with open(output_path, 'w') as text_file:

    # Output the results
    print(f'Financial Analysis', file = text_file)
    print(f'--------------------------', file = text_file)
    print(f'Total Months: {total_months}', file = text_file)
    print(f'Total: ${ProfLoss}', file = text_file)
    print(f'Average Change: ${AvgChange}', file = text_file)
    print(f'Greatest Increase in Profits: {bank_data[index_increase_change][0]} (${GreatestProfIncrease})', file = text_file)
    print(f'Greatest Decrease in Profits: {bank_data[index_decrease_change][0]} (${GreatestProfDecrease})', file = text_file)
