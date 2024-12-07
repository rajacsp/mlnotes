---
title: Basic-Vector
date: 2024-12-07
author: Your Name
cell_count: 9
score: 5
---

---
title: "Basic Vector"
author: "Raja CSP Raman"
date: 2019-05-02
description: "-"
type: technical_note
draft: false
---

```python
from gensim import corpora, models, similarities
```


```python
corpus = [
    [(0, 1.0), (1, 1.0), (2, 1.0)],
    [(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],
    [(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],
    [(0, 1.0), (4, 2.0), (7, 1.0)]    
]
```


```python
corpus
```




    [[(0, 1.0), (1, 1.0), (2, 1.0)],
     [(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],
     [(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],
     [(0, 1.0), (4, 2.0), (7, 1.0)]]




```python
tfidf = models.TfidfModel(corpus)
```


```python
vec = [(0, 1), (4, 1)]
```


```python
print(tfidf[vec])
```

    [(0, 0.9236102512530996), (4, 0.383332888988391)]


Tf-Idf, a simple transformation which takes documents represented as bag-of-words counts and applies a weighting which discounts common terms (or, equivalently, promotes rare terms). 

It also scales the resulting vector to unit length (in the Euclidean norm).


```python

```


---
**Score: 5**