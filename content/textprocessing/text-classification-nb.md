---
title: Text-Classification-Nb
date: 2024-12-14
author: Your Name
cell_count: 25
score: 25
---

---
title: "Text Classification - Naive Bayes - Stackoverflow Tags"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
# Disclaimer: some code copied form this https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
```


```python
import logging
import pandas as pd
import numpy as np
from numpy import random
import gensim
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
```


```python
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup
from io import BytesIO
import requests
```

%matplotlib inline


```python
filename = 'https://gitlab.com/rajacsp/datasets/raw/master/stack-overflow-data.csv'

r = requests.get(filename)
data = r.content
```


```python
df = pd.read_csv(BytesIO(data))
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>post</th>
      <th>tags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>what is causing this behavior  in our c# datet...</td>
      <td>c#</td>
    </tr>
    <tr>
      <th>1</th>
      <td>have dynamic html load as if it was in an ifra...</td>
      <td>asp.net</td>
    </tr>
    <tr>
      <th>2</th>
      <td>how to convert a float value in to min:sec  i ...</td>
      <td>objective-c</td>
    </tr>
    <tr>
      <th>3</th>
      <td>.net framework 4 redistributable  just wonderi...</td>
      <td>.net</td>
    </tr>
    <tr>
      <th>4</th>
      <td>trying to calculate and print the mean and its...</td>
      <td>python</td>
    </tr>
  </tbody>
</table>
</div>




```python
# remove not null

df = df[pd.notnull(df['tags'])]
```


```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>post</th>
      <th>tags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>40000</td>
      <td>40000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>40000</td>
      <td>20</td>
    </tr>
    <tr>
      <th>top</th>
      <td>newbie - game development (iphone) - new to ob...</td>
      <td>c#</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>1</td>
      <td>2000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (40000, 2)




```python
# Count words

df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>post</th>
      <th>tags</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>what is causing this behavior  in our c# datet...</td>
      <td>c#</td>
    </tr>
    <tr>
      <th>1</th>
      <td>have dynamic html load as if it was in an ifra...</td>
      <td>asp.net</td>
    </tr>
    <tr>
      <th>2</th>
      <td>how to convert a float value in to min:sec  i ...</td>
      <td>objective-c</td>
    </tr>
    <tr>
      <th>3</th>
      <td>.net framework 4 redistributable  just wonderi...</td>
      <td>.net</td>
    </tr>
    <tr>
      <th>4</th>
      <td>trying to calculate and print the mean and its...</td>
      <td>python</td>
    </tr>
    <tr>
      <th>5</th>
      <td>how to give alias name for my website  i have ...</td>
      <td>asp.net</td>
    </tr>
    <tr>
      <th>6</th>
      <td>window.open() returns null in angularjs  it wo...</td>
      <td>angularjs</td>
    </tr>
    <tr>
      <th>7</th>
      <td>identifying server timeout quickly in iphone  ...</td>
      <td>iphone</td>
    </tr>
    <tr>
      <th>8</th>
      <td>unknown method key  error in rails 2.3.8 unit ...</td>
      <td>ruby-on-rails</td>
    </tr>
    <tr>
      <th>9</th>
      <td>from the include  how to show and hide the con...</td>
      <td>angularjs</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['post']
```




    0        what is causing this behavior  in our c# datet...
    1        have dynamic html load as if it was in an ifra...
    2        how to convert a float value in to min:sec  i ...
    3        .net framework 4 redistributable  just wonderi...
    4        trying to calculate and print the mean and its...
    5        how to give alias name for my website  i have ...
    6        window.open() returns null in angularjs  it wo...
    7        identifying server timeout quickly in iphone  ...
    8        unknown method key  error in rails 2.3.8 unit ...
    9        from the include  how to show and hide the con...
    10       when we need interface c# <blockquote>    <str...
    11       how to install .ipa on jailbroken iphone over ...
    12       dynamic textbox text - asp.net  i m trying to ...
    13       rather than bubblesorting these names...the pr...
    14       site deployed in d: drive and uploaded files a...
    15       connection in .net  i got     <blockquote>    ...
    16       how to subtract 1 from an int  how do i subtra...
    17       ror console show syntax error  i want to add d...
    18       distance between 2 or more drop pins  i was do...
    19       sql query - how to exclude a record from anoth...
    20       java - hackerrank.com 30 days of code  day 6  ...
    21       clarification required on responsibility of  $...
    22       complicated min/max multi-table query  i need ...
    23       in asp.net mvc4 using javascript  when the but...
    24       jquery document ready with google  this is how...
    25       compiling a trusted resource url in angular th...
    26       syntax error when $eval a string inside a dire...
    27       delay on a function jquery  i have a hover eff...
    28       what are all the restrictions by apple for iph...
    29       objective-c instance variables accessor method...
                                   ...                        
    39970    converting from byte[] to string <blockquote> ...
    39971    needs to delete a line that matches with strin...
    39972    cannot load file error...but file definitely e...
    39973    images won t show on my website  i have a simp...
    39974    find a matching string in an array or a word i...
    39975    how to add button to cell in table view  i nee...
    39976    what is the difference between these two code ...
    39977    app terminates when erasing the image in ios  ...
    39978    how to customize react booststrap style   i am...
    39979    any legitimate way to bypass maxlength on html...
    39980    what is the best way for doing a real-world gu...
    39981    how to use x-y corrdinates and a radius to sim...
    39982    asp.net connection string error help needed  i...
    39983    403 error when upload file to google drive  i ...
    39984    rails after create not functioning as expected...
    39985    warning errors problem  <strong>program</stron...
    39986    iphone: decryption error  ***** with encipherm...
    39987    def help  trying to define pieces of code  not...
    39988    trying to get file name of the largest file  s...
    39989    i want to get the data from the access databas...
    39990    need to modify the geojson file for australia ...
    39991    having trouble converting a whole sentence fro...
    39992    php delete from multiple tables  i have a basi...
    39993    sql join multiple tables with pivot  i m tryin...
    39994    simple sql query not executing  i am familiar ...
    39995    different output if at end of function rather ...
    39996    multiple arrays  is there a way to access/stor...
    39997    c - how to differentiate a second same key pre...
    39998    state.go not working (#! & url is being append...
    39999    understanding the mechanisms of intentservice ...
    Name: post, Length: 40000, dtype: object




```python
# count words
df['post'].apply ( lambda x: len(x.split(' ')) ).sum()
```




    10286120




```python
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """
        text: a string
        
        return: modified initial string
    """
    text = BeautifulSoup(text, "lxml").text # HTML decoding
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text) # delete symbols which are in BAD_SYMBOLS_RE from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # delete stopwors from text
    return text
```


```python
df['post'] = df['post'].apply(clean_text)
```


```python
# Check the words count again

df['post'].apply ( lambda x: len(x.split(' ')) ).sum()
```




    3424297




```python
X = df.post
y = df.tags
```


```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```


```python
# Using NB

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
```


```python
nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])
nb.fit(X_train, y_train)
```




    Pipeline(memory=None,
         steps=[('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict',
            dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
            lowercase=True, max_df=1.0, max_features=None, min_df=1,
            ngram_range=(1, 1), preprocessor=None, stop_words=None,
            strip...inear_tf=False, use_idf=True)), ('clf', MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True))])




```python
nb.fit(X_train, y_train)
```




    Pipeline(memory=None,
         steps=[('vect', CountVectorizer(analyzer='word', binary=False, decode_error='strict',
            dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
            lowercase=True, max_df=1.0, max_features=None, min_df=1,
            ngram_range=(1, 1), preprocessor=None, stop_words=None,
            strip...inear_tf=False, use_idf=True)), ('clf', MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True))])




```python
from sklearn.metrics import classification_report
y_pred = nb.predict(X_test)

print('accuracy %s' % accuracy_score(y_pred, y_test))
```

    accuracy 0.7395



```python
my_tags = ['java','html','asp.net','c#','ruby-on-rails','jquery','mysql','php','ios','javascript','python','c','css','android','iphone','sql','objective-c','c++','angularjs','.net']


print(classification_report(y_test, y_pred,target_names=my_tags))
```

                   precision    recall  f1-score   support
    
             java       0.63      0.65      0.64       613
             html       0.94      0.86      0.90       620
          asp.net       0.87      0.92      0.90       587
               c#       0.70      0.77      0.73       586
    ruby-on-rails       0.73      0.87      0.79       599
           jquery       0.72      0.51      0.60       589
            mysql       0.77      0.74      0.75       594
              php       0.69      0.89      0.78       610
              ios       0.63      0.59      0.61       617
       javascript       0.57      0.65      0.60       587
           python       0.70      0.50      0.59       611
                c       0.79      0.78      0.79       594
              css       0.84      0.59      0.69       619
          android       0.66      0.84      0.74       574
           iphone       0.64      0.83      0.72       584
              sql       0.66      0.64      0.65       578
      objective-c       0.79      0.77      0.78       591
              c++       0.89      0.83      0.86       608
        angularjs       0.94      0.89      0.91       638
             .net       0.74      0.66      0.70       601
    
        micro avg       0.74      0.74      0.74     12000
        macro avg       0.74      0.74      0.74     12000
     weighted avg       0.75      0.74      0.74     12000
    



```python

```


---
**Score: 25**