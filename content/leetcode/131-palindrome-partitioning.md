---
title: 131-Palindrome-Partitioning
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/palindrome-partitioning


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
  def partition(self, s: str) -> List[List[str]]:
    ans = []

    def isPalindrome(s: str) -> bool:
      return s == s[::-1]

    def dfs(s: str, j: int, path: List[str], ans: List[List[str]]) -> None:
      if j == len(s):
        ans.append(path)
        return

      for i in range(j, len(s)):
        if isPalindrome(s[j: i + 1]):
          dfs(s, i + 1, path + [s[j: i + 1]], ans)

    dfs(s, 0, [], ans)
    return ans
```


```
new Solution().partition()
```


---
**Score: 5**