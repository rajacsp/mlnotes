---
title: Get-Value-And-Check-1
date: 2025-05-17
author: Your Name
cell_count: 16
score: 15
---

```python

```


```python
DATA                              = "data"
JSON_DATA                         = "jsonData"
PENALIZATION_IMPUTATION_WEIGHTAGE = "penalizationImputationWeightage"
```


```python
mltrainconfig_json = {
    "data" : {
        "jsonData" : {
            "penalizationImputationWeightage" : {
                "one" : "two"
            }
        }
    }
}
```


```python
penalization_imputation_weightage = mltrainconfig_json.get(DATA, {})\
        .get(JSON_DATA, {})\
        .get(PENALIZATION_IMPUTATION_WEIGHTAGE, {})
```


```python
penalization_imputation_weightage = penalization_imputation_weightage if penalization_imputation_weightage else imputing_factor_value
```


```python
penalization_imputation_weightage
```




    {'one': 'two'}




```python

```


```python

```


```python

```


```python
mltrainconfig_json = {
    "data" : {
        "jsonData" : {
            "penalizationImputationWeightage2" : {
                "one" : "two"
            }
        }
    }
}
```


```python
imputing_factor_value = {
    "eleven" : "twelve"
}
```


```python
penalization_imputation_weightage = mltrainconfig_json.get(DATA, {})\
        .get(JSON_DATA, {})\
        .get(PENALIZATION_IMPUTATION_WEIGHTAGE, {})
```


```python
penalization_imputation_weightage
```




    {}




```python
penalization_imputation_weightage = penalization_imputation_weightage if penalization_imputation_weightage else imputing_factor_value
```


```python
penalization_imputation_weightage
```




    {'eleven': 'twelve'}




```python

```


---
**Score: 15**