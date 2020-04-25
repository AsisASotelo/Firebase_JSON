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
"""load.py - 1. Loads data to Firebase 2. Creates inverted of Index and Uploads to Firebase

Arguments - pathname1 pathname2 pathname3
"""
FIREBASE_URL='https://inf55-6540d.firebaseio.com/'

parser = argparse.ArgumentParser()
parser.add_argument("filenames", nargs = "*",  help = "file path of first comma seperated file")
args = parser.parse_args()
filenames= args.filenames



STOP_WORDS = ['#','NULL','i', 'me', 'my', 'myself',\
'we', 'our', 'ours', 'ourselves', 'you', "you're",\
"you've", "you'll", "you'd", 'your', 'yours', 'yourself'\
, 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's",\
'her', 'hers', 'herself', 'it', "it's", 'its', \
'itself', 'they', 'them', 'their', 'theirs', 'themselves'\
, 'what', 'which', 'who', 'whom', 'this', 'that', "that'll"\
, 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be'\
, 'been', 'being', 'have', 'has', 'had', 'having', 'do',\
'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but',\
'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at'\
, 'by', 'for', 'with', 'about', 'against', 'between', 'into'\
, 'through', 'during', 'before', 'after', 'above', 'below', 'to'\
, 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under'\
, 'again', 'further', 'then', 'once', 'here', 'there', 'when', 
'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', \
'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', \
'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', \
're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", \
'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',\
"hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', \
"mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', \
"shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', \
"weren't", 'won', "won't", 'wouldn', "wouldn't",'null']

#Definiton and Implementation of Methods
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
    s = ["'", "/", ".", ",","#","[","]","(",")","`","-"]
    for i in x:
        if i in s:
            y+= ' '
        else:
            y+=i

    y = ''.join([i for i in y if(not i.isdigit())])
    return y

def word_lister(filePathName):  # // Returns List of Words Given File Name
    with open(filePathName, 'r',encoding='utf8',errors='replace') as csv_File:
        text = csv_File.read()
        result = clean(text).lower()
        result = result.split()
        word_list = [word for word in result if word not in STOP_WORDS]
        word_list = list(set(word_list))
    
    return word_list

def loader(file_Path_Name):
    csv_File_Path = file_Path_Name
    file_name_url = FIREBASE_URL + file_Path_Name.replace(".csv","") + ".json"

    data = {}

    print("Starting to load %s one second \n" % file_Path_Name)
    print("loading ...")
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
    
    #Send to Firebase

    data_json = json.dumps(data)
    response = requests.put(file_name_url,data_json)

    if response.status_code == 200:
        print("Finished loading %s into FIREBASE.\n" % file_Path_Name)
    else:
        print("Error Loading\n")
    
def indexer(filePathName,list_of_words):

    index = {}
    word_list = list_of_words
    bar = IncrementalBar(filePathName, max = len(word_list))
    index_url = FIREBASE_URL + "index/" + filePathName.replace(".csv","").capitalize()+".json"


    print("Starting to index %s one second" % filePathName)
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(".")
    

    with open(filePathName,'r',encoding="utf8",errors='replace') as csv_File:
        dialect = csv.Sniffer().sniff(csv_File.read(1024))
        csv.register_dialect("custom",dialect)
        csv_File.seek(0)
        dict_file = csv.DictReader(csv_File,dialect = "custom")
        file_title= filePathName.replace(".csv","")
        for word in word_list: # Loops over each normalized word found in CSV with word_lister
            if word not in index: # // Checks to see if word is already in index 
                index.update({word:{file_title:{}}}) # // If not adds to index
            
            for row in dict_file: # // Otherwise proceeds to check if word is found in any of the attribute fields
                
                
                for key, value in row.items():
                    value = clean(value).lower().strip()
                    if word in value:
                        row_number = row[list(row.keys())[0]] # Checks to see if word is in attributes values of row.
                        n_row_number = clean_keys(row_number).replace(" ","")
                        n_key = clean_keys(key).replace(" ","")

                        if n_key in index[word][file_title].keys(): # Checks if attribute key is already in list.
                            index[word][file_title][n_key][len(index[word][file_title][n_key])] = n_row_number
                        else:
                            index[word][file_title].update({ n_key:{0:n_row_number} })
            csv_File.seek(0)

            bar.next()
    bar.finish()
    print("Finished indexing %s ." % filePathName)
    print("Uploading index to FIREBASE ...")

    index_json = json.dumps(index)

    response = requests.put(index_url,data =index_json)
    
    if response.status_code == 200:
        print("Finished uploading index of %s ." % filePathName)
    else:
        print("Error Uploading")

    
   
# Main Method 

def main():

    # Loading of Each File

    for filename in filenames:
        word_list = word_lister(filename)
        loader(filename)

    # Indexing of Each File

    for filename in filenames:
        word_list = word_lister(filename)
        indexer(filename,word_list)






if __name__=="__main__":
    main()