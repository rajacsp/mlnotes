---
title: Try-Catch-Raise-Error
date: 2024-11-25
author: Your Name
cell_count: 6
score: 5
---

---
title: "Try Catch with Raise Error"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
def check_marks(mark):
    try:
        
        if(mark < 0):
            raise ValueError
        
        if(mark > 50):
            print('pass')
        else:
            print('fail')
    except ValueError:
        print('ValueError: Some value error')
    except TypeError:
        print('TypeError: Cannot convert into int')
```


```python
check_marks(10)
```

    fail



```python
check_marks('10')
```

    TypeError: Cannot convert into int



```python
check_marks(-10)
```

    ValueError: Some value error



```python

```


---
**Score: 5**