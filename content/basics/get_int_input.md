---
title: Get Int Input
date: 2024-12-07
author: Your Name
cell_count: 5
score: 5
---

---
title: "Get Int Input"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

print((x+y))
```

    Enter a number: one



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-2-d1355a0ae898> in <module>()
    ----> 1 x = int(input("Enter a number: "))
          2 y = int(input("Enter a number: "))
          3 
          4 print((x+y))


    ValueError: invalid literal for int() with base 10: 'one'



```python
# As you see above, python will throw error if you type anything other than number
```


```python
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

print((x+y))
```

    Enter a number: 5
    Enter a number: 6
    11



```python

```


---
**Score: 5**