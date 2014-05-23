#This function takes as input the word translations obtained from ibm model 1, the file in which we want to write the output and the number of sentences to be
#translated along with the filename. 
#It returns the file containing the translated sentences.

import string                                                                                           #import libraries 
import sys

def main():
    
    dict_translation={}
    if len(sys.argv)!= 5:                                                                               #check arguments
        print "Usage :: python evaluation.py wordTranslation.txt outputFile numberOfSentences_to_Test inputFile"
        sys.exit(0)
        
    with open(sys.argv[1],'r') as f:                                                                    #create dictionary for word and translated words
        for line in f:
            word=line.strip().split(' ')
            dict_translation[word[0]]=word[1]
        
    table = string.maketrans("","")                                                                     #initialisation                                                           
    numberOfSentences=int(sys.argv[3])
    count=0
    data=''

    with open(sys.argv[4],'r') as f:  
        for line in f:                                                                                      #find translation
            count+=1
            translatedWord=[]
            line = line.strip().translate(table, string.punctuation).lower()
            words = line.split(' ')
            for key in words:
                if key in dict_translation:
                    translatedWord.append(dict_translation[key])
                elif key=='':
                    translatedWord.append('')
                else:
                    translatedWord.append('NULL')
            data+=' '.join(translatedWord)+'\n'
            if count==numberOfSentences:
                break

    f=open(sys.argv[2],'w')                                                                             #write into file
    f.write(data)
    f.close()


if __name__ == "__main__":                                                                              #main
    main()
