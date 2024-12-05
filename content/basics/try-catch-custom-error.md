---
title: Try-Catch-Custom-Error
date: 2024-12-05
author: Your Name
cell_count: 7
score: 5
---

---
title: "Try Catch with Custom Error"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
class NegativeMarksError(Exception):
   pass
```


```python
def check_marks(mark):
    try:
        
        if(mark < 0):
            raise NegativeMarksError
        
        if(mark > 50):
            print('pass')
        else:
            print('fail')
    except ValueError:
        print('ValueError: Some value error')
    except TypeError:
        print('TypeError: Cannot convert into int')
    except NegativeMarksError:
        print('Negative Marks are not allowed')
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

    Negative Marks are not allowed



```python

```


---
**Score: 5**