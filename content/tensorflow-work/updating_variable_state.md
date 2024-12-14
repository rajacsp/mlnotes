---
title: Updating Variable State
date: 2024-12-14
author: Your Name
cell_count: 4
score: 0
---

---
title: "Updating Variable State"
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
a = tf.Variable(0, name = 'counter')

b = tf.add(a, tf.constant(2))

# update a with b value (which means a+1)
update = tf.assign(a, b)
```


```python
with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())

        print(sess.run(a))

        for _ in range(3):
            sess.run(update)
            print(sess.run(a))
```

    0
    2
    4
    6



---
**Score: 0**