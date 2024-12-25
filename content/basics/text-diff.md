---
title: Text-Diff
date: 2024-12-25
author: Your Name
cell_count: 10
score: 10
---

---
title: "Text Diff"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import difflib
```


```python
str1 = "I understand how customers do their choice. Difference"
str2 = "I understand how customers do their choice."
```


```python
seq = difflib.SequenceMatcher(None, str1, str2)
```


```python
d = seq.ratio()*100
```


```python
d
```




    88.65979381443299




```python
def get_similarity(str1, str2):
    seq = difflib.SequenceMatcher(None, str1, str2)
    d = seq.ratio()*100
    return d
```


```python
get_similarity(str1, str2)
```




    88.65979381443299




```python
get_similarity("Toronto is nice", "Toronto is looking nice")
```




    78.94736842105263




```python

```


---
**Score: 10**