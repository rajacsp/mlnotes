---
title: Static-Decorator
date: 2024-12-06
author: Your Name
cell_count: 8
score: 5
---

---
title: "Static Decorator"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
class Example:
    name = "Example"

    @staticmethod
    def static():
        print("%s static() called" % Example.name)
```


```python
class Offspring1(Example):
    name = "Offspring1"
```


```python
class Offspring2(Example):
    name = "Offspring2"

    @staticmethod
    def static():
        print("%s static() called" % Offspring2.name)
```


```python
Example.static()
```

    Example static() called



```python
Offspring1.static()
```

    Example static() called



```python
Offspring2.static()
```

    Offspring2 static() called



```python

```


---
**Score: 5**