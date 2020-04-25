#!/usr/bin/env python3
#Asis A Sotelo
#April 25,2020

#search.py- Takes a list of keywords and returns primary key values of the tuples 

import argparse
import json
import sys
import requests

FIREBASE_URL = url = 'https://inf55-6540d.firebaseio.com/'

parser = argparse.ArgumentParser()
parser.add_argument("keywords", nargs="*", help="Enter list of keywords seperated by a space.")
argv = parser.parse_args()
keywords = argv.keywords

def json_retriever(key_word):

    key_word_url = FIREBASE_URL + "sample/" +key_word+".json"
    print(key_word_url)

    response = requests.get(key_word_url)
    print(response.json())


def main():
    
    for keyword in keywords:
        json_retriever(keyword)

if __name__ == "__main__":
    main()
