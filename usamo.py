import csv

lines = open("Lines")
csvfile = open('usamo2021.csv', 'w', newline='')
p = csv.writer(csvfile)
for row in zip(*(map(lambda l:l[:-1], lines),) * 4):
	p.writerow(row)
	


