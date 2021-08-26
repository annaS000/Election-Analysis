# **Election Analysis**
## **Overview** 
---

> Tom, a Colorado Board of Elections employee, has asked us to help conduct an election audit of U.S. Congressional precinct results in Colorado. After receiving the [CSV](https://github.com/annaS000/Election-Analysis/tree/main/Resources) file containing the data, we have been asked to find a list of results including:
>* Total votes were cast in this congressional election
>* A breakdown of the number of votes and the percentage of total votes for each county in the precinct
>* The county which had the largest number of votes
>* A breakdown of the number of votes and the percentage of the total votes each candidate received
>* Which candidate won the election, what their vote count was, and what their percentage of the total votes was
>> Once we have our results, we can save them to a [text file](https://github.com/annaS000/Election-Analysis/blob/main/analysis/election_results.txt) and send over to Tom with our analysis.

---
## **Resources**

---

* Data Source: [election_results.csv](https://github.com/annaS000/Election-Analysis/tree/main/Resources)

* Software: Python 4.10.1, Visual Studio Code, 1.38.1

---

## **Summary** 


##### This section walks through the process of retrieving the data and reviews a summary of the results for the election. 

---
### **Setup:**
 After setting up our Python file in Visual Studio and importing our dependencies, we create paths to our input and output files to access them to read and write so, we can get started with our analysis of the data.

    import csv
    import os

    file_to_load = os.path.join("Resources", "election_results.csv")

    file_to_save = os.path.join("analysis", "election_results.txt")

    with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

>To read the title row and just use the data, we can use the line `headers = next(file_reader)`

 
 ### **Analysis:**

* **There were 369,711 votes cast in the election.** This number was retrieved by storing the `file_reader` data into a list and taking the length of it, since each element represents a vote in the election. 

        rows = [i for i in file_reader]
        total_votes = len(rows)
>Keep in mind: each element in our list, `rows` is also a list itself! So, `rows` is a list of lists.

* **The counties in this election were:**
    * Jefferson
    * Denver
    * Arapahoe

        <space>

    Using the properties of sets, we can obtain all of the unique names of counties in this election by indexing the elements in `rows`.

        counties = {i[1] for i in rows}
    >Our targeted index is equal to 1 because the county names are the 2nd element in each list.

* **The candidates in this election were:**
    * Raymon Anthony Doane
    * Diana DeGette
    * Charles Casper Stockham 

        <space>

     Using the same logic for collecting the county names, we are able to create a set of all candidates in the election.

        candidates = {i[2] for i in rows} 
    >Our index is equal to 2 because the candidate names are the 3rd element in each list.

<space>

* **The county results were:**
    * **Jefferson** received **10.5%** of the vote and **38,855** number of votes.
    * **Denver** received **82.8%** of the vote and **306,055** number of votes.
    * **Arapahoe** received **6.7%** of the vote and **24,801** number of votes.

        <space>

* **The county with the largest turnout was:**
    * **Denver**, which received **82.8%** of the vote and **306,055** number of votes.

        <space>    

    To get these results we can make dictionaries to store our data of interest and so we can print certain values when needed.


     ##### **Vote Dictionary (Counties):**
    From our list of county names, we can create a dictionary containing the county names as `keys` and their total votes received as their `values`.

        votesEach2 = dict((name, len([1 for i in rows if name in i])) for name in counties)
        
    > You can see here the dictionary is created with the function `dict()` by taking in a generator expression that creates tuples. The first element of the tuple is the county's name (the `keys`) and the second element will be the number of votes (the `values`). The values are being calculated by making lists of 1s for each county name. A one is placed in the list each time the current counties name is found in an element of `rows`. Then, by taking the lengths of these lists we have our number of votes per county.  

    ##### **Percentage Dictionary (Counties):**
    To get the vote percentages of each county, we can create another dictionary that will utilize `votesEach2`, `total_votes`, and `counties` to store the data. Then `maxcounty` will find us the county with the highest percentage of votes.

        vote_percentage2 = dict((name, (float(votesEach2[name]) / float(total_votes) * 100)) for name in counties)

        maxcounty = [i for i, j in vote_percentage2.items() if j == max(vote_percentage2[i] for i in counties)][0]

    > We could also do a similar check on `votesEach2` using the `max()` function to find the county with the greatest amount of total votes but I found that to be unnecessary. Both checks will yield the same result since we are applying the same action on all of the values in `votesEach2` and the amount of `total_votes` does not change.
* **The candidate results were:**
    * **Raymon Anthony Doane** received **3.1%** of the vote and **11,606** number of votes.
    * **Diana DeGette** received **73.8%** of the vote and **272,892** number of votes.
    * **Charles Casper Stockham** received **23.0%** of the vote and **85,213** number of votes. 

        <space>

        After getting the list of candidate, we are able to create the a dictionary, like we did earlier, containing the candidate names as `keys` and their total votes received as their `values`. We will also find `vote_percentage1` and the `winner` the same way we did for county names.

            votesEach1 = dict((name, len([1 for i in rows if name in i])) for name in candidates)

            vote_percentage1 = dict((name, (float(votesEach1[name]) / float(total_votes) * 100)) for name in candidates)

 <space>   

* **The winner of the election was:**
    * **Diana DeGette**, who received **73.8%** of the vote and **272,892** number of votes.



            winner = [i for i, j in vote_percentage1.items() if j == max(vote_percentage1[i] for i in candidates)][0]
---

### **Output**
##### Here is a visual of what our printed results look like after running the Python code in the Terminal.

---

![results](https://raw.githubusercontent.com/annaS000/Election-Analysis/main/Resources/election_outcomes.png)

---
## **Proposal**
##### [Link to Full Code](https://github.com/annaS000/Election-Analysis/blob/main/PyPoll_Challenge.py)

---

In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
#### **Examples:**
1. text

2. text
