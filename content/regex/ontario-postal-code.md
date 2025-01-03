---
title: Ontario-Postal-Code
date: 2025-01-03
author: Your Name
cell_count: 5
score: 5
---

---
title: "Ontario Postal Code"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import re
```


```python
names = ['M2N1H5', 'M2N 1H5', 'M882J8']

regex_patten = "^[A-Z]\d[A-Z]\s*\d[A-Z]\d"
# starts with Capital letter; it can have zero or one space

for name in names:
    m = re.match(regex_patten, name)

    if(m):
        #print(m.groups())
        print('matched : ', name)
```

    matched :  M2N1H5
    matched :  M2N 1H5



    \d - digit
    \D - non-digit
    \s - whitespace
    \S - non-whitespace
    \w - alphanumeric
    \W - non-alphanumeric



```python

```


---
**Score: 5**