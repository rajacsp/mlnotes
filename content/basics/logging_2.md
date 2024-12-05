---
title: Logging 2
date: 2024-12-05
author: Your Name
cell_count: 6
score: 5
---

---
title: "Logging 2"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import logging

logger = logging.getLogger()
#fhandler = logging.FileHandler(filename='mylog.log', mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)
```


```python
def do_sample():
    for x in range(10):
        logger.info('one')
        print(x)
```


```python
do_sample()
```

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
logging.error('hello!')
logging.debug('This is a debug message')
logging.info('this is an info message')
logging.warning('tbllalfhldfhd, warning.')
```

More:

https://stackoverflow.com/questions/18786912/get-output-from-the-logging-module-in-ipython-notebook


---
**Score: 5**