---
title: Grid-Search-Sample
date: 2025-01-04
author: Your Name
cell_count: 9
score: 5
---

---
title: "Grid Search Sample"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from __future__ import print_function

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
```


```python
# print(__doc__)

# Loading the Digits dataset
digits = datasets.load_digits()
```


```python
# To apply an classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target
```


```python
# Split the dataset in two equal parts
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=0)
```


```python
# Set the parameters by cross-validation
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                 'C': [1, 10, 100, 1000]},
                {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
```


```python
scores = ['precision', 'recall']
```


```python
for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(SVC(), tuned_parameters, cv=5,
                    scoring='%s_macro' % score)
    clf.fit(X_train, y_train)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
            % (mean, std * 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()

    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))
    print()
```

    # Tuning hyper-parameters for precision
    
    Best parameters set found on development set:
    
    {'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}
    
    Grid scores on development set:
    
    0.986 (+/-0.016) for {'C': 1, 'gamma': 0.001, 'kernel': 'rbf'}
    0.959 (+/-0.029) for {'C': 1, 'gamma': 0.0001, 'kernel': 'rbf'}
    0.988 (+/-0.017) for {'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}
    0.982 (+/-0.026) for {'C': 10, 'gamma': 0.0001, 'kernel': 'rbf'}
    0.988 (+/-0.017) for {'C': 100, 'gamma': 0.001, 'kernel': 'rbf'}
    0.982 (+/-0.025) for {'C': 100, 'gamma': 0.0001, 'kernel': 'rbf'}
    0.988 (+/-0.017) for {'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'}
    0.982 (+/-0.025) for {'C': 1000, 'gamma': 0.0001, 'kernel': 'rbf'}
    0.975 (+/-0.014) for {'C': 1, 'kernel': 'linear'}
    0.975 (+/-0.014) for {'C': 10, 'kernel': 'linear'}
    0.975 (+/-0.014) for {'C': 100, 'kernel': 'linear'}
    0.975 (+/-0.014) for {'C': 1000, 'kernel': 'linear'}
    
    Detailed classification report:
    
    The model is trained on the full development set.
    The scores are computed on the full evaluation set.
    
                  precision    recall  f1-score   support
    
               0       1.00      1.00      1.00        89
               1       0.97      1.00      0.98        90
               2       0.99      0.98      0.98        92
               3       1.00      0.99      0.99        93
               4       1.00      1.00      1.00        76
               5       0.99      0.98      0.99       108
               6       0.99      1.00      0.99        89
               7       0.99      1.00      0.99        78
               8       1.00      0.98      0.99        92
               9       0.99      0.99      0.99        92
    
       micro avg       0.99      0.99      0.99       899
       macro avg       0.99      0.99      0.99       899
    weighted avg       0.99      0.99      0.99       899
    
    
    # Tuning hyper-parameters for recall
    
    Best parameters set found on development set:
    
    {'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}
    
    Grid scores on development set:
    
    0.986 (+/-0.019) for {'C': 1, 'gamma': 0.001, 'kernel': 'rbf'}
    0.957 (+/-0.029) for {'C': 1, 'gamma': 0.0001, 'kernel': 'rbf'}
    0.987 (+/-0.019) for {'C': 10, 'gamma': 0.001, 'kernel': 'rbf'}
    0.981 (+/-0.028) for {'C': 10, 'gamma': 0.0001, 'kernel': 'rbf'}
    0.987 (+/-0.019) for {'C': 100, 'gamma': 0.001, 'kernel': 'rbf'}
    0.981 (+/-0.026) for {'C': 100, 'gamma': 0.0001, 'kernel': 'rbf'}
    0.987 (+/-0.019) for {'C': 1000, 'gamma': 0.001, 'kernel': 'rbf'}
    0.981 (+/-0.026) for {'C': 1000, 'gamma': 0.0001, 'kernel': 'rbf'}
    0.972 (+/-0.012) for {'C': 1, 'kernel': 'linear'}
    0.972 (+/-0.012) for {'C': 10, 'kernel': 'linear'}
    0.972 (+/-0.012) for {'C': 100, 'kernel': 'linear'}
    0.972 (+/-0.012) for {'C': 1000, 'kernel': 'linear'}
    
    Detailed classification report:
    
    The model is trained on the full development set.
    The scores are computed on the full evaluation set.
    
                  precision    recall  f1-score   support
    
               0       1.00      1.00      1.00        89
               1       0.97      1.00      0.98        90
               2       0.99      0.98      0.98        92
               3       1.00      0.99      0.99        93
               4       1.00      1.00      1.00        76
               5       0.99      0.98      0.99       108
               6       0.99      1.00      0.99        89
               7       0.99      1.00      0.99        78
               8       1.00      0.98      0.99        92
               9       0.99      0.99      0.99        92
    
       micro avg       0.99      0.99      0.99       899
       macro avg       0.99      0.99      0.99       899
    weighted avg       0.99      0.99      0.99       899
    
    



```python

```


---
**Score: 5**