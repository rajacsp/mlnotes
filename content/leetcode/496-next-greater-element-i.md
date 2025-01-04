---
title: 496-Next-Greater-Element-I
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/next-greater-element-i


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
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    numToNextGreater = {}
    stack = []

    for num in nums2:
      while stack and stack[-1] < num:
        numToNextGreater[stack.pop()] = num
      stack.append(num)

    return [numToNextGreater.get(num, -1) for num in nums1]
```


```
new Solution().nextGreaterElement()
```


---
**Score: 5**