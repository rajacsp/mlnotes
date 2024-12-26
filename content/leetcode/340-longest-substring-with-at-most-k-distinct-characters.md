---
title: 340-Longest-Substring-With-At-Most-K-Distinct-Characters
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters


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
  def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    ans = 0
    distinct = 0
    count = Counter()

    l = 0
    for r, c in enumerate(s):
      count[c] += 1
      if count[c] == 1:
        distinct += 1
      while distinct == k + 1:
        count[s[l]] -= 1
        if count[s[l]] == 0:
          distinct -= 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans
```


```
new Solution().lengthOfLongestSubstringKDistinct()
```


---
**Score: 5**