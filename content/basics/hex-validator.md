---
title: Hex-Validator
date: 2025-01-03
author: Your Name
cell_count: 8
score: 5
---

```python

```


```python
import re

def is_valid_hex_color(color):
    pattern = r'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$'
    return bool(re.match(pattern, color))

# Examples
print(is_valid_hex_color("#FFF"))  # True
print(is_valid_hex_color("#123ABC"))  # True
print(is_valid_hex_color("#123ABCG"))  # False
```

    True
    True
    False



```python
!pip show webcolors | grep "Version:"
```

    Version: 24.11.1



```python

```


```python
import webcolors

def is_valid_hex_color(color):
    try:
        webcolors.hex_to_rgb(color)
        return True
    except ValueError:
        return False

# Examples
print(is_valid_hex_color("#FFF"))  # True
print(is_valid_hex_color("#123ABC"))  # True
print(is_valid_hex_color("#123ABCG"))  # False
```

    True
    True
    False



```python

```


```python
def is_valid_hex_color(color):
    if not color.startswith("#"):
        return False
    if len(color) not in {4, 7}:
        return False
    try:
        int(color[1:], 16)
        return True
    except ValueError:
        return False

# Examples
print(is_valid_hex_color("#FFF"))  # True
print(is_valid_hex_color("#123ABC"))  # True
print(is_valid_hex_color("#123ABCG"))  # False
```

    True
    True
    False



```python

```


---
**Score: 5**