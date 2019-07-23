import csv
file = "C:/Users/Arsh/PycharmProjects/tictaktoe/arsh1.csv"
with open(file,"r") as myfile:
    csvreader = csv.reader(myfile, delimiter='\n')

    for row in csvreader:
        print(row)
