---
title: Negative Lookahead
date: 2025-01-03
author: Your Name
cell_count: 5
score: 5
---

---
title: "Negative Lookahead"
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
test = [ ('i sure like eating pie, but i love donuts', True),
         ('i sure like eating pie, but i hate donuts', True),
         ('i sure hate eating pie, but i like donuts', False) ]
```


```python
rx = re.compile(r"^i ((?!hate|pie).)* pie", re.X)

for t,v in test:
    m = rx.match(t)
    print(t, "==>", "pass" if bool(m) == v else "fail")
```

    i sure like eating pie, but i love donuts ==> pass
    i sure like eating pie, but i hate donuts ==> pass
    i sure hate eating pie, but i like donuts ==> pass



```python

```


---
**Score: 5**