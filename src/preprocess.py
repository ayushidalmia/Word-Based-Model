#This module takes as input the bi-text corpuses and the number of sentences.
#It returns the training and testing dataset along with the sentence pairs. 

import random                                                                           #import libraries
import string

def preprocessing(numberOfSentences, sourceFile, targetFile):

    indices=[]
    trainingSource=[]
    trainingTarget=[]
    testingSource=[]
    testingTarget=[]
    sentencePair={}
    
    for i in range(numberOfSentences):                                                  #create random numbers                           
        indices.append(random.randint(0,1920208))

    with open(sourceFile,'r') as  fSource:                                              #read from source language corpus
        for index,line in enumerate(fSource):
            if len(line)>0:
                if index in indices:
                    trainingSource.append(line.strip())                                 #create training and testing for source language
                else:
                    testingSource.append(line.strip())
                
    with open(targetFile,'r') as  fTarget:                                              #read from source language corpus
        for index,line in enumerate(fTarget):
            if len(line)>0:
                if index in indices:
                    trainingTarget.append(line.strip())                                 #create training and testing for source language
                else:
                    testingTarget.append(line.strip())
    
    table = string.maketrans("","")                                                     #create sentence pair for training set
    for i in range(len(trainingSource)):
        sentencePair[trainingSource[i].translate(table, string.punctuation).lower()]=trainingTarget[i].translate(table, string.punctuation).lower()
            
            
    with open('trainingSource.txt','wb') as f:                                          #write into training file for source data
        f.write('\n'.join(trainingSource))

    with open('trainingTarget.txt','wb') as f:                                          #write into training file for target data
        f.write('\n'.join(trainingTarget))

    testingSource=testingSource[:numberOfSentences]                                     #write into testing file for source data
    with open('testingSource.txt','wb') as f:
        f.write('\n'.join(testingSource))

    testingTarget=testingTarget[:numberOfSentences]                                     #write into testing file for target data
    with open('testingTarget.txt','wb') as f:
        f.write('\n'.join(testingTarget))

    return sentencePair
