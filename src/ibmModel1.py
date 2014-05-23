#This module implements the IBM Model 1 of Word Based Models.
#It takes 5 input from comman line argument. The filename, the training corpus, the testing corpus, the number of iterations, the number of sentences for training set.
#It returns the perplexity values for the given number of iterations along with the translation of the word on the basis of highest probability. 

import sys                                                                                              #import libraries
import math
from collections import defaultdict
from decimal import *
from preprocess import preprocessing
import operator

def calculatePerplexity(sentencePair, translationProbability):                                          #Perplexity Calculation
    newperplexity=0
    for pair in sentencePair:
        sourceWords=pair.split(' ')
        targetWords=sentencePair[pair].split(' ')
        ltarget=len(targetWords)
        lsource=len(sourceWords)
        probability=Decimal(0)
        for words in targetWords:
            if words!='':
                total=0
                for key in sourceWords:
                    if key!='':
                        total+=translationProbability[words][key]
                if total!=0:
                    probability+=Decimal(math.log(total,2))
        probability-=Decimal(math.log((lsource**ltarget),2))                                
        newperplexity+=Decimal(probability)
    newperplexity=-newperplexity
    newperplexity=2**newperplexity
    return newperplexity
        
def main():
    if len(sys.argv)!= 5:                                                                               #check arguments
        print "Usage :: python ibmModel1.py file_source file_target iterations numberOfSentencesForTraining"
        sys.exit(0)
    
    numberOfSentences=int(sys.argv[4])                                                                  #initialisation        
    numberOfIterations = int(sys.argv[3])
    sentencePair = preprocessing(numberOfSentences, sys.argv[1], sys.argv[2] )

    listOfSourceWords = defaultdict(list)                                                               #create list of possible source words for a target word
    for pair in sentencePair:
        sourceWords=pair.split(' ')
        targetWords=sentencePair[pair].split(' ')
        for word in targetWords:
            if word!='':
                for key in sourceWords:
                    if key!='':
                        listOfSourceWords[word].append(key)
                        
    for word in  listOfSourceWords:
       listOfSourceWords[word] = list(set(listOfSourceWords[word]))
        

    translationProbability=defaultdict(dict)                                                            #initialize the translation probability
    for wordTarget in  listOfSourceWords:
        uniqueWordsSource = listOfSourceWords[wordTarget]
        for wordSource in uniqueWordsSource:
            translationProbability[wordTarget][wordSource]=1/float(len(uniqueWordsSource))
        
        
            
    perplexity=0                                                                                        #Expectation Maximisation
    iteration=0
    while iteration<numberOfIterations:
        iteration+=1 
        print "Iteration: " +str(iteration)
        
        count=defaultdict(lambda:  defaultdict(float))                                                  #initialisation
        sumTotal=defaultdict(float)
        total=defaultdict(float)
            
        for pair in sentencePair:                                                                       #E Step
            sourceWords=pair.split(' ')
            targetWords=sentencePair[pair].split(' ')
            for words in targetWords:
                if words!='':
                    for key in sourceWords:
                        if key!='':
                            sumTotal[words]+=translationProbability[words][key]

            for words in targetWords:
                if words!='':
                    for key in sourceWords:
                        if key!='':
                            count[words][key]+=(translationProbability[words][key]/sumTotal[words])
                            total[key]+=(translationProbability[words][key]/sumTotal[words])
          
        for key in sourceWords:                                                                         #M Step
            if key!='':
                for words in targetWords:
                    if words!='':
                        translationProbability[words][key]=count[words][key]/total[key]

        newperplexity=calculatePerplexity(sentencePair, translationProbability)
        print newperplexity
        if perplexity>=newperplexity:
            print "Successful"
        else:
            print "Failed"
        perplexity=newperplexity

    data=[]
    print len(translationProbability)
    for key in translationProbability:
        possibleWords = translationProbability[key]
        data.append(key+' '+max(possibleWords.iteritems(), key=operator.itemgetter(1))[0])
            
    with open('wordTranslation.txt','w') as f:
        f.write('\n'.join(data))
        
            
if __name__ == "__main__":                                                                              #main
    main()
