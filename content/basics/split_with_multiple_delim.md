---
title: Split With Multiple Delim
date: 2024-12-04
author: Your Name
cell_count: 7
score: 5
---

---
title: "Split with Multiple"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import re
```


```python
content = "Hey, you - what are you doing here!?"
```


```python
contents = re.findall(r"[\w']+", content)
```


```python
contents
```




    ['Hey', 'you', 'what', 'are', 'you', 'doing', 'here']




```python
for c in contents:
    print(c)
```

    Hey
    you
    what
    are
    you
    doing
    here



```python

```


---
**Score: 5**