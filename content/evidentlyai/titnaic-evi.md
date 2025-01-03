---
title: Titnaic-Evi
date: 2025-01-03
author: Your Name
cell_count: 33
score: 30
---

```python

```


```python
# https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
```


```python
import pandas as pd
```


```python
!ls ../titanic.csv
```

    ../titanic.csv



```python
# Load the dataset
data = pd.read_csv('../titanic.csv')
```


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 12 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   PassengerId  891 non-null    int64  
     1   Survived     891 non-null    int64  
     2   Pclass       891 non-null    int64  
     3   Name         891 non-null    object 
     4   Sex          891 non-null    object 
     5   Age          714 non-null    float64
     6   SibSp        891 non-null    int64  
     7   Parch        891 non-null    int64  
     8   Ticket       891 non-null    object 
     9   Fare         891 non-null    float64
     10  Cabin        204 non-null    object 
     11  Embarked     889 non-null    object 
    dtypes: float64(2), int64(5), object(5)
    memory usage: 83.7+ KB



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
      <th>PassengerId</th>
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>0</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>Unknown</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>1</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>1</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>Unknown</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>1</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>0</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>Unknown</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
# data['Age'].fillna(data['Age'].median(), inplace=True)
data['Age'] = data['Age'].fillna(data['Age'].median())
```


```python
# Encode categorical variables if necessary
# Example: Convert 'Sex' to numerical values
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
```


```python

```


```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
```


```python
# Initialize the report with the Data Drift preset
report = Report(metrics=[DataDriftPreset()])
```


```python
data.isnull().sum()
```




    PassengerId      0
    Survived         0
    Pclass           0
    Name             0
    Sex              0
    Age              0
    SibSp            0
    Parch            0
    Ticket           0
    Fare             0
    Cabin          687
    Embarked         2
    dtype: int64




```python
data.describe()
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
      <td>891.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>446.000000</td>
      <td>0.383838</td>
      <td>2.308642</td>
      <td>0.352413</td>
      <td>29.361582</td>
      <td>0.523008</td>
      <td>0.381594</td>
      <td>32.204208</td>
    </tr>
    <tr>
      <th>std</th>
      <td>257.353842</td>
      <td>0.486592</td>
      <td>0.836071</td>
      <td>0.477990</td>
      <td>13.019697</td>
      <td>1.102743</td>
      <td>0.806057</td>
      <td>49.693429</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.420000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>223.500000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>22.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.910400</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>446.000000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>28.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>14.454200</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>668.500000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>35.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>891.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>80.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>512.329200</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['Cabin'] = data['Cabin'].fillna('Unknown')
```


```python
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
```


```python
data.isnull().sum()
```




    PassengerId    0
    Survived       0
    Pclass         0
    Name           0
    Sex            0
    Age            0
    SibSp          0
    Parch          0
    Ticket         0
    Fare           0
    Cabin          0
    Embarked       0
    dtype: int64




```python
data.nunique()
```




    PassengerId    891
    Survived         2
    Pclass           3
    Name           891
    Sex              2
    Age             88
    SibSp            7
    Parch            7
    Ticket         681
    Fare           248
    Cabin          148
    Embarked         3
    dtype: int64




```python
# Split the data into reference and current datasets
reference_data = data.sample(frac=0.7, random_state=42)  # 70% as reference
current_data = data.drop(reference_data.index)  # Remaining 30% as current
```


```python
reference_data.describe(include='all')
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
      <th>PassengerId</th>
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
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>624.000000</td>
      <td>624.000000</td>
      <td>624.000000</td>
      <td>624</td>
      <td>624.000000</td>
      <td>624.000000</td>
      <td>624.000000</td>
      <td>624.000000</td>
      <td>624</td>
      <td>624.000000</td>
      <td>624</td>
      <td>624</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>624</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>509</td>
      <td>NaN</td>
      <td>113</td>
      <td>3</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Greenberg, Mr. Samuel</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>382652</td>
      <td>NaN</td>
      <td>Unknown</td>
      <td>S</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>488</td>
      <td>440</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>438.080128</td>
      <td>0.391026</td>
      <td>2.314103</td>
      <td>NaN</td>
      <td>0.360577</td>
      <td>29.239984</td>
      <td>0.504808</td>
      <td>0.400641</td>
      <td>NaN</td>
      <td>31.846708</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>258.247396</td>
      <td>0.488372</td>
      <td>0.831209</td>
      <td>NaN</td>
      <td>0.480553</td>
      <td>13.146780</td>
      <td>1.018280</td>
      <td>0.815027</td>
      <td>NaN</td>
      <td>49.422675</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.750000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>213.750000</td>
      <td>0.000000</td>
      <td>2.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>22.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>7.925000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>434.500000</td>
      <td>0.000000</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>28.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>14.500000</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>658.250000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>35.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>30.178100</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>891.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>80.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>NaN</td>
      <td>512.329200</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
current_data.isnull().sum()
```




    PassengerId    0
    Survived       0
    Pclass         0
    Name           0
    Sex            0
    Age            0
    SibSp          0
    Parch          0
    Ticket         0
    Fare           0
    Cabin          0
    Embarked       0
    dtype: int64




```python

```


```python
reference_data.isnull().sum()
```




    PassengerId    0
    Survived       0
    Pclass         0
    Name           0
    Sex            0
    Age            0
    SibSp          0
    Parch          0
    Ticket         0
    Fare           0
    Cabin          0
    Embarked       0
    dtype: int64




```python
# Run the report
report.run(reference_data=reference_data, current_data=current_data)
```

    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp
    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp
    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp
    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp
    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp
    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp



```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
```


```python
# Initialize the report with the Data Drift preset
report = Report(metrics=[DataDriftPreset()])
```


```python
# Run the report
report.run(reference_data=reference_data, current_data=current_data)
```

    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp
    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp
    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp
    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp
    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp
    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/scipy/stats/_stats_py.py:8064: RuntimeWarning: divide by zero encountered in divide
      terms = (f_obs_float - f_exp)**2 / f_exp



```python
# Save the report to an HTML file
report.save_html('titanic_data_drift_report.html')
```


```python

```


```python
reference_data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 624 entries, 709 to 714
    Data columns (total 12 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   PassengerId  624 non-null    int64  
     1   Survived     624 non-null    int64  
     2   Pclass       624 non-null    int64  
     3   Name         624 non-null    object 
     4   Sex          624 non-null    int64  
     5   Age          624 non-null    float64
     6   SibSp        624 non-null    int64  
     7   Parch        624 non-null    int64  
     8   Ticket       624 non-null    object 
     9   Fare         624 non-null    float64
     10  Cabin        624 non-null    object 
     11  Embarked     624 non-null    object 
    dtypes: float64(2), int64(6), object(4)
    memory usage: 63.4+ KB



```python
current_data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 267 entries, 1 to 887
    Data columns (total 12 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   PassengerId  267 non-null    int64  
     1   Survived     267 non-null    int64  
     2   Pclass       267 non-null    int64  
     3   Name         267 non-null    object 
     4   Sex          267 non-null    int64  
     5   Age          267 non-null    float64
     6   SibSp        267 non-null    int64  
     7   Parch        267 non-null    int64  
     8   Ticket       267 non-null    object 
     9   Fare         267 non-null    float64
     10  Cabin        267 non-null    object 
     11  Embarked     267 non-null    object 
    dtypes: float64(2), int64(6), object(4)
    memory usage: 27.1+ KB



```python

```


```python

```


---
**Score: 30**