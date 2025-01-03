---
title: Pca-Simple
date: 2025-01-03
author: Your Name
cell_count: 12
score: 10
---

---
title: "PCA Simple"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
```


```python
iris = load_iris()
```


```python
X, y = iris.data, iris.target
```


```python
# This dataset is way too high-dimensional. Better do PCA:
pca = PCA(n_components=2)
```


```python
# Maybe some original features where good, too?
selection = SelectKBest(k=1)
```


```python
# Build estimator from PCA and Univariate selection:

combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```


```python
# Use combined features to transform dataset:
X_features = combined_features.fit(X, y).transform(X)
```


```python
svm = SVC(kernel="linear")
```


```python
# Do grid search over k, n_components and C:

pipeline = Pipeline([("features", combined_features), ("svm", svm)])

param_grid = dict(features__pca__n_components=[1, 2, 3],
                  features__univ_select__k=[1, 2],
                  svm__C=[0.1, 1, 10])
```


```python
grid_search = GridSearchCV(pipeline, param_grid=param_grid, verbose=10)
grid_search.fit(X, y)
#print(grid_search.best_estimator_)
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/sklearn/model_selection/_split.py:2053: FutureWarning: You should specify a value for 'cv' instead of relying on the default value. The default value will change from 3 to 5 in version 0.22.
      warnings.warn(CV_WARNING, FutureWarning)
    [Parallel(n_jobs=1)]: Using backend SequentialBackend with 1 concurrent workers.
    [Parallel(n_jobs=1)]: Done   1 out of   1 | elapsed:    0.0s remaining:    0.0s
    [Parallel(n_jobs=1)]: Done   2 out of   2 | elapsed:    0.0s remaining:    0.0s
    [Parallel(n_jobs=1)]: Done   3 out of   3 | elapsed:    0.0s remaining:    0.0s
    [Parallel(n_jobs=1)]: Done   4 out of   4 | elapsed:    0.0s remaining:    0.0s
    [Parallel(n_jobs=1)]: Done   5 out of   5 | elapsed:    0.0s remaining:    0.0s
    [Parallel(n_jobs=1)]: Done   6 out of   6 | elapsed:    0.0s remaining:    0.0s
    [Parallel(n_jobs=1)]: Done   7 out of   7 | elapsed:    0.0s remaining:    0.0s
    [Parallel(n_jobs=1)]: Done   8 out of   8 | elapsed:    0.0s remaining:    0.0s
    [Parallel(n_jobs=1)]: Done   9 out of   9 | elapsed:    0.0s remaining:    0.0s


    Fitting 3 folds for each of 18 candidates, totalling 54 fits
    [CV] features__pca__n_components=1, features__univ_select__k=1, svm__C=0.1 
    [CV]  features__pca__n_components=1, features__univ_select__k=1, svm__C=0.1, score=0.9607843137254902, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=1, svm__C=0.1 
    [CV]  features__pca__n_components=1, features__univ_select__k=1, svm__C=0.1, score=0.9019607843137255, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=1, svm__C=0.1 
    [CV]  features__pca__n_components=1, features__univ_select__k=1, svm__C=0.1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=1, svm__C=1 
    [CV]  features__pca__n_components=1, features__univ_select__k=1, svm__C=1, score=0.9411764705882353, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=1, svm__C=1 
    [CV]  features__pca__n_components=1, features__univ_select__k=1, svm__C=1, score=0.9215686274509803, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=1, svm__C=1 
    [CV]  features__pca__n_components=1, features__univ_select__k=1, svm__C=1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=1, svm__C=10 
    [CV]  features__pca__n_components=1, features__univ_select__k=1, svm__C=10, score=0.9607843137254902, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=1, svm__C=10 
    [CV]  features__pca__n_components=1, features__univ_select__k=1, svm__C=10, score=0.8823529411764706, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=1, svm__C=10 
    [CV]  features__pca__n_components=1, features__univ_select__k=1, svm__C=10, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=2, svm__C=0.1 
    [CV]  features__pca__n_components=1, features__univ_select__k=2, svm__C=0.1, score=0.9607843137254902, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=2, svm__C=0.1 
    [CV]  features__pca__n_components=1, features__univ_select__k=2, svm__C=0.1, score=0.9215686274509803, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=2, svm__C=0.1 
    [CV]  features__pca__n_components=1, features__univ_select__k=2, svm__C=0.1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=2, svm__C=1 
    [CV]  features__pca__n_components=1, features__univ_select__k=2, svm__C=1, score=0.9607843137254902, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=2, svm__C=1 
    [CV]  features__pca__n_components=1, features__univ_select__k=2, svm__C=1, score=0.9215686274509803, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=2, svm__C=1 
    [CV]  features__pca__n_components=1, features__univ_select__k=2, svm__C=1, score=1.0, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=2, svm__C=10 
    [CV]  features__pca__n_components=1, features__univ_select__k=2, svm__C=10, score=0.9803921568627451, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=2, svm__C=10 
    [CV]  features__pca__n_components=1, features__univ_select__k=2, svm__C=10, score=0.9019607843137255, total=   0.0s
    [CV] features__pca__n_components=1, features__univ_select__k=2, svm__C=10 
    [CV]  features__pca__n_components=1, features__univ_select__k=2, svm__C=10, score=1.0, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=1, svm__C=0.1 
    [CV]  features__pca__n_components=2, features__univ_select__k=1, svm__C=0.1, score=0.9607843137254902, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=1, svm__C=0.1 
    [CV]  features__pca__n_components=2, features__univ_select__k=1, svm__C=0.1, score=0.9019607843137255, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=1, svm__C=0.1 
    [CV]  features__pca__n_components=2, features__univ_select__k=1, svm__C=0.1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=1, svm__C=1 
    [CV]  features__pca__n_components=2, features__univ_select__k=1, svm__C=1, score=0.9803921568627451, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=1, svm__C=1 
    [CV]  features__pca__n_components=2, features__univ_select__k=1, svm__C=1, score=0.9411764705882353, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=1, svm__C=1 
    [CV]  features__pca__n_components=2, features__univ_select__k=1, svm__C=1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=1, svm__C=10 
    [CV]  features__pca__n_components=2, features__univ_select__k=1, svm__C=10, score=0.9803921568627451, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=1, svm__C=10 
    [CV]  features__pca__n_components=2, features__univ_select__k=1, svm__C=10, score=0.9411764705882353, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=1, svm__C=10 
    [CV]  features__pca__n_components=2, features__univ_select__k=1, svm__C=10, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=2, svm__C=0.1 
    [CV]  features__pca__n_components=2, features__univ_select__k=2, svm__C=0.1, score=0.9803921568627451, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=2, svm__C=0.1 
    [CV]  features__pca__n_components=2, features__univ_select__k=2, svm__C=0.1, score=0.9411764705882353, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=2, svm__C=0.1 
    [CV]  features__pca__n_components=2, features__univ_select__k=2, svm__C=0.1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=2, svm__C=1 
    [CV]  features__pca__n_components=2, features__univ_select__k=2, svm__C=1, score=1.0, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=2, svm__C=1 
    [CV]  features__pca__n_components=2, features__univ_select__k=2, svm__C=1, score=0.9607843137254902, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=2, svm__C=1 
    [CV]  features__pca__n_components=2, features__univ_select__k=2, svm__C=1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=2, svm__C=10 
    [CV]  features__pca__n_components=2, features__univ_select__k=2, svm__C=10, score=0.9803921568627451, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=2, svm__C=10 
    [CV]  features__pca__n_components=2, features__univ_select__k=2, svm__C=10, score=0.9215686274509803, total=   0.0s
    [CV] features__pca__n_components=2, features__univ_select__k=2, svm__C=10 
    [CV]  features__pca__n_components=2, features__univ_select__k=2, svm__C=10, score=1.0, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=1, svm__C=0.1 
    [CV]  features__pca__n_components=3, features__univ_select__k=1, svm__C=0.1, score=0.9803921568627451, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=1, svm__C=0.1 
    [CV]  features__pca__n_components=3, features__univ_select__k=1, svm__C=0.1, score=0.9411764705882353, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=1, svm__C=0.1 
    [CV]  features__pca__n_components=3, features__univ_select__k=1, svm__C=0.1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=1, svm__C=1 
    [CV]  features__pca__n_components=3, features__univ_select__k=1, svm__C=1, score=1.0, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=1, svm__C=1 
    [CV]  features__pca__n_components=3, features__univ_select__k=1, svm__C=1, score=0.9411764705882353, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=1, svm__C=1 
    [CV]  features__pca__n_components=3, features__univ_select__k=1, svm__C=1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=1, svm__C=10 
    [CV]  features__pca__n_components=3, features__univ_select__k=1, svm__C=10, score=1.0, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=1, svm__C=10 
    [CV]  features__pca__n_components=3, features__univ_select__k=1, svm__C=10, score=0.9215686274509803, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=1, svm__C=10 
    [CV]  features__pca__n_components=3, features__univ_select__k=1, svm__C=10, score=1.0, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=2, svm__C=0.1 
    [CV]  features__pca__n_components=3, features__univ_select__k=2, svm__C=0.1, score=0.9803921568627451, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=2, svm__C=0.1 


    [CV]  features__pca__n_components=3, features__univ_select__k=2, svm__C=0.1, score=0.9411764705882353, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=2, svm__C=0.1 
    [CV]  features__pca__n_components=3, features__univ_select__k=2, svm__C=0.1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=2, svm__C=1 
    [CV]  features__pca__n_components=3, features__univ_select__k=2, svm__C=1, score=1.0, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=2, svm__C=1 
    [CV]  features__pca__n_components=3, features__univ_select__k=2, svm__C=1, score=0.9607843137254902, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=2, svm__C=1 
    [CV]  features__pca__n_components=3, features__univ_select__k=2, svm__C=1, score=0.9791666666666666, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=2, svm__C=10 
    [CV]  features__pca__n_components=3, features__univ_select__k=2, svm__C=10, score=1.0, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=2, svm__C=10 
    [CV]  features__pca__n_components=3, features__univ_select__k=2, svm__C=10, score=0.9215686274509803, total=   0.0s
    [CV] features__pca__n_components=3, features__univ_select__k=2, svm__C=10 
    [CV]  features__pca__n_components=3, features__univ_select__k=2, svm__C=10, score=1.0, total=   0.0s


    [Parallel(n_jobs=1)]: Done  54 out of  54 | elapsed:    0.2s finished
    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/sklearn/model_selection/_search.py:841: DeprecationWarning: The default of the `iid` parameter will change from True to False in version 0.22 and will be removed in 0.24. This will change numeric results when test-set sizes are unequal.
      DeprecationWarning)





    GridSearchCV(cv='warn', error_score='raise-deprecating',
           estimator=Pipeline(memory=None,
         steps=[('features', FeatureUnion(n_jobs=None,
           transformer_list=[('pca', PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
      svd_solver='auto', tol=0.0, whiten=False)), ('univ_select', SelectKBest(k=1, score_func=<function f_classif at 0x11dd4c0d0>))],
           transformer...r', max_iter=-1, probability=False, random_state=None,
      shrinking=True, tol=0.001, verbose=False))]),
           fit_params=None, iid='warn', n_jobs=None,
           param_grid={'features__pca__n_components': [1, 2, 3], 'features__univ_select__k': [1, 2], 'svm__C': [0.1, 1, 10]},
           pre_dispatch='2*n_jobs', refit=True, return_train_score='warn',
           scoring=None, verbose=10)




```python

```


---
**Score: 10**