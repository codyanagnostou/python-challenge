# Import modules 
import os
import csv

# Create file path
budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
total_months = []
total = 0
avg_num_change = 0
avg_change = []
price_increase = []
price_decrease = []

# with open(budget_csv, encoding='utf-8') as csvfile:
with open(budget_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    firstrow = next(csvreader, None)
    previousvalue = int(firstrow[1])
    for row in csvreader:
        #Add up total months
        total_months.append(row[0])
        total = total + int(row[1])
        change = int(row[1]) - previousvalue
        previousvalue = int(row[1])
        avg_change.append(change)
    
   
# Print results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {len(total_months)+1}")
print(f"Total: ${total}")
print(f"Average Change: {sum(avg_change)/len(avg_change)}")
print(f"Greatest Increase in Profits: {max(avg_change)}")
print(f"Greatest Decrease in Profits: {min(avg_change)}") 

# Specify the file to write to
output_path = os.path.join("Analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents

with open(output_path, 'w') as f:
  print(f"Financial Analysis", file=f)
  print(f"----------------------------", file=f)
  print(f"Total Months: {len(total_months)+1}", file=f)
  print(f"Total: ${total}", file=f)
  print(f"Average Change: {sum(avg_change)/len(avg_change)}", file=f)
  print(f"Greatest Increase in Profits: {max(avg_change)}", file=f)
  print(f"Greatest Decrease in Profits: {min(avg_change)}", file=f) 