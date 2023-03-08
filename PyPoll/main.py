# Import CSV modules 
import os
import csv

# Create file path
election_csv = os.path.join("Resources", "election_data.csv")

#Lists to store data 
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# with open(budget_csv, encoding='utf-8') as csvfile:
with open(election_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        #Add up total months
        total_votes += 1
        candidate_name = row[2]
# If the candidate does not match any existing candidate, add the candidate to list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidates voter count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


# Print results
print(f"Election Results\n"
f"----------------------------\n"
f"Total Votes: {total_votes}\n"
f"----------------------------\n"
)
for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(f"{candidate_results}\n")
        
# Specify the file to write to
output_path = os.path.join("Analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents

with open(output_path, 'w') as f:
    print(f"Election Results\n", file=f)
    print(f"----------------------------\n", file=f)
    print(f"Total Votes: {total_votes}\n", file=f)
    print(f"----------------------------\n", file=f)
    
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(f"{candidate_results}\n", file=f)

