---
title: Two
date: 2024-12-07
author: Your Name
cell_count: 5
score: 5
---

```python
!python --version
```

    Python 3.10.5



```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
```


```python
# Load the dataset
tips = sns.load_dataset("tips")
```


```python
# Create a PairGrid with regression and histogram plots
g = sns.PairGrid(tips, diag_sharey=False, hue="sex", palette="Set2")
g.map_upper(sns.scatterplot, alpha=0.8)
g.map_lower(sns.kdeplot, fill=True, alpha=0.7)
g.map_diag(sns.histplot, kde=True)

# Add a title
g.fig.suptitle("Pairwise Relationships in Tips Dataset", fontsize=16, y=1.02)

# Customize legend
g.add_legend(title="Gender", adjust_subtitles=True)

# Show plot
plt.show()
```


    
![png](/mlnotes/images/two_3_0.png)
    



```python

```


---
**Score: 5**