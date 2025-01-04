---
title: 3-Longest-Substring-Without-Repeating-Characters
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/longest-substring-without-repeating-characters


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
  def lengthOfLongestSubstring(self, s: str) -> int:
    ans = 0
    count = Counter()

    l = 0
    for r, c in enumerate(s):
      count[c] += 1
      while count[c] > 1:
        count[s[l]] -= 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans
```


```
new Solution().lengthOfLongestSubstring()
```


---
**Score: 5**