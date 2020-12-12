import os
import csv

edpath = os.path.join("Resources","election_data.csv")

votes, khan, correy, li, otooley = 0, 0, 0, 0, 0

with open(edpath) as edfile:

    edreader = csv.reader(edfile,delimiter=',')
    next(edreader)

    for row in edreader:
        votes += 1
        if row[2] == "Khan":
            khan += 1
        if row[2] == "Correy":
            correy += 1
        if row[2] == "Li":
            li += 1
        if row[2] == "O'Tooley":
            otooley += 1

khan_per = round(khan/votes*100,3)
correy_per = round(correy/votes*100,3)
li_per = round(li/votes*100,3)
otooley_per = round(otooley/votes*100,3)

totals = [khan, correy, li, otooley]
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
winner = candidates[totals.index(max(totals))]

line12 = f"Election Results\n-----------------------"
line34 = f"Total votes: {votes}\n-----------------------"
line56 = f"Khan: {khan_per}% ({khan})\nCorrey: {correy_per}% ({correy})"
line78 = f"Li: {li_per}% ({li})\nO'Tooley: {otooley_per}% ({otooley})"
line90 = f"-----------------------\nWinner: {winner}"
print(f"{line12}\n{line34}\n{line56}\n{line78}\n{line90}")

with open('analysis/election_data.txt','w') as out:
    out.writelines(f"{line12}\n{line34}\n{line56}\n{line78}\n{line90}")