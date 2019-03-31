import csv
import numpy as np
import os

INFILENAME = "Data/creditcard.csv"
OUTFILENAME = "Data/creditcard_out.csv"

np.set_printoptions(precision=3)

def importCSV():
    reader = csv.reader(open(INFILENAME), delimiter=",")
    x = list(reader)
    y = np.asarray(x[1:])

    return y

def writeCSV(arrayToWrite):
    try:
        fh = open(OUTFILENAME, 'r')
        os.remove(OUTFILENAME)
    except FileNotFoundError:
        pass
    np.savetxt(OUTFILENAME, arrayToWrite, delimiter=",", fmt='%s')

writeCSV(importCSV())
