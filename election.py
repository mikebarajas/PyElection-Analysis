import csv
import os
directoryPath = os.getcwd()
files = []

for root, directories, filenames in os.walk(directoryPath):
    for filename in filenames:
        if filename[-3:] == "csv":
            files.append(filename) 

print(files)

def electionResults(filename):
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        votes = []
        results = []
        for row in csvReader:
            votes.append(row[2])
    total_votes = len(votes[1:])
    file = open("Election_Results/"  + filename[:-4] + '.txt','w')
    file.write('PyPoll Election Results \n')
    file.write('------------------------- \n')
    file.write('Total Votes: ' + str(total_votes) + '\n')
    file.write('------------------------- \n')
    candidates = list(set(votes[1:]))
    for candidate in candidates:
        count = 0    
        for vote in votes:
            if candidate == vote:
                count = count +1
        results.append({"Name":candidate,"Votes":count})
        percentage = str(round(100 * count/total_votes, 2))
        file.write(candidate + ': ' + percentage + "% with " + str(count) + ' Votes\n')
        file.write('------------------------- \n')
    winner = sorted(results, key=lambda candidate:candidate['Votes'])[-1:][0]["Name"]
    file.write('Winner: ' + winner + '\n')
    file.write('------------------------- \n')
    file.close() 

for x in files:
    electionResults(x)




