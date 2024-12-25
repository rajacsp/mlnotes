---
title: Current-Directory
date: 2024-12-25
author: Your Name
cell_count: 6
score: 5
---

---
title: "Current Directory"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import os
```


```python
dirpath = os.getcwd()
print("current directory is : " + dirpath)
```

    current directory is : /Users/rajacsp/projects/mlnotes/content/python/basics



```python
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
```

    Directory name is : basics



```python
scriptpath = os.path.realpath("one")
print("Script path is : " + scriptpath)
```

    Script path is : /Users/rajacsp/projects/mlnotes/content/python/basics/one



```python

```


---
**Score: 5**