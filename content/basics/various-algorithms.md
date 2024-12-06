---
title: Various-Algorithms
date: 2024-12-06
author: Your Name
cell_count: 12
score: 10
---

---
title: "Various Algorithms"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---
Source:

https://www.kaggle.com/drfrank/estonia-disaster-visualization-machine-learning


```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

X = np.array(
    [
        [1, 1], [1, 2], [2, 2], [2, 3]
        ,[3, 5], [6, 4], [56, 23], [34, 56], [4, 5]
    ]
)

# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3

# X_train, y_train = X, y

X_train, X_test, y_train, y_test = train_test_split(X,y,
                                               test_size=0.2,
                                               random_state=42)
```


```python
reg = LinearRegression().fit(X, y)
reg.score(X, y)

reg.coef_

reg.intercept_

reg.predict(np.array([[3, 5]]))
```




    array([16.])




```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn_model = knn.fit(X_train, y_train)
knn_model
```




    KNeighborsClassifier()




```python
from sklearn.linear_model import LogisticRegression

loj = LogisticRegression(solver = "liblinear")
loj_model = loj.fit(X,y)
# loj_model
```


```python
from sklearn.svm import SVC
svm_model = SVC(kernel = "linear").fit(X_train, y_train)
```


```python
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb_model = nb.fit(X_train, y_train)
nb_model
```




    GaussianNB()




```python
from sklearn.neural_network import MLPClassifier
mlpc = MLPClassifier().fit(X_train, y_train)
```

    /Users/rajacsp/opt/anaconda3/envs/py38_jupyter/lib/python3.8/site-packages/sklearn/neural_network/_multilayer_perceptron.py:582: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.
      warnings.warn(



```python
from sklearn.tree import DecisionTreeClassifier

cart = DecisionTreeClassifier()
cart_model = cart.fit(X_train, y_train)
```


```python
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier().fit(X_train, y_train)
```


```python
models = [
    knn_model,
    loj_model,
    svm_model,
    nb_model,
    mlpc,
    cart_model,
    rf_model
]

for model in models:
    names = model.__class__.__name__
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("-"*28)
    print(names + ":" )
    print("Accuracy: {:.4%}".format(accuracy))
```

    ----------------------------
    KNeighborsClassifier:
    Accuracy: 0.0000%
    ----------------------------
    LogisticRegression:
    Accuracy: 50.0000%
    ----------------------------
    SVC:
    Accuracy: 0.0000%
    ----------------------------
    GaussianNB:
    Accuracy: 0.0000%
    ----------------------------
    MLPClassifier:
    Accuracy: 0.0000%
    ----------------------------
    DecisionTreeClassifier:
    Accuracy: 0.0000%
    ----------------------------
    RandomForestClassifier:
    Accuracy: 0.0000%



---
**Score: 10**