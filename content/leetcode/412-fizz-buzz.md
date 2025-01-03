---
title: 412-Fizz-Buzz
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/fizz-buzz


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
  def fizzBuzz(self, n: int) -> List[str]:
    d = {3: 'Fizz', 5: 'Buzz'}
    return [''.join([d[k] for k in d if i % k == 0]) or str(i) for i in range(1, n + 1)]
```


```
new Solution().fizzBuzz()
```


---
**Score: 5**