---
title: Search
date: 2024-12-03
author: Your Name
cell_count: 6
score: 5
---

---
title: "Search"
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
data = [
    "name['toronto'] = 'One'",
    "state['ontario'] = 'Two'",
    "country['canada']['ca'] = 'Three'",
    "extra['maple'] = 'Four'"
]
```


```python
REGEX = re.compile(r"\['(?P<word>.*?)'\]")
```


```python
for line in data:
    found = REGEX.search(line)
    if found:
        print(found.group('word'))
```

    toronto
    ontario
    canada
    maple



```python

```


---
**Score: 5**