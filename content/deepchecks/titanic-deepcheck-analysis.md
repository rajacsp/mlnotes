---
title: Titanic-Deepcheck-Analysis
date: 2024-12-04
author: Your Name
cell_count: 15
score: 15
---

```python
!python --version
```

    Python 3.10.5



```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import full_suite
```


```python
# Load the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)
```


```python
# Preprocess the data
# Drop irrelevant columns
titanic = titanic.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
```


```python
# Fill missing values
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic['Embarked'] = titanic['Embarked'].fillna('S')
```


```python
# Encode categorical variables
label_encoder = LabelEncoder()
titanic['Sex'] = label_encoder.fit_transform(titanic['Sex'])
titanic['Embarked'] = label_encoder.fit_transform(titanic['Embarked'])
```


```python
# Split the data
X = titanic.drop(columns=['Survived'])
y = titanic['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```


```python
# Train a Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
```




<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>RandomForestClassifier(random_state=42)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">RandomForestClassifier</label><div class="sk-toggleable__content"><pre>RandomForestClassifier(random_state=42)</pre></div></div></div></div></div>




```python
# Wrap datasets into Deepchecks Dataset objects
columns = X.columns.tolist()
train_df = pd.DataFrame(X_train, columns=columns)
train_df['Survived'] = y_train
```


```python
test_df = pd.DataFrame(X_test, columns=columns)
test_df['Survived'] = y_test
```


```python
dc_train = Dataset(train_df, label='Survived', cat_features=['Sex', 'Embarked'])
dc_test = Dataset(test_df, label='Survived', cat_features=['Sex', 'Embarked'])
```


```python
# Run the full Deepchecks suite
suite = full_suite()
suite_result = suite.run(train_dataset=dc_train, test_dataset=dc_test, model=model)
```



<style>
    progress {
        -webkit-appearance: none;
        border: none;
        border-radius: 3px;
        width: 300px;
        height: 20px;
        vertical-align: middle;
        margin-right: 10px;
        background-color: aliceblue;
    }
    progress::-webkit-progress-bar {
        border-radius: 3px;
        background-color: aliceblue;
    }
    progress::-webkit-progress-value {
        background-color: #9d60fb;
    }
    progress::-moz-progress-bar {
        background-color: #9d60fb;
    }
</style>







    /home/rajaraman/miniconda3/envs/ml3105/lib/python3.10/site-packages/deepchecks/utils/abstracts/weak_segment_abstract.py:57: FutureWarning:
    
    Setting an item of incompatible dtype is deprecated and will raise in a future error of pandas. Value 'Other' has dtype incompatible with int64, please explicitly cast to a compatible dtype first.
    
    /home/rajaraman/miniconda3/envs/ml3105/lib/python3.10/site-packages/deepchecks/utils/abstracts/weak_segment_abstract.py:57: FutureWarning:
    
    Setting an item of incompatible dtype is deprecated and will raise in a future error of pandas. Value 'Other' has dtype incompatible with int64, please explicitly cast to a compatible dtype first.
    
    /home/rajaraman/miniconda3/envs/ml3105/lib/python3.10/site-packages/deepchecks/tabular/checks/train_test_validation/train_test_samples_mix.py:85: FutureWarning:
    
    DataFrame.applymap has been deprecated. Use DataFrame.map instead.
    



```python
# Display and save the results
suite_result.save_as_html('titanic_analysis_report.html')
print("Deepchecks analysis report saved to 'titanic_analysis_report.html'")
```

    Deepchecks analysis report saved to 'titanic_analysis_report.html'



```python
# Display the results in the notebook or terminal
suite_result.show()
```


    Accordion(children=(VBox(children=(HTML(value='\n<h1 id="summary_EKL0D0IU0T3X3W4TN4V3CMXRK">Full Suite</h1>\n<…



```python

```


---
**Score: 15**