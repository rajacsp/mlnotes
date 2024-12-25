---
title: Radar-Simple-2
date: 2024-12-25
author: Your Name
cell_count: 2
score: 0
---

---
title: "Radar Simple"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
# copied from https://python-graph-gallery.com/390-basic-radar-chart/

# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# Set data
df = pd.DataFrame({
'group': ['A','B','C','D'],
    
'java': [38, 1.5, 30, 4],
'python': [29, 10, 9, 34],
'numpy': [8, 39, 23, 24],
'scipy': [7, 31, 33, 14],
'flask': [28, 15, 32, 14],
})
 
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,40)
 
# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')
 
# Fill area
ax.fill(angles, values, 'b', alpha=0.1)
```




    [<matplotlib.patches.Polygon at 0x119b9c160>]




    
![png](/mlnotes/images/radar-simple-2_1_1.png)
    



---
**Score: 0**