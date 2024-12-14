---
title: Space-Removal-Df
date: 2024-12-14
author: Your Name
cell_count: 13
score: 10
---

```python

```


```python
import pandas as pd
```


```python
FILEPATH = "../countries-of-the-world.csv"
```


```python
df = pd.read_csv(FILEPATH)
```


```python
df.head(2)
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
      <th>Country</th>
      <th>Region</th>
      <th>Population</th>
      <th>Area (sq. mi.)</th>
      <th>Pop. Density (per sq. mi.)</th>
      <th>Coastline (coast/area ratio)</th>
      <th>Net migration</th>
      <th>Infant mortality (per 1000 births)</th>
      <th>GDP ($ per capita)</th>
      <th>Literacy (%)</th>
      <th>Phones (per 1000)</th>
      <th>Arable (%)</th>
      <th>Crops (%)</th>
      <th>Other (%)</th>
      <th>Climate</th>
      <th>Birthrate</th>
      <th>Deathrate</th>
      <th>Agriculture</th>
      <th>Industry</th>
      <th>Service</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>ASIA (EX. NEAR EAST)</td>
      <td>31056997</td>
      <td>647500</td>
      <td>48,0</td>
      <td>0,00</td>
      <td>23,06</td>
      <td>163,07</td>
      <td>700.0</td>
      <td>36,0</td>
      <td>3,2</td>
      <td>12,13</td>
      <td>0,22</td>
      <td>87,65</td>
      <td>1</td>
      <td>46,6</td>
      <td>20,34</td>
      <td>0,38</td>
      <td>0,24</td>
      <td>0,38</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>EASTERN EUROPE</td>
      <td>3581655</td>
      <td>28748</td>
      <td>124,6</td>
      <td>1,26</td>
      <td>-4,93</td>
      <td>21,52</td>
      <td>4500.0</td>
      <td>86,5</td>
      <td>71,2</td>
      <td>21,09</td>
      <td>4,42</td>
      <td>74,49</td>
      <td>3</td>
      <td>15,11</td>
      <td>5,22</td>
      <td>0,232</td>
      <td>0,188</td>
      <td>0,579</td>
    </tr>
  </tbody>
</table>
</div>




```python
for col in df.columns:
    print(col)
```

    Country
    Region
    Population
    Area (sq. mi.)
    Pop. Density (per sq. mi.)
    Coastline (coast/area ratio)
    Net migration
    Infant mortality (per 1000 births)
    GDP ($ per capita)
    Literacy (%)
    Phones (per 1000)
    Arable (%)
    Crops (%)
    Other (%)
    Climate
    Birthrate
    Deathrate
    Agriculture
    Industry
    Service



```python
# print all cols

new_cols = {}
for old_col in list(df.columns):
    # print(col)

    col = old_col
    col = col.lower()

    col = col.replace(".", "")
    col = col.replace(" ", "_")
    col = col.replace("(", "")
    col = col.replace(")", "")
    col = col.replace("%", "")
    col = col.replace("/", "")
    col = col.replace("$", "")
    
    # if " " in col or "(" in col:
    # print(col)

    new_cols[old_col] = col
```


```python
new_cols
```




    {'Country': 'country',
     'Region': 'region',
     'Population': 'population',
     'Area (sq. mi.)': 'area_sq_mi',
     'Pop. Density (per sq. mi.)': 'pop_density_per_sq_mi',
     'Coastline (coast/area ratio)': 'coastline_coastarea_ratio',
     'Net migration': 'net_migration',
     'Infant mortality (per 1000 births)': 'infant_mortality_per_1000_births',
     'GDP ($ per capita)': 'gdp__per_capita',
     'Literacy (%)': 'literacy_',
     'Phones (per 1000)': 'phones_per_1000',
     'Arable (%)': 'arable_',
     'Crops (%)': 'crops_',
     'Other (%)': 'other_',
     'Climate': 'climate',
     'Birthrate': 'birthrate',
     'Deathrate': 'deathrate',
     'Agriculture': 'agriculture',
     'Industry': 'industry',
     'Service': 'service'}




```python
df.rename(
    columns = new_cols, 
    inplace = True
)
```


```python
df.head(2)
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
      <th>country</th>
      <th>region</th>
      <th>population</th>
      <th>area_sq_mi</th>
      <th>pop_density_per_sq_mi</th>
      <th>coastline_coastarea_ratio</th>
      <th>net_migration</th>
      <th>infant_mortality_per_1000_births</th>
      <th>gdp__per_capita</th>
      <th>literacy_</th>
      <th>phones_per_1000</th>
      <th>arable_</th>
      <th>crops_</th>
      <th>other_</th>
      <th>climate</th>
      <th>birthrate</th>
      <th>deathrate</th>
      <th>agriculture</th>
      <th>industry</th>
      <th>service</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>ASIA (EX. NEAR EAST)</td>
      <td>31056997</td>
      <td>647500</td>
      <td>48,0</td>
      <td>0,00</td>
      <td>23,06</td>
      <td>163,07</td>
      <td>700.0</td>
      <td>36,0</td>
      <td>3,2</td>
      <td>12,13</td>
      <td>0,22</td>
      <td>87,65</td>
      <td>1</td>
      <td>46,6</td>
      <td>20,34</td>
      <td>0,38</td>
      <td>0,24</td>
      <td>0,38</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>EASTERN EUROPE</td>
      <td>3581655</td>
      <td>28748</td>
      <td>124,6</td>
      <td>1,26</td>
      <td>-4,93</td>
      <td>21,52</td>
      <td>4500.0</td>
      <td>86,5</td>
      <td>71,2</td>
      <td>21,09</td>
      <td>4,42</td>
      <td>74,49</td>
      <td>3</td>
      <td>15,11</td>
      <td>5,22</td>
      <td>0,232</td>
      <td>0,188</td>
      <td>0,579</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_csv('../countries-of-the-world-cleaned.csv')
```


```python

```


```python

```


---
**Score: 10**