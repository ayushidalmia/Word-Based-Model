Word-Based-Model
================

This repository consists of project done as part of the courses undertaken Natural Language Processing - Advanced, Spring 2014. The course was instructed by [Dr. Dipti Misra Sharma](http://www.iiit.ac.in/people/faculty/dipti), [Dr. Ravi Jampani](http://www.cise.ufl.edu/~rjampani/index.html) and [Mr. Akula Arjun Reddy](http://web.iiit.ac.in/~arjunreddy.aug08/)

##Requirements
Python 2.6 or above

##Problem
The project is about Machine Translation using Word Based Model, more specifically IBM Model 1. It takes as input the bi-text corpus for English and German sentences. Later, given a German sentence it returns the possible sentence in the English translation and vice versa. 

The src folder contains the following files:

###Main Functions

* ibmModel1.py

This program takes the two corpuses and returns a file containing the source language word and the best possible target language word.

In order to run the above program run the following command:
**python ibmModel1.py source_Corpus target_Corpus number_of_iterations number_of_sentences_for_training**

* evaluation.py

This program takes as input the file created in the previous code and generates the translated file for the given input file. 

In order to run the above program run the following command:
**python evaluation.py wordTranslation.txt outputFile numberOfSentences_to_Test inputFileToBeTranslated**

###Helper Functions
* preprocess.py

This acts as a helper function to ibmModel1.py. It creates the training and testing files along with the hashmap of the training sentence pairs.