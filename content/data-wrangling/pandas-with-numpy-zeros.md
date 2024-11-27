---
title: Pandas-With-Numpy-Zeros
date: 2024-11-27
author: Your Name
cell_count: 4
score: 0
---

---
title: "Pandas with Numpy Zeros"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import pandas as pd
```


```python
dtype = [('Col1','int32'), ('Col2','float32'), ('Col3','float32')]
values = np.zeros(20, dtype=dtype)
index = ['Row'+str(i) for i in range(1, len(values)+1)]
```


```python
df = pd.DataFrame(values, index=index)
print(df)
```

           Col1  Col2  Col3
    Row1      0   0.0   0.0
    Row2      0   0.0   0.0
    Row3      0   0.0   0.0
    Row4      0   0.0   0.0
    Row5      0   0.0   0.0
    Row6      0   0.0   0.0
    Row7      0   0.0   0.0
    Row8      0   0.0   0.0
    Row9      0   0.0   0.0
    Row10     0   0.0   0.0
    Row11     0   0.0   0.0
    Row12     0   0.0   0.0
    Row13     0   0.0   0.0
    Row14     0   0.0   0.0
    Row15     0   0.0   0.0
    Row16     0   0.0   0.0
    Row17     0   0.0   0.0
    Row18     0   0.0   0.0
    Row19     0   0.0   0.0
    Row20     0   0.0   0.0



---
**Score: 0**