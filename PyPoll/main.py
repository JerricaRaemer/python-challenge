import os
import csv

# Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidates = []
votes = {}


with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    csvreader_iteration = next(csvreader)
    #print(f"CSV Reader Iteration: {csvreader_iteration}")

    # ballot_id = []
    # county = []
    # candidate = []

    for row in csvreader:
        #print(row)
        # ballot_id.append(row[0])
        # county.append(row[1])
        # candidate.append(row[2])
        candidate = row[2]

        total_votes += 1
        if candidate not in candidates:
            candidates.append(candidate)
            votes[candidate]=0
        votes[candidate] += 1

print(votes)
percentages = {key: round(val / total_votes*100,3) for key, val in votes.items()}
print(percentages)
winning_candidate = max(votes, key=votes.get)
print(winning_candidate)

output1 = (
f"Election Results\n"
f"-------------------------\n"
f"Total Votes: {total_votes}\n"
f"-------------------------\n"
)
print(output1)

for k,v in votes.items():

    output2 = f"{k}: {percentages[k]}% ({v})\n"
    print(output2)

output3 = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"-------------------------"
)

print(output3)

    # print("List of Ballot ID's: ", ballot_id)
    # print("List of Counties: ", county)
    # print("List of Candidates: ", candidate)
        
# # Total number of votes cast
#     ballot_integers = [int(element) for element in ballot_id]
#     total_votes = len(ballot_integers)
#     print("Total Number of Votes: ", total_votes)

# # List of Candidates
#     candidates_number = len(set(candidate))
#     print("The number of candidates is ", candidates_number)

#     candidates_list = set(candidate)
#     print("The candidates are: ", candidates_list)

# # Percentage of votes for each candidate
#     votes_degette = candidate.count('Diana DeGette')
#     votes_stockham = candidate.count('Charles Casper Stockham')
#     votes_doane = candidate.count('Raymon Anthony Doane')

#     percentage_degette = votes_degette / total_votes
#     percentage_stockham = votes_stockham / total_votes
#     percentage_doane = votes_doane / total_votes

#     print("The percentage of votes for Diana DeGette is ", percentage_degette)
#     print("The percentage of votes for Charles Casper Stockham is ", percentage_stockham)
#     print("The percentage of votes for Raymon Anthony Doane is ", percentage_doane)

#     hundred_percent = percentage_degette + percentage_stockham + percentage_doane
#     print("Hopefully this is 100%: ", hundred_percent)
#     # yay!

# # Number of votes for each candidate
#     print("The total number of votes won by Diana Degette is ", votes_degette)
#     print("The total number of votes won by Charles Casper Stockham is ", votes_stockham)
#     print("The total number of votes won by Raymon Anthony Doane is ", votes_doane)

# # Winner by popular vote
#     percentages_array = [percentage_stockham, percentage_degette, percentage_doane]
#     print("The list of candidates is ", candidates_list)
#     print("The corresponding percentages for each candidate are ", percentages_array)
    
#     highest_percentage = max(percentages_array)
#     print("The winner had ", highest_percentage, " percentage of the votes!")
    
#     index_winner = percentages_array.index(highest_percentage)
#     print("The index of the winner is ", index_winner)
#     # winner_name = candidates_list[index_winner]
#     # print("The winner of the election by popular vote is ", winner_name)
