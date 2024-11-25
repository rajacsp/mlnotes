---
title: Chloropleth Maps
date: 2024-11-25
author: Your Name
cell_count: 21
score: 20
---

---
title: "Chloropleth Maps"
author: "Raja CSP Raman"
date: 2019-05-07
description: "-"
type: technical_note
draft: false
---

```python
import geopandas
```


```python
world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
```


```python
world.head()
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
      <th>pop_est</th>
      <th>continent</th>
      <th>name</th>
      <th>iso_a3</th>
      <th>gdp_md_est</th>
      <th>geometry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>920938</td>
      <td>Oceania</td>
      <td>Fiji</td>
      <td>FJI</td>
      <td>8374.0</td>
      <td>(POLYGON ((180 -16.06713266364245, 180 -16.555...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>53950935</td>
      <td>Africa</td>
      <td>Tanzania</td>
      <td>TZA</td>
      <td>150600.0</td>
      <td>POLYGON ((33.90371119710453 -0.950000000000000...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>603253</td>
      <td>Africa</td>
      <td>W. Sahara</td>
      <td>ESH</td>
      <td>906.5</td>
      <td>POLYGON ((-8.665589565454809 27.65642588959236...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>35623680</td>
      <td>North America</td>
      <td>Canada</td>
      <td>CAN</td>
      <td>1674000.0</td>
      <td>(POLYGON ((-122.84 49.00000000000011, -122.974...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>326625791</td>
      <td>North America</td>
      <td>United States of America</td>
      <td>USA</td>
      <td>18560000.0</td>
      <td>(POLYGON ((-122.84 49.00000000000011, -120 49....</td>
    </tr>
  </tbody>
</table>
</div>




```python
world = world[(world.pop_est > 0) & (world.continent != 'Antarctica')]
```


```python
world['gdp_per_cap'] = world.gdp_md_est / world.pop_est
```


```python
world.plot(column='gdp_per_cap')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x126780ac8>




    
![png](/mlnotes/images/chloropleth_maps_6_1.png)
    



```python
world.continent.unique()
```




    array(['Oceania', 'Africa', 'North America', 'Asia', 'South America',
           'Europe', 'Seven seas (open ocean)'], dtype=object)




```python
# Show only Asia
```


```python
asia = world[world.continent == 'Asia']
```


```python
asia['gdp_per_cap'] = asia.gdp_md_est / asia.pop_est
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.



```python
asia.plot(column='gdp_per_cap')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1268cf668>




    
![png](/mlnotes/images/chloropleth_maps_11_1.png)
    



```python
# Show only Europe
```


```python
eu = world[world.continent == 'Europe']
eu['gdp_per_cap'] = eu.gdp_md_est / eu.pop_est
eu.plot(column='gdp_per_cap')
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/ipykernel_launcher.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      





    <matplotlib.axes._subplots.AxesSubplot at 0x126a12ef0>




    
![png](/mlnotes/images/chloropleth_maps_13_2.png)
    



```python
# South America

sa = world[world.continent == 'South America']
sa['gdp_per_cap'] = sa.gdp_md_est / sa.pop_est
sa.plot(column='gdp_per_cap')
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.





    <matplotlib.axes._subplots.AxesSubplot at 0x126bc0470>




    
![png](/mlnotes/images/chloropleth_maps_14_2.png)
    



```python
# With Legend
```


```python
import matplotlib.pyplot as plt
```


```python
fig, ax = plt.subplots(1, 1)

sa = world[world.continent == 'South America']
sa['gdp_per_cap'] = sa.gdp_md_est / sa.pop_est

sa.plot(column = 'pop_est', ax=ax, legend=True)
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.





    <matplotlib.axes._subplots.AxesSubplot at 0x126b8c588>




    
![png](/mlnotes/images/chloropleth_maps_17_2.png)
    



```python
fig, ax = plt.subplots(1, 1)

asia = world[world.continent == 'Asia']
asia['gdp_per_cap'] = asia.gdp_md_est / asia.pop_est

asia.plot(column = 'pop_est', ax=ax, legend=True)
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.





    <matplotlib.axes._subplots.AxesSubplot at 0x127002ef0>




    
![png](/mlnotes/images/chloropleth_maps_18_2.png)
    



```python
fig, ax = plt.subplots(1, 1)

asia = world[world['continent'] == 'Asia']
asia['gdp_per_cap'] = asia['gdp_md_est'] / asia['pop_est']

from mpl_toolkits.axes_grid1 import make_axes_locatable

divider = make_axes_locatable(ax)

cax = divider.append_axes("right", size="4%", pad=0.1)

asia.plot(column = 'pop_est', ax=ax, legend=True, cax=cax)
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.





    <matplotlib.axes._subplots.AxesSubplot at 0x127e412e8>




    
![png](/mlnotes/images/chloropleth_maps_19_2.png)
    



```python
fig, ax = plt.subplots(1, 1)

asia = world[world['continent'] == 'Asia']
asia['gdp_per_cap'] = asia['gdp_md_est'] / asia['pop_est']

from mpl_toolkits.axes_grid1 import make_axes_locatable

divider = make_axes_locatable(ax)

cax = divider.append_axes("right", size="4%", pad=0.1)

asia.plot(column = 'pop_est', ax=ax, legend=True, cax=cax, cmap='YlOrRd')
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.





    <matplotlib.axes._subplots.AxesSubplot at 0x1282e8f98>




    
![png](/mlnotes/images/chloropleth_maps_20_2.png)
    



---
**Score: 20**