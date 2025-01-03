---
title: Lancaster-Stemmer
date: 2025-01-03
author: Your Name
cell_count: 8
score: 5
---

---
title: "Lancaster Stemmer"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from nltk.stem import LancasterStemmer
```


```python
l_stemmer = LancasterStemmer()
```


```python
print(l_stemmer.stem("hunting"))
```

    hunt



```python
print(l_stemmer.stem("hunting"))
```

    hunt



```python
words = [
    "hunting",
    "bunnies",
    "flies"
]
```


```python
result = [l_stemmer.stem(word) for word in words]
```


```python
result
```




    ['hunt', 'bunny', 'fli']




---
**Score: 5**