---
title: Graph
date: 2024-12-04
author: Your Name
cell_count: 19
score: 15
---

---
title: "Graph"
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
graph = tf.get_default_graph()
```


```python
graph.get_operations()
```




    []




```python
a = tf.constant(2, name = "one")
```


```python
operations = graph.get_operations()
```
operations

```python
b = tf.constant(2, name = "two")
```


```python
b
```




    <tf.Tensor 'two:0' shape=() dtype=int32>




```python
operations
```




    [<tf.Operation 'one' type=Const>]




```python
c = tf.add(a, b, name = "three")
```


```python
c
```




    <tf.Tensor 'three:0' shape=() dtype=int32>




```python
operations
```




    [<tf.Operation 'one' type=Const>,
     <tf.Operation 'one_1' type=Const>,
     <tf.Operation 'three' type=Add>,
     <tf.Operation 'one_2' type=Const>]




```python
session = tf.Session()
```


```python
print(session.run(c))
```

    4



```python
c
```




    <tf.Tensor 'three:0' shape=() dtype=int32>




```python
for op in operations:
    print(op.name)
```

    one



```python
session.close()
```


```python

```


---
**Score: 15**