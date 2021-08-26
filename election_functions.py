#Any Election Function
# Add our dependencies.
import csv
import os

def getPath(folder,file):
    return os.path.join(folder,file)

# Assign variables for the files to load and save to paths.
load = getPath('Resources', 'election_results.csv')
save = getPath('analysis', 'election_analysis.txt')

def getData(load):
    with open(load) as election_data:
        file_reader = csv.reader(election_data)
        headers = next(file_reader)
        return [i for i in file_reader]

rows = getData(load)

def totalVotes(rows):
        return len(rows)

total_votes = totalVotes(rows)

def stringSet(colNumber):
        return {i[colNumber] for i in rows}
        
#Make a list (set) of all candidates/counties in election
candidates = stringSet(2) 
counties =  stringSet(1)

def votesEach(stringSet):
    return dict((name, len([1 for i in rows if name in i])) for name in stringSet)

# Name dictionary for votes per candidate and county
votesEach1 = votesEach(candidates)
votesEach2 = votesEach(counties)

def percentVote(whichEach,stringSet):
    return dict((name, (float(whichEach[name]) / float(total_votes) * 100)) for name in stringSet)
# Percentage of votes for candidates and counties in a dictionary
vote_percentage1 = percentVote(votesEach1,candidates)
vote_percentage2 = percentVote(votesEach2,counties)

def whoWon(whichPercent,stringSet):
    return [i for i, j in whichPercent.items() if j == max(whichPercent[i] for i in stringSet)][0]
#Choose the winner and largest county turnout of the election (highest percentage) 
winner = whoWon(vote_percentage1,candidates)
maxcounty = whoWon(vote_percentage2,counties)

def electionResults():
    with open(save, "w") as txt_file:
        numvotes = (
            f"Election Results\n"
            f"------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"------------------------\n\n"
            f"County Votes:\n") 

        txt_file.write(numvotes)

        for name in counties:
            county_results = (
                f"{name}: {vote_percentage2[name]:.1f}% ({votesEach2[name]:,})\n")

            txt_file.write(county_results)

        maxcounty_results = (
            f"-------------------------\n"
            f"Largest County Turnout: {maxcounty}\n"
            f"-------------------------\n")

        txt_file.write(maxcounty_results)    

        for name in candidates:
            candidate_results = (
                f"{name}: {vote_percentage1[name]:.1f}% ({votesEach1[name]:,})\n")  

            txt_file.write(candidate_results)

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winner}\n"
            f"Winning Vote Count: {votesEach1[winner]:,}\n"
            f"Winning Percentage: {vote_percentage1[winner]:.1f}%\n"
            f"-------------------------")

        txt_file.write(winning_candidate_summary)
    return print(open(save).read())

printNsave = electionResults()


# list of bytes per variable
varlist = [printNsave,total_votes,candidates,counties,votesEach1,
           votesEach2,vote_percentage1,vote_percentage2,winner,maxcounty]
howbig = [sys.getsizeof(i) for i in varlist]
print(howbig)
