#!/usr/bin/env python3

# Asis A Sotelo
# March 31, 2019
# load.py

"""1.Coverts data from csv arg into JSON and loads them into Firebase using python requests library 2. Creates and inverted index in Firebase"""

import argparse
import sys
import csv
import json

# parser = argparse.ArgumentParser()
# parser.add_argument("filenames", nargs = 3,  help = "file path of first comma seperated file")
# args = parser.parse_args()

def main():

    # print(args.filenames[0])

    csvFilePath = 'city.csv'

    url = 'https://inf55-6540d.firebaseio.com/sample.json'
    data = {}

############# Loads the data into Firebase ##############


    with open(csvFilePath) as csvFile:
        dialect = csv.Sniffer().sniff(csvFile.read(1024))
        csv.register_dialect("custom",dialect) 
        csvFile.seek(0)
        reader = csv.DictReader(csvFile,dialect="custom")
        fieldnames = [reader.fieldnames[i].replace("#","").replace(" ","") for i in range(len(reader.fieldnames))]
        csvFile.seek(0)
        reader=csv.DictReader(csvFile,fieldnames,dialect ="custom")

        next(reader)
        print(fieldnames)

        for row in reader:
            id = row[fieldnames[0]]
            data[id]=row
            print(data)

    

#################################################################
#################################################################






if __name__ == "__main__":
    main()

