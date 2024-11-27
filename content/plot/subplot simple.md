---
title: Subplot Simple
date: 2024-11-27
author: Your Name
cell_count: 3
score: 0
---

---
title: "Sub Plot Simple"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import matplotlib.pyplot as plt

python_course_green = "#476042"
plt.figure(figsize=(6, 4))
plt.subplot(221) # equivalent to: plt.subplot(2, 2, 1)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11365e1d0>




```python
plt.text(0.5, # x coordinate, 0 leftmost positioned, 1 rightmost
         0.5, # y coordinate, 0 topmost positioned, 1 bottommost
         'subplot(2,2,1)', # the text which will be printed
         horizontalalignment='center', # shortcut 'ha' 
         verticalalignment='center', # shortcut 'va'
         fontsize=20, # can be named 'font' as well
         alpha=.5 # float (0.0 transparent through 1.0 opaque)
         )
plt.subplot(224, facecolor=python_course_green)
plt.text(0.5, 0.5, 
         'subplot(2,2,4)', 
         ha='center', va='center',
         fontsize=20, 
         color="y")

plt.show()
```


    
![png](/mlnotes/images/subplot%20simple_2_0.png)
    



---
**Score: 0**