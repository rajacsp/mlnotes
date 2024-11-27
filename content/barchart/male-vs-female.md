---
title: Male-Vs-Female
date: 2024-11-27
author: Your Name
cell_count: 2
score: 0
---

```python
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('Male', 'Female')
y_pos = np.arange(2)
values = [10,8]
 
plt.bar(y_pos, values, width=0.12, align='center', alpha=0.2)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Male vs Female')
 
plt.show()
```


    
![png](/mlnotes/images/male-vs-female_0_0.png)
    



```python

```


---
**Score: 0**