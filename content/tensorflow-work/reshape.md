---
title: Reshape
date: 2024-12-04
author: Your Name
cell_count: 4
score: 0
---

---
title: "Reshape"
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
tf.InteractiveSession()

a = tf.zeros((2, 2))
b = tf.ones((2, 2))

abc = tf.reduce_sum(b, reduction_indices=1).eval()
#rray([2., 2.], dtype=float32)
print(abc)

print(a.get_shape())

# reshape
ef = tf.reshape(a, (1, 4)).eval()
print(ef)
```

    [2. 2.]
    (2, 2)
    [[0. 0. 0. 0.]]


##### Notes:

Tensorflow compuations define a compuation graph that has no numerical value until 

InteractiveSession() will help you to keep a default session open in ipython

In a construction phase, tensorflow programs assemble a graph. 
Then in the execution phase, the session is used to execute ops in the graph

All computations add nodes to global default graph

When you train a model you use variables to hold and update parameters.
Variables are in-memory buffers containing tensors.


---
**Score: 0**