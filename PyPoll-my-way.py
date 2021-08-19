#Election Results

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # 2. Add to the total vote count.
        total_votes = sum(row)

# 3. Print the total votes.
print(total_votes)


# #Find total number of votes cast
# totalVotes = sum(1 for i in Ballot)

# #Make a list of all candidates who received votes
# candidates = {i for i in Candidate}

# #Find the total number of votes each candidate received
# votesEach = [(i,sum(j)) for i in candidates for j]

# #Calculate the percentage of votes each candidate won
# votePercentage = [(i) for i in Candidate]
# #Choose the winner of the election based on popular vote (highest percentage)
# max([votePercentage[i][0] for i in range(len(votePercentage))])
