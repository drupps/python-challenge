#Modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
print(csvpath)
with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #Variables to hold various counts
    total_votes = 0 #total votes
    votes = 0 #straight up votes
    percent_vote = 0 #percentage of votes candidate got
    win_count = 0 #winning vote count

    #Dict to hold candidate votes and list to hold all candidates
    candidates_dict = {}  #dictionary
    candidates = [] #list of all candidates, needed because you can't append to a dict
    win_candidate = '' #string

    for row in csvreader:

        total_votes +=1 #counter to keep track of total votes

        name = row[2] #pulling the candidate name from the third column #and storing it in candidates list
        if name not in candidates: #checking to see the candidate has been added already to the candidate list
            candidates.append



        # name = row[2]
        # total_votes = len(csvreader)

        # if name in candidate_dict:
        #     candidate_dict = candidate_dict.get(name, 'Does not exist')
        # else    
        #     candidate_dict = ['name'] = {candidate_dict}


    #print(total)
    print(candidate_dict)
    
    #print(f'{name}: {percent}% ({total})')


    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: " {total_votes})
    print(f"-------------------------")