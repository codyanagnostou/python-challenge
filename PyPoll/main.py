# Import CSV modules 
import os
import csv

# Create file path
election_csv = os.path.join("Resources", "election_data.csv")

#Lists to store data 
total_votes = []

# with open(budget_csv, encoding='utf-8') as csvfile:
with open(election_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        #Add up total months
        total_votes.append(row[0])

# Print results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {len(total_votes)}")
