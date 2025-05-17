---
title: Get Full Matches
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

---
title: "Get Full Matches"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import re
from typing import List
```


```python
_RGX = re.compile(r'(.)\1*')
def long_repeat(string: str) -> List[str]:
    return [m.group(0) for m in _RGX.finditer(string)]
```


```python
print(long_repeat('devvvvveeeeeeeeeeeloooooooooper'))
```

    ['d', 'e', 'vvvvv', 'eeeeeeeeeee', 'l', 'ooooooooo', 'p', 'e', 'r']



```python
print(long_repeat('country'))
```

    ['c', 'o', 'u', 'n', 't', 'r', 'y']



```python
# to do:
# Ignore single characters
```


---
**Score: 5**