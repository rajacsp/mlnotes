---
title: Ontario-Postal-Code
date: 2024-11-17
author: Your Name
cell_count: 3
score: 0
---

```python
import re
```


```python
names = ['M2N1H5', 'M2N 1H5', 'M882J8']

regex_patten = "^[A-Z]\\d[A-Z]\\s*\\d[A-Z]\\d"
# starts with Capital letter; it can have zero or one space

for name in names:
    m = re.match(regex_patten, name)

    if(m):
        #print(m.groups())
        print('matched : ', name)
```

    matched :  M2N1H5
    matched :  M2N 1H5



```python

```


---
**Score: 0**