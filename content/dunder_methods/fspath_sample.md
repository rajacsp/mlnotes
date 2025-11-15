---
title: Fspath Sample
date: 2025-11-14
author: Your Name
cell_count: 6
score: 5
---

```python

```


```python
import os

class MyPath:
    def __init__(self, path):
        self.path = path

    def __fspath__(self):
        return self.path
```


```python
p = MyPath("example.txt")

# Python will call __fspath__ internally
print(os.fspath(p))   # Output: example.txt

# You can now use it directly with file operations
# with open(p, "w") as f:
#     f.write("Hello!")
```

    example.txt



```python
# Read the content
with open(p, "r") as f:
    content = f.read()
```


```python
print(content)
```

    one
    two



```python

```


---
**Score: 5**