# You are in PyPoll

# Import the OS and CSV Reader Module
import os
import csv

# Find the file
pypoll_csv = os.path.join('Resources', 'PyPoll_ElectionData.csv')

# Make poll_data a list
poll_data = []

# Read from the pypoll file
with open(pypoll_csv, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
            poll_data.append(row)

    # Print headers
    print('Election Results')
    print('----------------------')

    # Find the total number of votes cast
    total_votes = len(poll_data)

    print(f'Total Votes: {total_votes}')
    print('----------------------')

    # Use a dictionary to find candidates and vote counts
    candidates_votes = {}

    for candidates in poll_data:
        if candidates[2] in candidates_votes:
            candidates_votes[candidates[2]] += 1
        else:
            candidates_votes[(candidates[2])] = 1

    # Create another dictionary with candidates and their percentage of votes
    candidates_percent = dict([(key, (value / total_votes) * 100) for key, value in candidates_votes.items()])

    # Find the winner of the election based on popoular vote
    candidate = list(candidates_percent.keys())
    votes = list(candidates_percent.values())
    winner = candidate[votes.index(max(votes))]

    # A final list with both values in it for each candidate
    final_list_candidates = list(candidates_percent.keys())
    final_list_percents = list(candidates_percent.values())
    final_list_votes = list(candidates_votes.values())

    # Print each of the candidates, their percentage of votes, and the number of votes
    i = 0
    for row in final_list_candidates:
        print(f'{final_list_candidates[i]}: {final_list_percents[i]:.2f}% ({final_list_votes[i]})')
        i += 1

    print('----------------------')

    print(f'Winner: {winner}')

    print('----------------------')



# Write to the txt file
output_path = os.path.join('Analysis', 'PyPollAnalysis.txt')

# # Open the file using "write" mode.
# with open(output_path, 'w') as text_file:

#     # Print outputs
#     print('Election Results', file = text_file)
#     print('----------------------', file = text_file)
#     print(f'Total Votes: {total_votes}', file = text_file)
#     print('----------------------', file = text_file)

