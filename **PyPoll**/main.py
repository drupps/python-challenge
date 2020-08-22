# Modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
print(csvpath)
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    total = 0
    candidate_dict = {}

    for row in csvreader:
        total +=1
        name = row[2]
        if name in candidate_dict:
            name = candidate_dict[]

    #print(total)
    print(candidate_dict)
    