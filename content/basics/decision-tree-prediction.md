---
title: Decision-Tree-Prediction
date: 2024-12-14
author: Your Name
cell_count: 7
score: 5
---

---
title: "Decision Tree Prediction"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from sklearn import tree
```


```python
X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
```


```python
clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, y)
```


```python
predicted = clf.predict([[1, 1]])
```


```python
print(predicted)
```

    [0.5]



```python

```


---
**Score: 5**