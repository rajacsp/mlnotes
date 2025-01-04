---
title: Linear Vs Binary Timeit
date: 2025-01-04
author: Your Name
cell_count: 7
score: 5
---

---
title: "Timeit on Linear and Binary"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import timeit
```


```python
def linear_search(lys, element):  
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1
```


```python
def binary_search(lys, val):  
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
```


```python
list = [1, 2, 5, 6]
```


```python
SETUP_CODE = ''' 
from __main__ import linear_search, binary_search
from random import randint'''
      
TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
linear_search(mylist, find) 
'''

# timeit.repeat statement 
times = timeit.repeat(setup = SETUP_CODE, 
                      stmt = TEST_CODE, 
                      repeat = 3, 
                      number = 10000) 

# priniting minimum exec. time 
print('Linear search time: {}'.format(min(times))) 

TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
binary_search(mylist, find) 
'''
```

    Linear search time: 5.699102585989749



```python
# timeit.repeat statement 
times = timeit.repeat(setup = SETUP_CODE, 
                      stmt = TEST_CODE, 
                      repeat = 3, 
                      number = 10000) 
  
# priniting minimum exec. time 
print('Binary search time: {}'.format(min(times)))
```

    Binary search time: 3.0898517410096247



---
**Score: 5**