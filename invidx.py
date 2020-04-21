#!/usr/bin/env python3
# Asis A Sotelo
# Friday, April 10th, 2020

#invidx.py - Development of Inverted Index


import csv
import requests 
import numpy
import re 
from progress.bar import IncrementalBar



STOP_WORDS =['#','NULL','i', 'me', 'my', 'myself',\
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

def clean(x):
    y = ''
    s = ["'", "/", ".", ","]
    for i in x:
        if i in s:
            y+= ' '
        else:
            y+=i

    y = ''.join([i for i in y if(not i.isdigit())])
    return y



def main():

    csvFilePath = 'city.csv'
    
    index = {}


    with open(csvFilePath, 'r',encoding='utf8',errors='replace') as csvFile:
        text = csvFile.read()
        result = clean(text).lower()
        result = result.split()
        word_list = [word for word in result if word not in STOP_WORDS]
        word_list = list(set(word_list))
        print(len(word_list))
    bar = IncrementalBar('Progress', max = len(word_list))

    

    with open(csvFilePath,'r',encoding="utf8",errors='replace') as csvFile:
        dialect = csv.Sniffer().sniff(csvFile.read(1024))
        csv.register_dialect("custom",dialect) 
        csvFile.seek(0)
        dict_file = csv.DictReader(csvFile,dialect = "custom")
        for word in word_list:
            bar.next()
            if word not in index:
                index.update({word:{csvFilePath:{}}})
            
            for row in dict_file:
                
                
                for key, value in row.items():
                    value = clean(value).lower().strip()
                    if word in value: # Checks to see if word is in attributes of row
                        #print(index[word].keys())
                        if key in index[word][csvFilePath].keys(): # Checks if key is already in list
                            index[word][csvFilePath][key].append(row[list(row.keys())[0]])
                            pass
                        else:
                            index[word][csvFilePath].update({key :[] })
            csvFile.seek(0)


    bar.finish()

    







    


    


        




if __name__=="__main__":
    main()