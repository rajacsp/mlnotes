---
title: Product-Summary-Classification-Nb
date: 2025-01-04
author: Your Name
cell_count: 24
score: 20
---

---
title: "Text Classification - Naive Bayes - Product Summary"
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
filename = 'https://docs.google.com/spreadsheet/ccc?key=1sN_OwRH8evSuMjjpjUJTonuJ3vKWC5iZj8yiEAF728k&output=csv'

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
      <th>link</th>
      <th>title</th>
      <th>summary</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.walmart.ca/en/ip/seiki-50-class-4k...</td>
      <td>NaN</td>
      <td>Introducing the Seiki 50 Inch ULTRA HD (2160P)...</td>
      <td>electronics</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.walmart.ca/en/ip/sharp-60-class-4k...</td>
      <td>NaN</td>
      <td>Enjoy Ultra HD entertainment on a amazing look...</td>
      <td>electronics</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.walmart.ca/en/ip/rca-24-led-hd-tv/...</td>
      <td>NaN</td>
      <td>The RCA 24" 720p Class 60Hz LED D TV features ...</td>
      <td>electronics</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.walmart.ca/en/ip/rca-32-tvdvd-comb...</td>
      <td>NaN</td>
      <td>The RCA 32" ultra-slim 720p 60HZ LED-LCD HDTV ...</td>
      <td>electronics</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.walmart.ca/en/ip/rca-65-4k-ultra-h...</td>
      <td>NaN</td>
      <td>With the RTUC6520 Curved TV, enjoy 4K Ultra HD...</td>
      <td>electronics</td>
    </tr>
  </tbody>
</table>
</div>




```python
# remove not null

df = df[pd.notnull(df['category'])]
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
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>0.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (19, 4)




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
      <th>link</th>
      <th>title</th>
      <th>summary</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://www.walmart.ca/en/ip/seiki-50-class-4k...</td>
      <td>NaN</td>
      <td>Introducing the Seiki 50 Inch ULTRA HD (2160P)...</td>
      <td>electronics</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.walmart.ca/en/ip/sharp-60-class-4k...</td>
      <td>NaN</td>
      <td>Enjoy Ultra HD entertainment on a amazing look...</td>
      <td>electronics</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.walmart.ca/en/ip/rca-24-led-hd-tv/...</td>
      <td>NaN</td>
      <td>The RCA 24" 720p Class 60Hz LED D TV features ...</td>
      <td>electronics</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.walmart.ca/en/ip/rca-32-tvdvd-comb...</td>
      <td>NaN</td>
      <td>The RCA 32" ultra-slim 720p 60HZ LED-LCD HDTV ...</td>
      <td>electronics</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.walmart.ca/en/ip/rca-65-4k-ultra-h...</td>
      <td>NaN</td>
      <td>With the RTUC6520 Curved TV, enjoy 4K Ultra HD...</td>
      <td>electronics</td>
    </tr>
    <tr>
      <th>5</th>
      <td>https://www.walmart.ca/en/ip/movelo-algonquin-...</td>
      <td>NaN</td>
      <td>\nMetallic purple with sky blue streaks, the M...</td>
      <td>bikes</td>
    </tr>
    <tr>
      <th>6</th>
      <td>https://www.walmart.ca/en/ip/movelo-algonquin-...</td>
      <td>NaN</td>
      <td>\nSix speeds, hand brakes and a metallic blue ...</td>
      <td>bikes</td>
    </tr>
    <tr>
      <th>7</th>
      <td>https://www.walmart.ca/en/ip/movelo-algonquin-...</td>
      <td>NaN</td>
      <td>Six speeds, hand brakes and a striking blue ap...</td>
      <td>bikes</td>
    </tr>
    <tr>
      <th>8</th>
      <td>https://www.walmart.ca/en/ip/275-hyper-bicycle...</td>
      <td>NaN</td>
      <td>Popular for trails and casual riding; full sus...</td>
      <td>bikes</td>
    </tr>
    <tr>
      <th>9</th>
      <td>https://www.walmart.ca/en/ip/26-hyper-bicycles...</td>
      <td>NaN</td>
      <td>Popular for trails and casual riding; full sus...</td>
      <td>bikes</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = df[pd.notnull(df['summary'])]


df['summary']

```




    0     Introducing the Seiki 50 Inch ULTRA HD (2160P)...
    1     Enjoy Ultra HD entertainment on a amazing look...
    2     The RCA 24" 720p Class 60Hz LED D TV features ...
    3     The RCA 32" ultra-slim 720p 60HZ LED-LCD HDTV ...
    4     With the RTUC6520 Curved TV, enjoy 4K Ultra HD...
    5     \nMetallic purple with sky blue streaks, the M...
    6     \nSix speeds, hand brakes and a metallic blue ...
    7     Six speeds, hand brakes and a striking blue ap...
    8     Popular for trails and casual riding; full sus...
    9     Popular for trails and casual riding; full sus...
    10    Two striking colors, metallic blue and hot pin...
    11    Midnight blue with scarlet red streaks, the 26...
    12    The steel gray steel frame and the acid green ...
    13    Help the LEGO® City farmer manage his crops wi...
    14    \nEnter the Dragon Pit with throne, gate-openi...
    15    Travel with Han Solo, Chewbacca and their frie...
    16    Evade the HunterCopter’s stud shooters and Ven...
    17    Fly a sleek interceptor with LEGO® Star Wars A...
    18    Display and role-play with this majestic meter...
    Name: summary, dtype: object




```python
# count words
df['summary'].apply ( lambda x: len(x.split(' ')) ).sum()
```




    3041




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
df['summary'] = df['summary'].apply(clean_text)
```


```python
# Check the words count again

df['summary'].apply ( lambda x: len(x.split(' ')) ).sum()
```




    2333




```python
X = df.summary
y = df.category
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

    accuracy 1.0


##### What did we do?

We have just passed summary as an input and predicted category based on the summary. For the testing purpose, we have used only 5 rows. 


---
**Score: 20**