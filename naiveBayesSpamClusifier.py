from fileinput import filename
import os
import io
from posixpath import dirname
import numpy as np
from pandas import DataFrame
from sklearn. feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
 
def readFile(path):
    for root, dirname, filenames in os.walk(path):
        for filename in filenames:
            path=os.path.join(root,filename)
            inBody=False
            lines=[]
            f=io.open(path,"r", encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line=='\n'
                    inBody=True
            f.close()
            message='\n'.join(lines)
            yield path,message