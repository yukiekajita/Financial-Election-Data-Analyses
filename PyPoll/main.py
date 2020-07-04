# Modules
import os
import csv

# Set path for file
election_data = os.path.join('Resources/election_data.csv')

# Track various financial parameters
total_votes = 0
can_list = []
can_vote_count = []

with open(election_data, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:

        # Starting +1 to count row numbers for obtaining total votes number and first row candidate name
        total_votes = total_votes + 1
        can_vote_count.append(1)

        # Start to accumulate candidates' name by comparing candidate names between rows through loop
        # Put first found name in list
        can_name = row[2]

        if can_name in can_list:
            can_index = can_list.index(can_name)
            can_vote_count[can_index] = can_vote_count[can_index] + 1

        else:
            # Add candidate name to list if a loop finds a new candidate name
            can_list.append(can_name)
            can_vote_count.append(1)

# #Checking results
# print(total_votes)
# print(f'each candidate: {can_list}')
# print(f'{can_list.index(can_name)}')

can_percent = []
max_votes = can_vote_count[0]
max_index = 0
can_rank_list = []

for x in range (len(can_list)):
    vote_percent = (can_vote_count[x] / total_votes * 100)
    can_percent.append(vote_percent)

##Checking results
# print(f'Vote Count for each candidate: {can_vote_count}')
# print(f'Vote Percent for each candidate: {can_percent}')

    # Find a winner from the election
    if can_vote_count[x] > max_votes:
        max_votes = can_vote_count[x]
        max_index = x

winner = can_list[max_index]
##Checking results
# print(winner)

print("                                                            ")
print("Election Results")
print("------------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------------------------")
for x in range (len(can_list)):
    print(f'{can_list[x]}: {can_percent[x]:.3f}% ({can_vote_count[x]})')   
print("------------------------------------------------------------") 
print(f'Winner: {winner}')
print("------------------------------------------------------------") 

## Make Python Result Output in Texfile
###Type "$python3 main.py >> output.text"