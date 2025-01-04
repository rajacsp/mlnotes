---
title: Textblob-Classifier-2
date: 2025-01-04
author: Your Name
cell_count: 8
score: 5
---

---
title: "TextBlob Classifier 2"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
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

#print(train)

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
blob = TextBlob("The beer is good. But the hangover is horrible.", classifier=cl)
```


```python
for s in blob.sentences:
    print(s)
    print(s.classify())
```

    The beer is good.
    pos
    But the hangover is horrible.
    neg



```python
print(cl.accuracy(test))
```

    0.8333333333333334



```python

```


---
**Score: 5**