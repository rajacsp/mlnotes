---
title: Various-Algorithms-Titanic
date: 2024-11-24
author: Your Name
cell_count: 32
score: 30
---

---
title: "Various Algorithms Titanic"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---
Source:

https://www.kaggle.com/drfrank/estonia-disaster-visualization-machine-learning

https://stackoverflow.com/questions/55240330/how-to-read-csv-file-from-github-using-pandas

https://gist.github.com/michhar/2dfd2de0d4f8727f873422c5d959fff5

https://www.kaggle.com/rajacsp/titanic-basic-analysis


```python
import pandas as pd

url = 'https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/fa71405126017e6a37bea592440b4bee94bf7b9e/titanic.csv'
df = pd.read_csv(url, index_col=0)

data = df

data.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
    <tr>
      <th>PassengerId</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.drop(['SibSp', 'Pclass', 'Name', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'], axis = 1, inplace = True)
```


```python
data.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
      <th>Sex</th>
      <th>Age</th>
    </tr>
    <tr>
      <th>PassengerId</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>male</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>female</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>male</td>
      <td>35.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.isnull().sum()
```




    Survived      0
    Sex           0
    Age         177
    dtype: int64




```python
data['Age'] = data['Age'].fillna(data['Age'].mean())
```


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
      <th>Sex</th>
      <th>Age</th>
    </tr>
    <tr>
      <th>PassengerId</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>male</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>female</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>male</td>
      <td>35.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.isnull().sum()
```




    Survived    0
    Sex         0
    Age         0
    dtype: int64




```python
data = pd.get_dummies(data, columns = ['Sex'])
```


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Survived</th>
      <th>Age</th>
      <th>Sex_female</th>
      <th>Sex_male</th>
    </tr>
    <tr>
      <th>PassengerId</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>22.0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>26.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>35.0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
y = data['Survived']
```


```python
y.head()
```




    PassengerId
    1    0
    2    1
    3    1
    4    1
    5    0
    Name: Survived, dtype: int64




```python
X = data.drop('Survived', axis = 1)
X.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Sex_female</th>
      <th>Sex_male</th>
    </tr>
    <tr>
      <th>PassengerId</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>22.0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>26.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>35.0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                               test_size = 0.3,
                                               random_state = 21)
```


```python
reg = LinearRegression().fit(X, y)
reg.score(X, y)

reg.coef_

reg.intercept_

# reg.predict(np.array([[3, 5]]))
```




    0.4921256890039903



### 1. KNN


```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn_model = knn.fit(X_train, y_train)
knn_model
```




    KNeighborsClassifier()



### 2. Logistic Regression


```python
from sklearn.linear_model import LogisticRegression

loj = LogisticRegression(solver = "liblinear")
loj_model = loj.fit(X,y)
# loj_model
```

### 3. Support Vector Machine


```python
from sklearn.svm import SVC
svm_model = SVC(kernel = "linear").fit(X_train, y_train)
```

### 4. Gaussian Naive Bayes


```python
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb_model = nb.fit(X_train, y_train)
nb_model
```




    GaussianNB()



### 5. Artificial Neural Networks


```python
from sklearn.neural_network import MLPClassifier
mlpc = MLPClassifier().fit(X_train, y_train)
```

### 6. CART


```python
from sklearn.tree import DecisionTreeClassifier

cart = DecisionTreeClassifier()
cart_model = cart.fit(X_train, y_train)
```

### 7. Random Forest Classifier


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
    Accuracy: 75.3731%
    ----------------------------
    LogisticRegression:
    Accuracy: 78.7313%
    ----------------------------
    SVC:
    Accuracy: 78.7313%
    ----------------------------
    GaussianNB:
    Accuracy: 78.7313%
    ----------------------------
    MLPClassifier:
    Accuracy: 79.1045%
    ----------------------------
    DecisionTreeClassifier:
    Accuracy: 77.6119%
    ----------------------------
    RandomForestClassifier:
    Accuracy: 77.2388%



```python

```


---
**Score: 30**