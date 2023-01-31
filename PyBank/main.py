# Import modules 

import os
import csv

# Create file path
csvpath = os.path.join("Resources", "budget_data.csv")

#Define function
def banking_numbers(row):
    # CSV headers: Date, Profit & Loss
    date = (row[0])
    pandl = (row[1])
# Read in the CSV file
with open(csvpath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# Print 
print(f"----------------------------")
print(f"Total Months: ")
print(f"Total: ")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Overall Graduation Rate: ")
print(f"Greatest Decrease in Profits: ")