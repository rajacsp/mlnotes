---
title: Cistem-Stemmer
date: 2025-01-03
author: Your Name
cell_count: 8
score: 5
---

---
title: "Cistem Stemmer"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from nltk.stem.cistem import Cistem
```


```python
c_stemmer = Cistem()
```


```python
print(c_stemmer.stem("filtering"))
```

    filtering



```python
print(c_stemmer.segment("filtering"))
```

    ('filtering', '')



```python
print(c_stemmer.segment("Ausgefeiltere"))
```

    ('ausgefeilt', 'ere')


* segment method will return both the stem and the rest that was removed at the end


```python

```


---
**Score: 5**