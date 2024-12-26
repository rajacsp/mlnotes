---
title: 159-Longest-Substring-With-At-Most-Two-Distinct-Characters
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters


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
  def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    ans = 0
    distinct = 0
    count = [0] * 128

    l = 0
    for r, c in enumerate(s):
      count[ord(c)] += 1
      if count[ord(c)] == 1:
        distinct += 1
      while distinct == 3:
        count[ord(s[l])] -= 1
        if count[ord(s[l])] == 0:
          distinct -= 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans
```


```
new Solution().lengthOfLongestSubstringTwoDistinct()
```


---
**Score: 5**