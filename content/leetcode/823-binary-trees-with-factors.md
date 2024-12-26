---
title: 823-Binary-Trees-With-Factors
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-trees-with-factors


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
  def numFactoredBinaryTrees(self, arr: List[int]) -> int:
    kMod = 1_000_000_007
    n = len(arr)
    # dp[i] := # Of binary trees with arr[i] as root
    dp = [1] * n
    arr.sort()
    numToIndex = {a: i for i, a in enumerate(arr)}

    for i, root in enumerate(arr):  # arr[i] is root
      for j in range(i):
        if root % arr[j] == 0:  # arr[j] is left subtree
          right = root // arr[j]
          if right in numToIndex:
            dp[i] += dp[j] * dp[numToIndex[right]]
            dp[i] %= kMod

    return sum(dp) % kMod
```


```
new Solution().numFactoredBinaryTrees()
```


---
**Score: 5**