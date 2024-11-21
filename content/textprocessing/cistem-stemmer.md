---
title: Cistem-Stemmer
date: 2024-11-21
author: Your Name
cell_count: 6
score: 5
---

```python
from nltk.stem.cistem import Cistem
```


```python
c_stemmer = Cistem()
```


```python
c_stemmer.stem("filtering")
```




    'filtering'




```python
c_stemmer.segment("filtering")
```




    ('filtering', '')




```python
c_stemmer.segment("Ausgefeiltere")
```




    ('ausgefeilt', 'ere')



segment method will return both the stem and the rest that was removed at the end


---
**Score: 5**