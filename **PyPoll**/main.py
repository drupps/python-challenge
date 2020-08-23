#Modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first
    csv_header = next(csvreader)

    #variables to hold various counts
    total_votes = 0 #total votes
    votes = 0 #straight up votes
    percent_vote = 0 #percentage of votes candidate got
    win_count = 0 #winning vote count

    #dict to hold candidate votes and list to hold all candidates
    candidates_dict = {}  #dictionary
    candidates_list = [] #list of all candidates, needed because you can't append to a dict
    win_candidate = '' #string

    for row in csvreader:
        total_votes +=1 #counter to keep track of total votes

        name = row[2] #pulling the candidate name from the third column #and storing it in candidates list
        if name not in candidates_list: #checking to see the candidate has been added already to the candidate list
            candidates_list.append(name) #appending the candidate not in the list to the list of candidates
            candidates_dict[name] = 0 #tracking that candidate's voter count
        candidates_dict[name] += 1 #add a vote to that candidate's count

print(f'Election Results \n----------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')

    #percentage stuff
for name in candidates_dict:
    votes = candidates_dict[name] #everytime we put a candidates name into the dict, we set that to votes
    percent_vote = round((votes/total_votes) * 100, 2) #percent vote with

    if (candidates_dict[name] > win_count): #this determines if a candidates vote count is great than the win count
        win_count = candidates_dict[name] #if the above statement is true, than the winning count is put for the candidate vote count
        win_candidate = name #assigns the name of the candidate to the win_candidate variable

    print(f'{name}: {percent_vote}% ({votes})') #holy shit, one result was shown when the print was outside the if statement and now trying it inside shows the four!
print(f'-------------------------')
print(f'The Winner: {win_candidate}')
print(f'-------------------------')

# Specify the file to write to (copied from my pybank main.py)
output_path = os.path.join("Analysis", "PyPoll_Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents (copied from my pybank main.py)
with open(output_path, 'w') as csvfile:

    #writing to the txt file
    csvfile.write(f'Election Results \n----------------------------\n')
    csvfile.write(f'Total Votes: {total_votes}\n')
    csvfile.write(f'{name}: {percent_vote}% ({total_votes})\n')
    csvfile.write(f'-------------------------\n')
    csvfile.write(f'The Winner: {win_candidate}\n')
    csvfile.write(f'-------------------------')
   