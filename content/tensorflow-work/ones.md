---
title: Ones
date: 2024-12-25
author: Your Name
cell_count: 8
score: 5
---

---
title: "Ones"
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
a = tf.ones([2, 5])
```


```python
a
```




    <tf.Tensor 'ones:0' shape=(2, 5) dtype=float32>




```python
with tf.Session() as sess:
    print(sess.run(a))
```

    [[1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1.]]



```python
b = tf.ones([1, 3], tf.int32)
```


```python
with tf.Session() as sess:
    print(sess.run(b))
```

    [[1 1 1]]



```python

```


---
**Score: 5**