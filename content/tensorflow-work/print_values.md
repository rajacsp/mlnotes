---
title: Print Values
date: 2024-12-07
author: Your Name
cell_count: 7
score: 5
---

---
title: "Print Values"
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
normal_rv = tf.Variable(tf.truncated_normal([2, 3], stddev=0.1))
```


```python
# Initialize the variables
init_op = tf.initialize_all_variables()
```


```python
with tf.Session() as sess:
    sess.run(init_op)
    
    print(sess.run(normal_rv))
```

    [[ 0.14728771  0.08864368 -0.12002647]
     [-0.10451528 -0.04784236  0.10818603]]


Note: initialize_all_variables is deprecated and removed from 2017


```python

```


---
**Score: 5**