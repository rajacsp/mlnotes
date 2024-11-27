---
title: Breakfast-Spending
date: 2024-11-27
author: Your Name
cell_count: 6
score: 5
---

---
title: "Breakfast Spending"
author: "Rj"
date: 2019-05-06
description: "List Test"
type: technical_note
draft: false
---

```python
import matplotlib.pyplot as plt
```


```python
x = [1, 2, 3, 4, 5, 6, 7, 8]
```


```python
# Amount I spent on the breakfast 
y = [9.12, 10.25, 11.25, 7.80, 8.90, 9.80, 10.12, 10.00]
```


```python
x, y
```




    ([1, 2, 3, 4, 5, 6, 7, 8], [9.12, 10.25, 11.25, 7.8, 8.9, 9.8, 10.12, 10.0])




```python
plt.plot(x, y, 'bx')
plt.axis([0, 10, 0, 20])
```




    [0, 10, 0, 20]




    
![png](/mlnotes/images/breakfast-spending_5_1.png)
    



---
**Score: 5**