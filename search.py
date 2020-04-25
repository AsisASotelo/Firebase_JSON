#!/usr/bin/env python3
#Asis A Sotelo 
#April 22, 2020

#search.py - Takes a list of keywords and returns primary key.

import argparse
import sys
import csv
import json
import requests

"""search.py - Program that takes a list of keyword as command line arguments and returns values of tuples.

Arguments - Keywords: arg[n]

Returns - Tuples
    

"""

# Create parser for programing 

# parser = argparse.ArgumentParser()
# parser.add_argument("keywords",nargs ='+',help="Must be a list of keywords")
# args = parser.parse_args()


def main():

    for keyword in args.keywords:
        print(keyword)


if __name__ == '__main__':
    main()