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

    rows = [i for i in file_reader]
        
    # 2. Add to the total vote count.
    total_votes = len(rows)

    #Make a list of all candidates who received votes
    candidates = list({i[2] for i in rows})

# Function that takes in data and outputs dictionary of candidate and number of votes
def voteChecker(rows):
        return dict((name, len([1 for i in rows if name in i])) for name in candidates)

#Name dictionary for votes per candidate
votesEach = voteChecker(rows)

# #Calculate the percentage of votes each candidate won
# 3. Calculate the percentage of votes.
vote_percentage = dict((name, (float(votesEach[name]) / float(total_votes) * 100)) for name in candidates)
# 4. Print the candidate name and percentage of votes.
for name in candidates:
    print(f"{name}: received {vote_percentage[name]:.1f}% of the vote.")

# #Choose the winner of the election based on popular vote (highest percentage)
winner = [i for i, val in vote_percentage.items() if val == max([vote_percentage[i] for i in candidates])]
print(f"The winning candidate is {winner[0]}")
