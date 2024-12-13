---
title: Random Timestamp
date: 2024-12-13
author: Your Name
cell_count: 6
score: 5
---

---
title: "Random Timestamp"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
from random import randrange
import datetime
```


```python
def random_date(start,l):
   current = start
   while l >= 0:
      curr = current + datetime.timedelta(minutes=randrange(60))
      yield curr
      l-=1
```


```python
def get_random_timestamp(max):
    startDate = datetime.datetime(2013, 9, 20,13,00)

    for x in random_date(startDate,10):
        #print(x.strftime("%d/%m/%y %H:%M"))

        #print(x)
        timestamp = datetime.datetime.timestamp(x)
        print(int(timestamp))
```


```python
get_random_timestamp(20)
```

    1379697780
    1379697540
    1379697960
    1379697420
    1379697420
    1379699760
    1379698680
    1379697120
    1379697660
    1379696460
    1379696820



```python

```


---
**Score: 5**