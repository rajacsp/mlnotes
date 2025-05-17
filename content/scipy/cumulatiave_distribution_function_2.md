---
title: Cumulatiave Distribution Function 2
date: 2025-05-17
author: Your Name
cell_count: 3
score: 0
---

title: "Cumulative Distribution Function 2"
author: "Raja CSP Raman"
date: 2019-05-06
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import matplotlib.pyplot as plt
```


```python
data = np.loadtxt('random_timestamp.txt')

print(data)

sorted_data = np.sort(data)

yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)

plt.plot(sorted_data,yvals)

plt.show()
```

    [1.37969832e+09 1.37969826e+09 1.37969682e+09 1.37969814e+09
     1.37969802e+09 1.37969856e+09 1.37969664e+09 1.37969676e+09
     1.37969940e+09 1.37969976e+09 1.37969850e+09]



    
![png](/mlnotes/images/cumulatiave_distribution_function_2_2_1.png)
    



---
**Score: 0**