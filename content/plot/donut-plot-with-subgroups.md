---
title: Donut-Plot-With-Subgroups
date: 2024-12-13
author: Your Name
cell_count: 7
score: 5
---

---
title: "Donut Plot with subgroups"
author: "Rj"
date: 2020-08-20
description: "Donut Plot"
type: technical_note
draft: false
---
Source:

https://python-graph-gallery.com/163-donut-plot-with-subgroups/


```python
# Libraries
import matplotlib.pyplot as plt

# Make data: I have 3 groups and 7 subgroups
group_names=['groupA', 'groupB', 'groupC']
group_size=[12,11,30]
subgroup_names=['A.1', 'A.2', 'A.3', 'B.1', 'B.2', 'C.1', 'C.2', 'C.3', 'C.4', 'C.5']
subgroup_size=[4,3,5,6,5,10,5,5,4,6]

# Create colors
a, b, c=[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]

# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.6), b(0.6), c(0.6)] )
plt.setp( mypie, width=0.3, edgecolor='white')

# Second Ring (Inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3, labels=subgroup_names, labeldistance=0.7, colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), c(0.6), c(0.5), c(0.4), c(0.3), c(0.2)])
plt.setp( mypie2, width=0.4, edgecolor='white')
plt.margins(0,0)

# show it
plt.show()
```


    
![png](/mlnotes/images/donut-plot-with-subgroups_2_0.png)
    



```python
# Make data: I have 3 groups and 7 subgroups
group_names = ['groupA', 'groupB']
group_size = [12,11]
subgroup_names = ['A.1', 'A.2', 'A.3', 'B.1', 'B.2']
subgroup_size = [4,3,5,6,5]

# Create colors
a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]

# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.6), b(0.6)] )
plt.setp( mypie, width=0.3, edgecolor='white')

# Second Ring (Inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3, labels=subgroup_names, 
                labeldistance=0.7, 
                colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), c(0.6), c(0.5), c(0.4), c(0.3), c(0.2)]
            )
plt.setp( mypie2, width=0.4, edgecolor='white')
plt.margins(0,0)

# show it
plt.show()
```


    
![png](/mlnotes/images/donut-plot-with-subgroups_3_0.png)
    



```python
# Make data: I have 3 groups and 7 subgroups
group_names = ['Movies', 'TV Shows']
group_size = [70, 30]
subgroup_names = ['2008', '2009', '2008', '2009']
subgroup_size = [45, 25, 25, 5]

# Create colors
a, b = [plt.cm.Blues, plt.cm.Reds]

# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.6), b(0.6)] )
plt.setp( mypie, width=0.3, edgecolor='white')

# Second Ring (Inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3, labels=subgroup_names, 
                labeldistance=0.7, 
                colors=[a(0.5), a(0.2), b(0.1), b(0.1)]
            )
plt.setp( mypie2, width=0.4, edgecolor='white')
plt.margins(0,0)

# show it
plt.show()
```


    
![png](/mlnotes/images/donut-plot-with-subgroups_4_0.png)
    



```python

```


```python

```


---
**Score: 5**