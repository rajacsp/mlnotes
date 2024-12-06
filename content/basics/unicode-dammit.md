---
title: Unicode-Dammit
date: 2024-12-06
author: Your Name
cell_count: 9
score: 5
---

---
title: "Unicode Dammit"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from bs4 import UnicodeDammit
```


```python
print("inside main method")
    
dammit = UnicodeDammit(b"Sacr\xc3\xa9 bleu!")


```

    inside main method



```python
print(type(dammit))
```

    <class 'bs4.dammit.UnicodeDammit'>



```python
print(dammit.unicode_markup)
```

    SacrÃ© bleu!



```python
print(type(dammit.unicode_markup))
```

    <class 'str'>



```python
print(dammit.original_encoding)
```

    iso-8859-9



```python
print(type(dammit.original_encoding))
```

    <class 'str'>



```python

```


---
**Score: 5**