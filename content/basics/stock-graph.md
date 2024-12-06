---
title: Stock-Graph
date: 2024-12-06
author: Your Name
cell_count: 5
score: 5
---

---
title: "Stock Graph"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import matplotlib.pyplot as plt
import fix_yahoo_finance as yf
```


```python
def show_stock(code):
    data = yf.download(code,'2010-01-01','2018-09-01')
    data.Close.plot()
    plt.show()
```


```python
show_stock('INFY')
```

    [*********************100%***********************]  1 of 1 downloaded



    
![png](/mlnotes/images/stock-graph_3_1.png)
    



```python
show_stock('AMZN')
```

    [*********************100%***********************]  1 of 1 downloaded



    
![png](/mlnotes/images/stock-graph_4_1.png)
    



---
**Score: 5**