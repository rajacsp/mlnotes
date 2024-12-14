---
title: Class
date: 2024-12-14
author: Your Name
cell_count: 10
score: 10
---

---
title: "Class Basics"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return repr((self.name, self.age, self.salary))
```


```python
employees = [
    Employee('Peter', 21, 6),
    Employee('Kevin', 22, 4),
    Employee('Simon', 21, 8)
]
```


```python
employees
```




    [('Peter', 21, 6), ('Kevin', 22, 4), ('Simon', 21, 8)]




```python
# sorting

sorted(employees, key = lambda e: e.salary)
```




    [('Kevin', 22, 4), ('Peter', 21, 6), ('Simon', 21, 8)]




```python
sorted(employees, key = lambda e: -e.salary)
```




    [('Simon', 21, 8), ('Peter', 21, 6), ('Kevin', 22, 4)]




```python
from operator import itemgetter, attrgetter
sorted(employees, key=attrgetter('age'))
```




    [('Peter', 21, 6), ('Simon', 21, 8), ('Kevin', 22, 4)]




```python
young_employees = sorted(employees, key=attrgetter('age'), reverse=False)
```


```python
young_employees
```




    [('Peter', 21, 6), ('Simon', 21, 8), ('Kevin', 22, 4)]




```python

```


---
**Score: 10**