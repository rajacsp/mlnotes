---
title: Porter-Stemmer
date: 2024-12-07
author: Your Name
cell_count: 8
score: 5
---

---
title: "Porter Stemmer"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from nltk.stem.porter import PorterStemmer
```


```python
stemmer = PorterStemmer()
```


```python
words =  [
    "radios",
    "colors",
    "mumbled"
]
```


```python
words
```




    ['radios', 'colors', 'mumbled']




```python
result = [stemmer.stem(word) for word in words]
```


```python
result
```




    ['radio', 'color', 'mumbl']




```python

```


---
**Score: 5**