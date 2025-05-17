---
title: Print-Filenames
date: 2025-05-17
author: Your Name
cell_count: 8
score: 5
---

---
title: "Print Filenames"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
from os import walk
from os import listdir
from os.path import isfile, join
```


```python
path = '/tmp'
```


```python
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
```


```python
onlyfiles
```




    ['.BBE72B41371180178E084EEAF106AED4F350939DB95D3516864A1CC62E7AE82F']




```python
for fle in onlyfiles:
    print(fle)
```

    .BBE72B41371180178E084EEAF106AED4F350939DB95D3516864A1CC62E7AE82F



```python

```


```python

```


---
**Score: 5**