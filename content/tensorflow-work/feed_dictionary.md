---
title: Feed Dictionary
date: 2024-12-03
author: Your Name
cell_count: 3
score: 0
---

---
title: "Feed Dictionary"
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
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.multiply(a, b)

with tf.Session() as sess:
    print(sess.run([c], feed_dict={a:[2], b: [3]}))
```

    [array([6.], dtype=float32)]



---
**Score: 0**