---
title: 3-Longest-Substring-Without-Repeating-Chars
date: 2024-12-25
author: Your Name
cell_count: 8
score: 5
---

```python
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
```


```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: ml311; pyv: 3.11.10 (main, Oct  3 2024, 07:29:13) [GCC 11.2.0]'




```python
print(pyu.ps2("scipy"))
```

    scipy==1.14.1
    



```python

```


```python
from collections import Counter

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


```python
Solution().lengthOfLongestSubstring("one")
```




    3




```python
Solution().lengthOfLongestSubstring("pwwkew")
```




    3




```python

```


---
**Score: 5**