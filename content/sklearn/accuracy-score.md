---
title: Accuracy-Score
date: 2024-12-14
author: Your Name
cell_count: 5
score: 5
---

---
title: "Accuracy Score"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
from sklearn.metrics import accuracy_score
```


```python
y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
score1 = accuracy_score(y_true, y_pred)    
print(score1)
```

    0.5



```python
score2 = accuracy_score(y_true, y_pred, normalize=False)
print(score2)
```

    2



```python

```


---
**Score: 5**