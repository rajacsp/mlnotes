---
title: Split-And-Get-First
date: 2025-01-03
author: Your Name
cell_count: 7
score: 5
---

```python

```


```python
UNDERSCORE = "_"
```


```python
feature_value_map_for_score = {
  "system_businessname_overlapLevenshtein": 0.5,
  "system_address_overlapLevenshtein": 1.0,
  "system_streetname_overlapLevenshtein": 1.0,
  "system_city_overlapLevenshtein": 1.0,
  "system_zipcode_overlapLevenshtein": 1.0,
  "system_businessname_sorensen": 0.56,
  "system_address_sorensen": 1.0,
  "system_streetname_sorensen": 1.0,
  "system_city_sorensen": 1.0,
  "system_region_sorensen": 1.0,
  "system_houseno_exactMatch": 1.0,
  "system_zipcode_ratcliff": 1.0,
  "system_suiteno_exactMatch": 1.0
}
```


```python
individual_algo_feature_score_map = {
  "system_businessname": {
    "system_businessname_overlapLevenshtein": 0.5,
    "system_businessname_sorensen": 0.56
  },
  "system_address": {
    "system_address_overlapLevenshtein": 1.0,
    "system_address_sorensen": 1.0
  },
  "system_streetname": {
    "system_streetname_overlapLevenshtein": 1.0,
    "system_streetname_sorensen": 1.0
  },
  "system_city": {
    "system_city_overlapLevenshtein": 1.0,
    "system_city_sorensen": 1.0
  },
  "system_zipcode": {
    "system_zipcode_overlapLevenshtein": 1.0,
    "system_zipcode_ratcliff": 1.0
  },
  "system_region": {
    "system_region_sorensen": 1.0
  },
  "system_houseno": {
    "system_houseno_exactMatch": 1.0
  }
}
```


```python
for key, value in feature_value_map_for_score.items():
    feature_prefix = UNDERSCORE.join(key.split(UNDERSCORE)[:-1])
    # print(feature_prefix)

    if feature_prefix in individual_algo_feature_score_map.keys():
        print(f'{feature_prefix} avaible, no impute needed')
    else:
        print(f'{feature_prefix} not avaible, impute needed')
```

    system_businessname avaible, no impute needed
    system_address avaible, no impute needed
    system_streetname avaible, no impute needed
    system_city avaible, no impute needed
    system_zipcode avaible, no impute needed
    system_businessname avaible, no impute needed
    system_address avaible, no impute needed
    system_streetname avaible, no impute needed
    system_city avaible, no impute needed
    system_region avaible, no impute needed
    system_houseno avaible, no impute needed
    system_zipcode avaible, no impute needed
    system_suiteno not avaible, impute needed



```python

```


```python

```


---
**Score: 5**