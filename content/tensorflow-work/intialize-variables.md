---
title: Intialize-Variables
date: 2024-12-04
author: Your Name
cell_count: 5
score: 5
---

---
title: "Initialize Variables"
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
init_op = tf.global_variables_initializer()
```


```python
session = tf.Session()
```


```python
# initialize variables
session.run(init_op)
```


---
**Score: 5**