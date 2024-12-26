---
title: 989-Add-To-Array-Form-Of-Integer
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/add-to-array-form-of-integer


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
  def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    for i in reversed(range(len(num))):
      k, num[i] = divmod(num[i] + k, 10)

    while k > 0:
      num = [k % 10] + num
      k //= 10

    return num
```


```
new Solution().addToArrayForm()
```


---
**Score: 5**