# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    #Storing rows in a list
    rows = [i for i in file_reader]

    # Total vote count
    total_votes = len(rows)

    # Make a list of all candidates who received votes
    candidates = list({i[2] for i in rows}) 

    # Create a county list and county votes dictionary.
    counties =  list({i[1] for i in rows}) 

# Function that takes in data and returns dictionary of candidate and number of votes for candidates
def voteChecker1(rows):
        return dict((name, len([1 for i in rows if name in i])) for name in candidates)

# Function that takes in data and returns dictionary of candidate and number of votes for counties
def voteChecker2(rows):
        return dict((name, len([1 for i in rows if name in i])) for name in counties)

# Name dictionary for votes per candidate
votesEach1 = voteChecker1(rows)
votesEach2 = voteChecker2(rows)

# 2: Track the largest county and county voter turnout.

winning_candidate = []
winning_count = []
        
# Percentage of votes in a dictionary
vote_percentage1 = dict((name, (float(votesEach1[name]) / float(total_votes) * 100)) for name in candidates)

vote_percentage2 = dict((name, (float(votesEach2[name]) / float(total_votes) * 100)) for name in counties)

         # 6f: Write an if statement to determine the winning county and get its vote count.


    # 7: Print the county with the largest turnout to the terminal.

winner_county = [i for i, j in vote_percentage2.items() if j == max([vote_percentage2[i] for i in counties])][0]


    # 8: Save the county with the largest turnout to a text file.


# Print results
print(f"************************\n")
print(f"     Final Results\n")
print(f"************************\n")

#Print the candidate name and percentage of votes.
for name in candidates:
    print(f"{name}: {vote_percentage[name]:.1f}% ({votesEach[name]:,})\n")

#Choose the winner of the election (highest percentage) 
winner = [i for i, j in vote_percentage1.items() if j == max([vote_percentage1[i] for i in candidates])][0]

# Print out the winner and summary

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {votesEach[winner]:,}\n"
    f"Winning Percentage: {vote_percentage[winner]:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
