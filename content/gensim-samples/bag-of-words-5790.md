---
title: Bag-Of-Words-5790
date: 2024-11-24
author: Your Name
cell_count: 10
score: 10
---

---
title: "Bag of Words"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from gensim.utils import simple_preprocess
from gensim import corpora
from pprint import pprint
```


```python
contents = [
    "More than half of survey participants also reported clicking on a headline expecting to read a balanced news account, only to find the story was pushing an agenda.",
    "The survey, conducted over a five-day period last month, sampled more than 2,300 Canadians."
]
```


```python
contents
```




    ['More than half of survey participants also reported clicking on a headline expecting to read a balanced news account, only to find the story was pushing an agenda.',
     'The survey, conducted over a five-day period last month, sampled more than 2,300 Canadians.']




```python
# Get the tokens
tokens = [simple_preprocess(doc) for doc in contents]
```


```python
tokens
```




    [['more',
      'than',
      'half',
      'of',
      'survey',
      'participants',
      'also',
      'reported',
      'clicking',
      'on',
      'headline',
      'expecting',
      'to',
      'read',
      'balanced',
      'news',
      'account',
      'only',
      'to',
      'find',
      'the',
      'story',
      'was',
      'pushing',
      'an',
      'agenda'],
     ['the',
      'survey',
      'conducted',
      'over',
      'five',
      'day',
      'period',
      'last',
      'month',
      'sampled',
      'more',
      'than',
      'canadians']]




```python
# Create the dictionary
dict = corpora.Dictionary()
```


```python
dict
```




    <gensim.corpora.dictionary.Dictionary at 0x11d0a88d0>




```python
# Create the Corpus
corpus1 = [dict.doc2bow(doc, allow_update=True) for doc in tokens]
```


```python
pprint(corpus1)
```

    [[(0, 1),
      (1, 1),
      (2, 1),
      (3, 1),
      (4, 1),
      (5, 1),
      (6, 1),
      (7, 1),
      (8, 1),
      (9, 1),
      (10, 1),
      (11, 1),
      (12, 1),
      (13, 1),
      (14, 1),
      (15, 1),
      (16, 1),
      (17, 1),
      (18, 1),
      (19, 1),
      (20, 1),
      (21, 1),
      (22, 1),
      (23, 2),
      (24, 1)],
     [(10, 1),
      (20, 1),
      (21, 1),
      (22, 1),
      (25, 1),
      (26, 1),
      (27, 1),
      (28, 1),
      (29, 1),
      (30, 1),
      (31, 1),
      (32, 1),
      (33, 1)]]



---
**Score: 10**