---
title: Tokenize Sentence
date: 2024-12-03
author: Your Name
cell_count: 10
score: 10
---

---
title: "Tokenize Sentences"
author: "Raja CSP Raman"
date: 2019-05-02
description: "-"
type: technical_note
draft: false
source: https://tedboy.github.io/nlps/gensim_tutorial/tut1.html
---

```python
from gensim import corpora
```


```python
documents = [
    "The traditional paradigm just seems safer: be firm and a little distant from your employees", 

"The people who work for you should respect you, but not feel so familiar with you that they might forget who’s in charge", 

"A little dog-eat-dog, tough-it-out, sink-or-swim culture seems to yield time-tested results and keep people hungry and on their toes", 

"New developments in organizational research are providing some surprising answers to these questions", 

"Tough managers often mistakenly think that putting pressure on employees will increase performance", 

"What it does increase is stress—and research has shown that high levels of stress carry a number of costs to employers and employees alike", 

"Stress brings high health care and turnover costs", 

"In a study of employees from various organizations, health care expenditures for employees with high levels of stress were 46 percent greater than at similar organizations without high levels of stress", 

"In particular, workplace stress has been linked to coronary heart disease in both retrospective (observing past patterns) and prospective (predicting future patterns) studies" 
]
```


```python
documents
```




    ['The traditional paradigm just seems safer: be firm and a little distant from your employees',
     'The people who work for you should respect you, but not feel so familiar with you that they might forget who’s in charge',
     'A little dog-eat-dog, tough-it-out, sink-or-swim culture seems to yield time-tested results and keep people hungry and on their toes',
     'New developments in organizational research are providing some surprising answers to these questions',
     'Tough managers often mistakenly think that putting pressure on employees will increase performance',
     'What it does increase is stress—and research has shown that high levels of stress carry a number of costs to employers and employees alike',
     'Stress brings high health care and turnover costs',
     'In a study of employees from various organizations, health care expenditures for employees with high levels of stress were 46 percent greater than at similar organizations without high levels of stress',
     'In particular, workplace stress has been linked to coronary heart disease in both retrospective (observing past patterns) and prospective (predicting future patterns) studies']




```python
# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
```


```python
stoplist
```




    {'a', 'and', 'for', 'in', 'of', 'the', 'to'}




```python
texts = [
    [word for word in document.lower().split() if word not in stoplist] for document in documents
]
```


```python
len(texts)
```




    9




```python
texts[0]
```




    ['traditional',
     'paradigm',
     'just',
     'seems',
     'safer:',
     'be',
     'firm',
     'little',
     'distant',
     'from',
     'your',
     'employees']




```python

```


---
**Score: 10**