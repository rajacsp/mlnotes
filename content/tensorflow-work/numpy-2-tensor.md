---
title: Numpy-2-Tensor
date: 2024-12-13
author: Your Name
cell_count: 3
score: 0
---

---
title: "Numpy 2 Tensor"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
import tensorflow as tf
import numpy as np
import os

# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```


```python
a = np.zeros((3, 3))
ta = tf.convert_to_tensor(a)

with tf.Session() as sess:
    print(sess.run(ta))
```

    [[0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]]



---
**Score: 0**