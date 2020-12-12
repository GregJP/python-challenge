import os
import csv

bdpath = os.path.join("Resources","budget_data.csv")

months, profit = 0, 0
each_profit, dates, change = [], [], []

with open(bdpath) as bdfile:
    
    bdreader = csv.reader(bdfile,delimiter=',')
    next(bdreader)
    
    for row in bdreader:
        months += 1
        profit += int(row[1])
        dates.append(row[0])
        each_profit.append(int(row[1]))

    for x in range(1,months):
        change.append(each_profit[x]-each_profit[x-1])

average_change = round(sum(change)/len(change),2)
max_change = max(change)
min_change = min(change)
max_date = dates[change.index(max_change)+1]
min_date = dates[change.index(min_change)+1]


line12 = f"Financial Analysis\n------------------"
line345 = f"Total Months: {months}\nTotal Profit: ${profit}\nAverage Change: ${average_change}"
line67 = f"Greatest Profit Increase: {max_date} (${max_change})\nGreatest Profit Decrease: {min_date} (${min_change})"
print(f"{line12}\n{line345}\n{line67}")    

with open('analysis/budget_data.txt','w') as out:
    out.writelines(f"{line12}\n{line345}\n{line67}")