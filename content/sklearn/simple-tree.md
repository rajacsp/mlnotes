---
title: Simple-Tree
date: 2024-12-13
author: Your Name
cell_count: 5
score: 5
---

---
title: "Simple Tree"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
from sklearn import tree
```


```python
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
```


```python
print(clf.predict([[21., 21.]]))
```

    [1]



```python

```


---
**Score: 5**