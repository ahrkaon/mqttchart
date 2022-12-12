import csv

def makecsv():
    with open("test.csv","r") as f:
        reader = csv.reader(f)
        for row in reader:
            temp = row
    list_float = list(map(float, temp[:-1]))
    return list_float