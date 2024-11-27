---
title: Fetching-Variable-State
date: 2024-11-27
author: Your Name
cell_count: 4
score: 0
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
a = tf.constant(2)
b = tf.constant(3)

c = tf.add(a, b)
d = tf.multiply(a, b)

'''
    tf.mul, tf.sub and tf.neg are deprecated in favor of tf.multiply, tf.subtract and tf.negative.
        https://stackoverflow.com/questions/42217059/tensorflowattributeerror-module-object-has-no-attribute-mul
'''

with tf.Session() as sess:
    # Calling sess.run(var) on a tf.Session() retrieves its value
    # We can retrieve multiple variables simultaneously like below
    result = sess.run([d, c])
    print(result)
```

    [6, 5]



```python

```


---
**Score: 0**