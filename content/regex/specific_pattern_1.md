---
title: Specific Pattern 1
date: 2024-12-03
author: Your Name
cell_count: 5
score: 5
---

---
title: "Specific Pattern 1"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
source: https://stackoverflow.com/questions/56232268/extract-word-form-string-using-regex-word-boundaries-in-python
---

```python
import re
```


```python
fn = "DC_QnA_bo_v.15.12.3_DE_duplicates.xlsx"
rgx = re.compile('\b_[A-Z]{2}\b')
print(re.findall(rgx, fn))
```

    []



```python
rgx = re.compile('(?<=_)[A-Z]+(?=_)')
print(re.findall(rgx, fn))
```

    ['DE']



```python

```


---
**Score: 5**