# Modules
import os
import csv

# Set path for file
election_data = os.path.join('Resources/election_data.csv')

# Track various financial parameters
total_votes = 0
can_vote_count = 0
can_list = []
can_vote_count = []

with open(election_data, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    first_row = next(csvreader)
    total_votes = total_votes + 1

    for row in csvreader:

        # Count row numbers for obtaining total votes number
        total_votes = total_votes + 1

        # Start to accumulate candidates' name by comparing candidate name through loop
        # Put first found name in list
        can_name = row[2]

        if can_name in can_list:
            can_index = can_list.index(can_name)
            can_vote_count[can_index] = can_vote_count[can_index] + 1

        else:
            # Add candidate name to list if loop finds a new candidate name
            can_list.append(can_name)
            can_vote_count.append(1)

# #print results
# print(total_votes)
# print(f'each candidate: {can_list}')
# print(f'{can_list.index(can_name)}')

can_percent = []
for x in range (len(can_list)):
    vote_percent = (can_vote_count[x] / total_votes * 100)
    can_percent.append(vote_percent)

print(f'Vote Count for each candidate: {can_vote_count}')
print(f'Vote Percent for each candidate: {can_percent}')

# #Find a winner
# candidate_vote_list = total_candidate_vote_list + [khan_vote] + [correy_vote] + [li_vote] + [otooley_vote]
# max_votes_index = max(total_candidate_vote.values()) 
# first = [i for i in total_candidate_vote.keys() if total_candidate_vote[i]==winner]
# print(sorted(first)[0])

# print("                                                            ")
# print("Election Results")
# print("------------------------------------------------------------")
# print(f"Total Votes: {total_votes}")
# print("------------------------------------------------------------")
# print(f"Khan: {formatted_khan_vote_percentage}% ({len(net_khan_list)})")
# print(f"Correy: {formatted_correy_vote_percentage}% ({len(net_correy_list)})")
# print(f"Li: {formatted_li_vote_percentage}% ({len(net_li_list)})")
# print(f"O'Tooley: {formatted_otooley_vote_percentage}% ({len(net_otooley_list)})")
# print("------------------------------------------------------------")   