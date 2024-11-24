---
title: Logging 1
date: 2024-11-24
author: Your Name
cell_count: 6
score: 5
---

---
title: "Logging"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import logging

logger = logging.getLogger()
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger.setLevel(logging.DEBUG)
logging.debug("test")
```

    DEBUG:root:test



```python
def do_sample():
    for x in range(10):
        logging.info('one')
        print(x)
```


```python
do_sample()
```

    INFO:root:one
    INFO:root:one
    INFO:root:one
    INFO:root:one
    INFO:root:one
    INFO:root:one
    INFO:root:one
    INFO:root:one
    INFO:root:one
    INFO:root:one


    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python

```


```python

```


---
**Score: 5**