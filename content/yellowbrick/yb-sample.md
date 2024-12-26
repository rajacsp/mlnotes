---
title: Yb-Sample
date: 2024-12-26
author: Your Name
cell_count: 10
score: 10
---

---
title: "YB Sample"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import pandas as pd
```


```python
def load_yb_data(name = 'energy'):
    folder_path = name+'/'+name
    return pd.read_csv('/Users/rajacsp/datasets/yb_data/'+(folder_path)+'.csv')
```


```python
from yellowbrick.features import ParallelCoordinates
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
```


```python
# Load Breast Cancer Dataset
breast_cancer = load_breast_cancer()
```


```python
type(breast_cancer)
```




    sklearn.utils.Bunch




```python
X = breast_cancer.data
y = breast_cancer.target
```


```python
# Split the Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=44)
```


```python
visualizer = ParallelCoordinates()
visualizer.fit_transform(X_train, y_train)
#visualizer.score(X_test, y_test)
visualizer.poof()
```


    
![png](/mlnotes/images/yb-sample_8_0.png)
    


Note:

proof method finalizes the drawing (adding titles, axes labels, etc) and then renders the image of your behalf.


---
**Score: 10**