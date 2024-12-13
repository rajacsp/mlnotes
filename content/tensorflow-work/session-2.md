---
title: Session-2
date: 2024-12-13
author: Your Name
cell_count: 10
score: 10
---

---
title: "Session 2"
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
a = tf.constant(1.2)
```


```python
b = tf.constant(2.8)
```


```python
c = a + b
```


```python
c
```




    <tf.Tensor 'add:0' shape=() dtype=float32>




```python
# You can see the value is not updated as it is just a model
```


```python
with tf.Session() as sess:
    print(sess.run(c))
    print(c)
```

    4.0
    Tensor("add:0", shape=(), dtype=float32)



```python
c
```




    <tf.Tensor 'add:0' shape=() dtype=float32>




```python

```


---
**Score: 10**