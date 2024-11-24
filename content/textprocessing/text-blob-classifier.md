---
title: Text-Blob-Classifier
date: 2024-11-24
author: Your Name
cell_count: 8
score: 5
---

---
title: "Text Blob Classifier"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from textblob.classifiers import NaiveBayesClassifier
```


```python
train = [
     ('I love this sandwich.', 'pos'),
     ('this is an amazing place!', 'pos'),
     ('I feel very good about these beers.', 'pos'),
     ('this is my best work.', 'pos'),
     ("what an awesome view", 'pos'),
     ('I do not like this restaurant', 'neg'),
     ('I am tired of this stuff.', 'neg'),
     ("I can't deal with this", 'neg'),
     ('he is my sworn enemy!', 'neg'),
     ('my boss is horrible.', 'neg')
     ]
```


```python
test = [
     ('the beer was good.', 'pos'),
     ('I do not enjoy my job', 'neg'),
     ("I ain't feeling dandy today.", 'neg'),
     ("I feel amazing!", 'pos'),
     ('Gary is a friend of mine.', 'pos'),
     ("I can't believe I'm doing this.", 'neg')
]
```


```python
cl = NaiveBayesClassifier(train)
```


```python
prob_dist = cl.prob_classify("terrific movie it is. Great concept")
print(prob_dist.max())
```

    pos



```python
print(round(prob_dist.prob("pos"), 2))
print(round(prob_dist.prob("neg"), 2))
```

    0.63
    0.37



```python

```


---
**Score: 5**