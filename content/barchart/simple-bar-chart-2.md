---
title: Simple-Bar-Chart-2
date: 2024-12-03
author: Your Name
cell_count: 2
score: 0
---

```python
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()
```


    
![png](/mlnotes/images/simple-bar-chart-2_0_0.png)
    



```python

```


---
**Score: 0**