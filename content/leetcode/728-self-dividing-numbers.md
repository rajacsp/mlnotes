---
title: 728-Self-Dividing-Numbers
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/self-dividing-numbers


```
import pyutil as pyu
pyu.get_local_pyinfo()
```


```
print(pyu.ps2("python-dotenv"))
```


```
from typing import List
```


```
class Solution:
  def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    return [num for num in range(left, right + 1) if all(n != 0 and num % n == 0 for n in map(int, str(num)))]
```


```
new Solution().selfDividingNumbers()
```


---
**Score: 5**