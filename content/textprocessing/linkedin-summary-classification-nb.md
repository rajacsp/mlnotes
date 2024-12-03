---
title: Linkedin-Summary-Classification-Nb
date: 2024-12-04
author: Your Name
cell_count: 25
score: 25
---

---
title: "Text Classification - Naive Bayes - LinkedIn Summary"
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
filename = 'https://docs.google.com/spreadsheet/ccc?key=1MtpNgoJKlgqkPOw_SkMt3dP5GUZRQL4cJxzZ6FEKgzg&output=csv'

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
      <td>https://www.linkedin.com/in/claire-lesage/</td>
      <td>Computational Linguist at Facebook (via Infote...</td>
      <td>NaN</td>
      <td>datascientist</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.linkedin.com/in/shayna-gardiner-38...</td>
      <td>Computational Linguist &amp; Data Scientist @ Rece...</td>
      <td>Linguist, scientist, PhD. Focus on language va...</td>
      <td>datascientist</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.linkedin.com/in/varada-kolhatkar-b...</td>
      <td>Computational Linguist. Computer Scientist.</td>
      <td>NaN</td>
      <td>datascientist</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.linkedin.com/in/mukesh-vaghasiya-a...</td>
      <td>Java Developer</td>
      <td>5+ years of experience developing web applicat...</td>
      <td>backend-developer</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.linkedin.com/in/pratik-bhatt-34143...</td>
      <td>Java Developer at eClinicalWorks</td>
      <td>I am a dynamic personality with curiosity to l...</td>
      <td>backend-developer</td>
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
      <th>link</th>
      <th>title</th>
      <th>summary</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7</td>
      <td>7</td>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>7</td>
      <td>7</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>https://www.linkedin.com/in/claire-lesage/</td>
      <td>Software Engineer at Microsoft | Full stack de...</td>
      <td>Experienced Software Engineer with a demonstra...</td>
      <td>backend-developer</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (7, 4)




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
      <td>https://www.linkedin.com/in/claire-lesage/</td>
      <td>Computational Linguist at Facebook (via Infote...</td>
      <td>NaN</td>
      <td>datascientist</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://www.linkedin.com/in/shayna-gardiner-38...</td>
      <td>Computational Linguist &amp; Data Scientist @ Rece...</td>
      <td>Linguist, scientist, PhD. Focus on language va...</td>
      <td>datascientist</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://www.linkedin.com/in/varada-kolhatkar-b...</td>
      <td>Computational Linguist. Computer Scientist.</td>
      <td>NaN</td>
      <td>datascientist</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://www.linkedin.com/in/mukesh-vaghasiya-a...</td>
      <td>Java Developer</td>
      <td>5+ years of experience developing web applicat...</td>
      <td>backend-developer</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://www.linkedin.com/in/pratik-bhatt-34143...</td>
      <td>Java Developer at eClinicalWorks</td>
      <td>I am a dynamic personality with curiosity to l...</td>
      <td>backend-developer</td>
    </tr>
    <tr>
      <th>5</th>
      <td>https://www.linkedin.com/in/komal-shah-a2917151/</td>
      <td>Software Engineer at Microsoft | Full stack de...</td>
      <td>Experienced Software Engineer with a demonstra...</td>
      <td>backend-developer</td>
    </tr>
    <tr>
      <th>6</th>
      <td>https://www.linkedin.com/in/anjali-jaiswal-b3a...</td>
      <td>Java Developer at CDN Software Solutions</td>
      <td>Experienced Java Software Engineer with a demo...</td>
      <td>backend-developer</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = df[pd.notnull(df['summary'])]


df['summary']

```




    1    Linguist, scientist, PhD. Focus on language va...
    3    5+ years of experience developing web applicat...
    4    I am a dynamic personality with curiosity to l...
    5    Experienced Software Engineer with a demonstra...
    6    Experienced Java Software Engineer with a demo...
    Name: summary, dtype: object




```python
# count words
df['summary'].apply ( lambda x: len(x.split(' ')) ).sum()
```




    227




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




    166




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


```python

```


---
**Score: 25**