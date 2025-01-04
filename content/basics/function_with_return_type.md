---
title: Function With Return Type
date: 2025-01-04
author: Your Name
cell_count: 8
score: 5
---

---
title: "Function With Return Type"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
def square(a):
    return a * a
```


```python
print(square(5))
```

    25



```python
def square(a:int) -> int:
    return a * a
```


```python
print(square(4))
```

    16



```python
def square_1(a:int) -> str:
    return a * a
```


```python
print(square_1(15))
```

    225


in the above function, even though we say the return type is string, we are returning an int. 


---
**Score: 5**