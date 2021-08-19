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

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")

# # Write some data to the file.
# outfile.write("Counties in the Election\n")

# # Make a line
# outfile.write("-------------------------\n")

# # Write three counties to the file.
# outfile.write("Arapahoe\nDenver\nJefferson")

# # Close the file
# outfile.close()

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
