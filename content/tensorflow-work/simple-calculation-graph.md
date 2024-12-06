---
title: Simple-Calculation-Graph
date: 2024-12-06
author: Your Name
cell_count: 12
score: 10
---

---
title: "Template"
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
# a = (b + c) * (c + 2)
```


```python
const = tf.constant(2.0, name='const')
```


```python
# create variables
b = tf.Variable(2.0, name='b')
c = tf.Variable(1.0, name='c')
```


```python
# Fill the operations
d = tf.add(b, c, name='d')
e = tf.add(c, const, name='e')
```


```python
a = tf.multiply(d, e, name='a')
```


```python
# Variable initialization
init_op = tf.global_variables_initializer()
```


```python
with tf.Session() as sess:
    sess.run(init_op)
    
    a_out = sess.run(a)
    
    print(a_out)
```

    9.0



```python
b = tf.placeholder(tf.float32, [None, 1], name='b')
```


```python
import numpy as np

with tf.Session() as sess:
    sess.run(init_op)
    
    b_out = sess.run(a, feed_dict={b: np.arange(0, 10)[:, np.newaxis]})
    
    print(b_out)
```

    9.0



```python

```


---
**Score: 10**