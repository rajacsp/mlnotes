---
title: 339-Nested-List-Weight-Sum
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/nested-list-weight-sum


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
  def depthSum(self, nestedList: List[NestedInteger]) -> int:
    ans = 0
    depth = 0
    q = deque()

    def addIntegers(nestedList: List[NestedInteger]) -> None:
      for ni in nestedList:
        q.append(ni)

    addIntegers(nestedList)

    while q:
      depth += 1
      for _ in range(len(q)):
        ni = q.popleft()
        if ni.isInteger():
          ans += ni.getInteger() * depth
        else:
          addIntegers(ni.getList())

    return ans
```


```
new Solution().depthSum()
```


---
**Score: 5**