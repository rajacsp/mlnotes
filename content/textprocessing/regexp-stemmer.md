---
title: Regexp-Stemmer
date: 2024-12-13
author: Your Name
cell_count: 9
score: 5
---

---
title: "Regexp Stemmer"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from nltk.stem import RegexpStemmer
```


```python
re_stemmer = RegexpStemmer("ing$|s$|e$|able$", min=7)
```


```python
words = [
    "wheels",
    "breaking",
    "thrones",
    "breakable"
]
```


```python
words
```




    ['wheels', 'breaking', 'thrones', 'breakable']




```python
result = [re_stemmer.stem(word) for word in words]
```


```python
result
```




    ['wheels', 'break', 'throne', 'break']



As the minium length of the string is 7 in the RegexStemmer, 'wheels' is not stemmed properly


```python

```


---
**Score: 5**