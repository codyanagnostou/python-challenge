# Import CSV modules 

import os
import csv

# Path to collect data from the Resources folder
banking_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#Define function
def banking_numbers(pl_data):
    # CSV headers: Date, Profit & Loss
    date = (pl_data[0])
    pandl = (pl_data[1])
# Read in the CSV file
with open(banking_csv, 'r') as csvfile:

# Print 
print(f"----------------------------")
print(f"Total Months: ")
print(f"Total: ")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Overall Graduation Rate: ")
print(f"Greatest Decrease in Profits: ")