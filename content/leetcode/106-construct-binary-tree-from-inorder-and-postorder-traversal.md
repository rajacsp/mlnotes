---
title: 106-Construct-Binary-Tree-From-Inorder-And-Postorder-Traversal
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal


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
  def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    inToIndex = {num: i for i, num in enumerate(inorder)}

    def build(inStart: int, inEnd: int, postStart: int, postEnd: int) -> Optional[TreeNode]:
      if inStart > inEnd:
        return None

      rootVal = postorder[postEnd]
      rootInIndex = inToIndex[rootVal]
      leftSize = rootInIndex - inStart

      root = TreeNode(rootVal)
      root.left = build(inStart, rootInIndex - 1,  postStart,
                        postStart + leftSize - 1)
      root.right = build(rootInIndex + 1, inEnd,  postStart + leftSize,
                         postEnd - 1)
      return root

    return build(0, len(inorder) - 1, 0, len(postorder) - 1)
```


```
new Solution().buildTree()
```


---
**Score: 5**