---
title: Snowball-Stemmer
date: 2024-12-13
author: Your Name
cell_count: 7
score: 5
---

---
title: "Snowball Stemmer"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from nltk.stem.snowball import SnowballStemmer
```


```python
words = [
    "hunting",
    "bunnies",
    "thinking"
]
```


```python
words
```




    ['hunting', 'bunnies', 'thinking']




```python
stemmer = SnowballStemmer("english")
```


```python
result = [stemmer.stem(word) for word in words]
```


```python
result
```




    ['hunt', 'bunni', 'think']




---
**Score: 5**