---
title: Stemmer-With-Stopwords
date: 2024-12-13
author: Your Name
cell_count: 7
score: 5
---

---
title: "Stemmer with Stopwords"
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
stemmer = SnowballStemmer("english")
```


```python
print(stemmer.stem("having"))
```

    have



```python
stemmer2 = SnowballStemmer("english",  ignore_stopwords = True)
```


```python
print(stemmer2.stem("having"))
```

    having



```python

```


---
**Score: 5**