---
title: 10-Regular-Expression-Matching
date: 2024-12-25
author: Your Name
cell_count: 8
score: 5
---

```python
# https://leetcode.com/problems/regular-expression-matching/description/
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
# print(pyu.ps2("scipy"))
```


```python

```


```python
class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    m = len(s)
    n = len(p)
    # dp[i][j] := True if s[0..i) matches p[0..j)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    def isMatch(i: int, j: int) -> bool:
      return j >= 0 and p[j] == '.' or s[i] == p[j]

    for j, c in enumerate(p):
      if c == '*' and dp[0][j - 1]:
        dp[0][j + 1] = True

    for i in range(m):
      for j in range(n):
        if p[j] == '*':
          noRepeat = dp[i + 1][j - 1]  # Min index of '*' is 1
          doRepeat = isMatch(i, j - 1) and dp[i][j + 1]
          dp[i + 1][j + 1] = noRepeat or doRepeat
        elif isMatch(i, j):
          dp[i + 1][j + 1] = dp[i][j]

    return dp[m][n]
```


```python
Solution().isMatch("aa", "a")
```




    False




```python
Solution().isMatch("aa", "a*")
```




    True




```python
Solution().isMatch("aa", "a*")
```


---
**Score: 5**