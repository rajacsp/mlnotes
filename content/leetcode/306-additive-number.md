---
title: 306-Additive-Number
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/additive-number


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
  def isAdditiveNumber(self, num: str) -> bool:
    n = len(num)

    def dfs(firstNum: int, secondNum: int, s: int) -> bool:
      if s == len(num):
        return True

      thirdNum = firstNum + secondNum
      thirdNumStr = str(thirdNum)

      return num.find(thirdNumStr, s) == s and dfs(secondNum, thirdNum, s + len(thirdNumStr))

    # num[0..i] = firstNum
    for i in range(n // 2):
      if i > 0 and num[0] == '0':
        return False
      firstNum = int(num[:i + 1])
      # num[i + 1..j] = secondNum
      # Len(thirdNum) >= max(len(firstNum), len(secondNum))
      j = i + 1
      while max(i, j - i) < n - j:
        if j > i + 1 and num[i + 1] == '0':
          break
        secondNum = int(num[i + 1:j + 1])
        if dfs(firstNum, secondNum, j + 1):
          return True
        j += 1

    return False
```


```
new Solution().isAdditiveNumber()
```


---
**Score: 5**