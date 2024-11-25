---
title: Fuzzy-String-Ratio
date: 2024-11-25
author: Your Name
cell_count: 4
score: 0
---

---
title: "Fuzzy String Ratio"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from fuzzywuzzy import fuzz
```


```python
print(fuzz.ratio("this is a test", "this is a test!"))
```

    97



```python
print(fuzz.ratio("this is a cup", "this is a world cup"))
```

    81



---
**Score: 0**