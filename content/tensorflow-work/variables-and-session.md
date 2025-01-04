---
title: Variables-And-Session
date: 2025-01-04
author: Your Name
cell_count: 4
score: 0
---

---
title: "Variables and Session"
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
a = tf.ones((2, 2))
b = tf.Variable(tf.zeros((2, 2)), name = 'weights')

with tf.Session() as sess:
    print(sess.run(a))
    sess.run(tf.initialize_all_variables()) # commenting out this line will throw exception
    print(sess.run(b))
```

    [[1. 1.]
     [1. 1.]]
    WARNING:tensorflow:From /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/tensorflow/python/util/tf_should_use.py:193: initialize_all_variables (from tensorflow.python.ops.variables) is deprecated and will be removed after 2017-03-02.
    Instructions for updating:
    Use `tf.global_variables_initializer` instead.
    [[0. 0.]
     [0. 0.]]


##### Notes

Tensorflow variables must be initialized before they have values


---
**Score: 0**