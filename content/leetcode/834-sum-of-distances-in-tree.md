---
title: 834-Sum-Of-Distances-In-Tree
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sum-of-distances-in-tree


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
  def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
    ans = [0] * N
    count = [1] * N
    tree = defaultdict(set)

    for u, v in edges:
      tree[u].add(v)
      tree[v].add(u)

    def postorder(node, parent=None):
      for child in tree[node]:
        if child == parent:
          continue
        postorder(child, node)
        count[node] += count[child]
        ans[node] += ans[child] + count[child]

    def preorder(node, parent=None):
      for child in tree[node]:
        if child == parent:
          continue
        # count[child] nodes are 1 step closer from child than parent
        # (N - count[child]) nodes are 1 step farther from child than parent
        ans[child] = ans[node] - count[child] + (N - count[child])
        preorder(child, node)

    postorder(0)
    preorder(0)
    return ans
```


```
new Solution().sumOfDistancesInTree()
```


---
**Score: 5**