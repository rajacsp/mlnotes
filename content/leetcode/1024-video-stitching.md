---
title: 1024-Video-Stitching
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/video-stitching


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
  def videoStitching(self, clips: List[List[int]], time: int) -> int:
    ans = 0
    end = 0
    farthest = 0

    clips.sort()

    i = 0
    while farthest < time:
      while i < len(clips) and clips[i][0] <= end:
        farthest = max(farthest, clips[i][1])
        i += 1
      if end == farthest:
        return -1
      ans += 1
      end = farthest

    return ans
```


```
new Solution().videoStitching()
```


---
**Score: 5**