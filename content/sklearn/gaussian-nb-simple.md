---
title: Gaussian-Nb-Simple
date: 2024-12-14
author: Your Name
cell_count: 6
score: 5
---

---
title: "Gaussian NB Simple"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
```


```python
iris = datasets.load_iris()
```


```python
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
```


```python
print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))
```

    Number of mislabeled points out of a total 150 points : 6



```python

```


---
**Score: 5**