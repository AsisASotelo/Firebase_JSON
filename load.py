#!/usr/bin/env python3
# Asis A Sotelo
# Friday, April 10th, 2020

#load.py - Development of Inverted Index


import csv
import time
import requests 
import numpy
import re
import json
import argparse
from progress.bar import IncrementalBar
import time
import string
"""load.py - 1. Loads data to Firebase 2. Creates inverted of Index and Uploads to Firebase

Arguments - pathname1 pathname2 pathname3
"""
FIREBASE_URL='https://inf55-6540d.firebaseio.com/'


parser = argparse.ArgumentParser()
parser.add_argument("filenames", nargs = "*",  help = "file path of first comma seperated file")
args = parser.parse_args()
filenames= args.filenames

def clean_keys(x):
    y = ''
    s = ["'", "/", ".", ",","#","\\","[","]","(",")","`","-"]
    for i in x:
        if i in s:
            y+= ' '
        else:
            y+=i

    y = ''.join([i for i in y])
    return y

def clean(x):
    y = ''
    
    for i in x:
        if i in string.punctuation:
            y+= ' '
        else:
            y+=i

    y = ''.join([i for i in y if(not i.isdigit())])
    return y

class IndexCreator:

    INDEX = {}

    def __init__(self,file_args):
        self.file_names = file_args

    def printargs(self):
        print(self.file_names)
    
    def indexer(self, filePathName,data):

        bar = IncrementalBar(filePathName, max = len(data))
        csv_file = filePathName.replace(".csv","")

        # Creates Index Using data dict created in loader
        for key, value in data.items():
            for key2,value2 in value.items():
                value2 = clean(value2)
                attribs = value2.split()
                for word in attribs:
                    word = word.lower()
                    if word not in self.INDEX: # Word has not been added to Index
                        self.INDEX[word]={csv_file:[key]}
                    elif csv_file not in self.INDEX[word]: # CSV File not added to Word Index
                        self.INDEX[word][csv_file] = [key]
                    else:
                        self.INDEX[word][csv_file].append(key)
        
            bar.next()
        bar.finish()
        time.sleep(3)
    
    def upload(self,data,url):
        data_json = json.dumps(data)
        response = requests.put(url,data_json)
        

        return response.status_code ==200
    def create_data(self,file_Path_Name):

        csv_File_Path = file_Path_Name
        file_name_url = FIREBASE_URL + file_Path_Name.replace(".csv","") + ".json"

        data = {}

        print("Creating diction for %s ... \n" % file_Path_Name)
        time.sleep(2)
    

        with open(csv_File_Path,'r',encoding='utf8',errors='ignore') as csv_File:
            dialect = csv.Sniffer().sniff(csv_File.read(1024))
            csv.register_dialect("custom",dialect) 
            csv_File.seek(0)
            reader = csv.DictReader(csv_File,dialect="custom")
            fieldnames = [reader.fieldnames[i].replace("#","").replace(" ","") for i in range(len(reader.fieldnames))]
            csv_File.seek(0)
            reader=csv.DictReader(csv_File,fieldnames,dialect ="custom")

            next(reader)
        
            for row in reader:
                id = row[fieldnames[0]]
                data[id]=row

        print("Finished creating dictionary for %s.\n" % file_Path_Name)
        time.sleep(2)
        return data

    def index_create_upload(self):
        index_url = FIREBASE_URL + "index" + ".json"
        for file_name in self.file_names:
            data_url = FIREBASE_URL + file_name.replace(".csv","") +".json"
            file_name_data = self.create_data(file_name)
            
            if self.upload(file_name_data,data_url):
                print("Loaded %s into Firebase Successfully !\n" % file_name)
            else:
                print("Failed to load %s into Firebase !\n" % file_name)
            
            self.indexer(file_name,file_name_data)
        
        print("Loading index into Firebase ...\n")
        time.sleep(1)
        self.upload(self.INDEX,index_url)
        print("Finished loading index into Firebase\n")

def main():

    indexer = IndexCreator(filenames)
    indexer.index_create_upload()


if __name__=="__main__":
    main()