---
title: Sort Rows
date: 2024-12-03
author: Your Name
cell_count: 15
score: 15
---

---
title: "Sort Rows"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import pandas as pd
```


```python
data = {
    'language' : [80, 67, 90],
    'maths' : [100, 78, 98],
    'science' : [98, 77, 56],
    'programming': [100, 100, 90]
}

index = ['chris', 'kevin', 'peter']
```


```python
df = pd.DataFrame(data, index = index)
```


```python
df
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
      <th>language</th>
      <th>maths</th>
      <th>science</th>
      <th>programming</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>chris</th>
      <td>80</td>
      <td>100</td>
      <td>98</td>
      <td>100</td>
    </tr>
    <tr>
      <th>kevin</th>
      <td>67</td>
      <td>78</td>
      <td>77</td>
      <td>100</td>
    </tr>
    <tr>
      <th>peter</th>
      <td>90</td>
      <td>98</td>
      <td>56</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by='maths')
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
      <th>language</th>
      <th>maths</th>
      <th>science</th>
      <th>programming</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>kevin</th>
      <td>67</td>
      <td>78</td>
      <td>77</td>
      <td>100</td>
    </tr>
    <tr>
      <th>peter</th>
      <td>90</td>
      <td>98</td>
      <td>56</td>
      <td>90</td>
    </tr>
    <tr>
      <th>chris</th>
      <td>80</td>
      <td>100</td>
      <td>98</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by='science', ascending=False)
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
      <th>language</th>
      <th>maths</th>
      <th>science</th>
      <th>programming</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>chris</th>
      <td>80</td>
      <td>100</td>
      <td>98</td>
      <td>100</td>
    </tr>
    <tr>
      <th>kevin</th>
      <td>67</td>
      <td>78</td>
      <td>77</td>
      <td>100</td>
    </tr>
    <tr>
      <th>peter</th>
      <td>90</td>
      <td>98</td>
      <td>56</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by=['maths', 'science'])
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
      <th>language</th>
      <th>maths</th>
      <th>science</th>
      <th>programming</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>kevin</th>
      <td>67</td>
      <td>78</td>
      <td>77</td>
      <td>100</td>
    </tr>
    <tr>
      <th>peter</th>
      <td>90</td>
      <td>98</td>
      <td>56</td>
      <td>90</td>
    </tr>
    <tr>
      <th>chris</th>
      <td>80</td>
      <td>100</td>
      <td>98</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by=['maths', 'science'], ascending=False)
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
      <th>language</th>
      <th>maths</th>
      <th>science</th>
      <th>programming</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>chris</th>
      <td>80</td>
      <td>100</td>
      <td>98</td>
      <td>100</td>
    </tr>
    <tr>
      <th>peter</th>
      <td>90</td>
      <td>98</td>
      <td>56</td>
      <td>90</td>
    </tr>
    <tr>
      <th>kevin</th>
      <td>67</td>
      <td>78</td>
      <td>77</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by=['science', 'maths'], ascending=False)
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
      <th>language</th>
      <th>maths</th>
      <th>science</th>
      <th>programming</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>chris</th>
      <td>80</td>
      <td>100</td>
      <td>98</td>
      <td>100</td>
    </tr>
    <tr>
      <th>kevin</th>
      <td>67</td>
      <td>78</td>
      <td>77</td>
      <td>100</td>
    </tr>
    <tr>
      <th>peter</th>
      <td>90</td>
      <td>98</td>
      <td>56</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['max_score'] = df.max(axis=1)
```


```python
df
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
      <th>language</th>
      <th>maths</th>
      <th>science</th>
      <th>programming</th>
      <th>max_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>chris</th>
      <td>80</td>
      <td>100</td>
      <td>98</td>
      <td>100</td>
      <td>100</td>
    </tr>
    <tr>
      <th>kevin</th>
      <td>67</td>
      <td>78</td>
      <td>77</td>
      <td>100</td>
      <td>100</td>
    </tr>
    <tr>
      <th>peter</th>
      <td>90</td>
      <td>98</td>
      <td>56</td>
      <td>90</td>
      <td>98</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['min_score'] = df.min(axis=1)
```


```python
df
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
      <th>language</th>
      <th>maths</th>
      <th>science</th>
      <th>programming</th>
      <th>max_score</th>
      <th>min_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>chris</th>
      <td>80</td>
      <td>100</td>
      <td>98</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
    </tr>
    <tr>
      <th>kevin</th>
      <td>67</td>
      <td>78</td>
      <td>77</td>
      <td>100</td>
      <td>100</td>
      <td>67</td>
    </tr>
    <tr>
      <th>peter</th>
      <td>90</td>
      <td>98</td>
      <td>56</td>
      <td>90</td>
      <td>98</td>
      <td>56</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 15**