#!/usr/bin/env python3

# Asis A Sotelo
# March 31, 2019
# load.py

"""1.Coverts data from csv arg into JSON and loads them into Firebase using python requests library 2. Creates and inverted index in Firebase"""

import argparse
import sys
import csv
import json

parser = argparse.ArgumentParser()
parser.add_argument("filenames", nargs = 3,  help = "file path of first comma seperated file")
args = parser.parse_args()

def main():

    print(args.filenames[0])


if __name__ == '__main__':
    main()
