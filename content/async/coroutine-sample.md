---
title: Coroutine-Sample
date: 2024-12-07
author: Your Name
cell_count: 3
score: 0
---

```python
import asyncio 
import time

async def test():
    print('inside test')

async def foo():
    await test()  # No exception raised.
    print('foo')
```


```python
foo()
```




    <coroutine object foo at 0x7f54f8e83940>




```python

```


---
**Score: 0**