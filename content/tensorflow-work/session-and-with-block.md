---
title: Session-And-With-Block
date: 2025-05-17
author: Your Name
cell_count: 8
score: 5
---

---
title: "Session and With Block"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
import tensorflow as tf

import os

# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```


```python
a = tf.Variable(2)
```


```python
b = a * 4
```


```python
b
```




    <tf.Tensor 'mul:0' shape=() dtype=int32>




```python
init_op = tf.initialize_all_variables()
```


```python
with tf.Session() as session:
    session.run(init_op)
    result = session.run(a + b)
    print(result)
```

    10



```python

```


---
**Score: 5**