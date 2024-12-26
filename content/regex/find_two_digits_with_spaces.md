---
title: Find Two Digits With Spaces
date: 2024-12-26
author: Your Name
cell_count: 7
score: 5
---

---
title: "Find Two Digits with Spaces"
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
text = "It happened on Feb 21 at 3:30"

answer= re.findall(r'\b\d{2}\b', text)
print(answer)
```

    ['21', '30']



```python
# To match only two digits with spaces
answers = re.findall(r'\s\d{2}\s', text)
```


```python
for a in answers:
    print(a.strip())
```

    21



```python
# To do
# Find 3:30 or 3.30 or 3-30 alone
```


```python

```


---
**Score: 5**