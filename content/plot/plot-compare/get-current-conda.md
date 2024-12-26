---
title: Get-Current-Conda
date: 2024-12-26
author: Your Name
cell_count: 3
score: 0
---

```python
import sys
import os

# Get the parent directory of the current notebook
current_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir, "../../"))  # Adjust the path to reach the `notebooks` folder

# Add the parent directory to sys.path
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Now you can import pyutil
import pyutil

# Example usage of pyutil
pyutil.get_myenv()  # Replace with actual function name
```




    'ml312-2024'




```python

```

    ml312-2024



```python

```


---
**Score: 0**