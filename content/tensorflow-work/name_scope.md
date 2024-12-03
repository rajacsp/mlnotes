---
title: Name Scope
date: 2024-12-03
author: Your Name
cell_count: 6
score: 5
---

---
title: "Name Scope"
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
# to clear the graph before new nodes
tf.reset_default_graph()

with tf.name_scope("march"):
    a = tf.constant(1, name = 'a')
    print(a.name)
    
    b = tf.Variable(2, name = 'b')
    print(b.name)
```

    march/a:0
    march/b:0



```python
a
```




    <tf.Tensor 'march/a:0' shape=() dtype=int32>




```python
print(a.name)
```

    march/a:0



```python
# Note: You can access the variable outside of the scope even after it is assigned.
```


---
**Score: 5**