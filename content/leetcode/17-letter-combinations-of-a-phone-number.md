---
title: 17-Letter-Combinations-Of-A-Phone-Number
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/letter-combinations-of-a-phone-number


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
  def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
      return []

    digitToLetters = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    ans = []

    def dfs(i: int, path: List[chr]) -> None:
      if i == len(digits):
        ans.append(''.join(path))
        return

      for letter in digitToLetters[ord(digits[i]) - ord('0')]:
        path.append(letter)
        dfs(i + 1, path)
        path.pop()

    dfs(0, [])
    return ans
```


```
new Solution().letterCombinations()
```


---
**Score: 5**