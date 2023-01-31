# Import modules 

import os
import csv

# Create file path
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
total_months = []
total = []
avg_change = []
price_increase = []
price_decrease = []
grad_rate = []

# Print 
print(f"----------------------------")
print(f"Total Months: ")
print(f"Total: ")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Overall Graduation Rate: ")
print(f"Greatest Decrease in Profits: ")