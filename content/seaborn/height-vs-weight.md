---
title: Height-Vs-Weight
date: 2024-12-07
author: Your Name
cell_count: 8
score: 5
---

```python
!python --version
```

    Python 3.10.5



```python
# !pip install seaborn
```


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
```


```python
data = {
    "Height": [150, 160, 165, 170, 175, 180, 185],
    "Weight": [50, 60, 65, 70, 75, 80, 85],
    "Gender": ["Female", "Male", "Female", "Male", "Female", "Male", "Female"]
}
```


```python
df = pd.DataFrame(data)
```


```python
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
scatter_plot = sns.scatterplot(data=df, x="Height", y="Weight", hue="Gender", style="Gender", s=100)

plt.title("Height vs. Weight by Gender", fontsize=16)
plt.xlabel("Height (cm)", fontsize=12)
plt.ylabel("Weight (kg)", fontsize=12)
plt.legend(title="Gender")
plt.show()
```


    
![png](/mlnotes/images/height-vs-weight_5_0.png)
    



```python

```


```python

```


---
**Score: 5**