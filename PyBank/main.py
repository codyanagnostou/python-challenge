# Import modules 

import os
import csv

# Create file path
budget_csv = os.path.join("Resources", "budget_data.csv")

#Create function


# Lists to store data
total_months = []
total = []
avg_change = []
price_increase = []
price_decrease = []

# with open(budget_csv, encoding='utf-8') as csvfile:
with open(budget_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        #Add up total months
        total_months.append(row[0])

# Print 
print(f"----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")