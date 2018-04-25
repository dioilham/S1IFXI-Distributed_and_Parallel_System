import csv
#import numpy as np
fileName = "john.txt"
# the file is this
# A,A,@,@,$,$,&,&,!,!,H,H,Z,Z,W,W

f = open(fileName, 'r')
reader = csv.reader(f)
allRows = list(reader)
#chunks = [allRows[x:x+100] for x in xrange(0, len(allRows), 100)]
#np.array_split(np.array(allRows), 5)
#firstRow = allRows[0]

def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]

A = [1,2,3,4,5,6]
B, C = split_list(A)

#print(allRows)
#print(firstRow)
size = len(allRows)
print(size)
#print(len(firstRow))

