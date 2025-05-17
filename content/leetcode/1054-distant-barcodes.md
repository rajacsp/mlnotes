---
title: 1054-Distant-Barcodes
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/distant-barcodes


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
  def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
    ans = [0] * len(barcodes)
    count = Counter(barcodes)
    i = 0  # ans' index
    maxNum = max(count, key=count.get)

    def fillAns(num: int) -> None:
      nonlocal i
      while count[num]:
        ans[i] = num
        i = i + 2 if i + 2 < len(barcodes) else 1
        count[num] -= 1

    fillAns(maxNum)
    for num in count.keys():
      fillAns(num)

    return ans
```


```
new Solution().rearrangeBarcodes()
```


---
**Score: 5**