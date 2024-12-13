---
title: File-To-Dictionary
date: 2024-12-13
author: Your Name
cell_count: 6
score: 5
---

---
title: "File To Dictionary"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import gensim
from gensim import corpora
from gensim.utils import simple_preprocess
from smart_open import smart_open
import os
```


```python
dictionary = corpora.Dictionary()
```


```python
# Create gensim dictionary form a single tet file
dictionary = corpora.Dictionary(simple_preprocess(line, deacc=True) for line in open('sample.txt', encoding='utf-8'))
```


```python
print(dictionary)
```

    Dictionary(78 unique tokens: ['account', 'agenda', 'also', 'an', 'balanced']...)



```python
dictionary.token2id
```




    {'about': 25,
     'according': 66,
     'account': 0,
     'agenda': 1,
     'also': 2,
     'an': 3,
     'and': 26,
     'are': 45,
     'assigned': 67,
     'association': 68,
     'authenticity': 27,
     'balanced': 4,
     'be': 69,
     'between': 28,
     'canadian': 46,
     'canadians': 57,
     'cannot': 70,
     'cent': 29,
     'clicking': 5,
     'conducted': 58,
     'day': 59,
     'distinguish': 30,
     'doubts': 31,
     'election': 47,
     'error': 71,
     'expecting': 6,
     'fact': 32,
     'falsehood': 33,
     'federal': 48,
     'find': 7,
     'findings': 49,
     'five': 60,
     'found': 34,
     'foundation': 50,
     'had': 35,
     'half': 8,
     'headline': 9,
     'in': 36,
     'intelligence': 72,
     'journalism': 51,
     'jumped': 37,
     'last': 61,
     'margin': 73,
     'marketing': 74,
     'month': 62,
     'more': 10,
     'news': 11,
     'of': 12,
     'on': 13,
     'online': 75,
     'only': 14,
     'over': 63,
     'participants': 15,
     'particularly': 52,
     'past': 38,
     'per': 39,
     'period': 64,
     'polls': 76,
     'pushing': 16,
     'read': 17,
     'reported': 18,
     'research': 77,
     'respondents': 40,
     'run': 53,
     'sampled': 65,
     'says': 54,
     'stories': 41,
     'story': 19,
     'struggled': 42,
     'survey': 20,
     'than': 21,
     'the': 22,
     'to': 23,
     'troubling': 55,
     'up': 56,
     'was': 24,
     'while': 43,
     'year': 44}




---
**Score: 5**