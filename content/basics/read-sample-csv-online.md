---
title: Read-Sample-Csv-Online
date: 2025-01-04
author: Your Name
cell_count: 8
score: 5
---

---
title: "Read Sample CSV Online"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
'''
https://stackoverflow.com/questions/22216076/unicodedecodeerror-utf8-codec-cant-decode-byte-0xa5-in-position-0-invalid-s
'''
```




    '\nhttps://stackoverflow.com/questions/22216076/unicodedecodeerror-utf8-codec-cant-decode-byte-0xa5-in-position-0-invalid-s\n'




```python
from io import BytesIO
import requests
import pandas as pd
```


```python
filename = 'https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv'

r = requests.get(filename)
data = r.content
```


```python
df = pd.read_csv(BytesIO(data), index_col=0, encoding = 'unicode_escape')
```


```python
df.head()
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
      <th>Eldon Base for stackable storage shelf, platinum</th>
      <th>Muhammed MacIntyre</th>
      <th>3</th>
      <th>-213.25</th>
      <th>38.94</th>
      <th>35</th>
      <th>Nunavut</th>
      <th>Storage &amp; Organization</th>
      <th>0.8</th>
    </tr>
    <tr>
      <th>1</th>
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
      <th>2</th>
      <td>1.7 Cubic Foot Compact "Cube" Office Refrigera...</td>
      <td>Barry French</td>
      <td>293</td>
      <td>457.81</td>
      <td>208.16</td>
      <td>68.02</td>
      <td>Nunavut</td>
      <td>Appliances</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Cardinal Slant-D® Ring Binder, Heavy Gauge Vinyl</td>
      <td>Barry French</td>
      <td>293</td>
      <td>46.71</td>
      <td>8.69</td>
      <td>2.99</td>
      <td>Nunavut</td>
      <td>Binders and Binder Accessories</td>
      <td>0.39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>R380</td>
      <td>Clay Rozendal</td>
      <td>483</td>
      <td>1198.97</td>
      <td>195.99</td>
      <td>3.99</td>
      <td>Nunavut</td>
      <td>Telephones and Communication</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Holmes HEPA Air Purifier</td>
      <td>Carlos Soltero</td>
      <td>515</td>
      <td>30.94</td>
      <td>21.78</td>
      <td>5.94</td>
      <td>Nunavut</td>
      <td>Appliances</td>
      <td>0.50</td>
    </tr>
    <tr>
      <th>6</th>
      <td>G.E. Longer-Life Indoor Recessed Floodlight Bulbs</td>
      <td>Carlos Soltero</td>
      <td>515</td>
      <td>4.43</td>
      <td>6.64</td>
      <td>4.95</td>
      <td>Nunavut</td>
      <td>Office Furnishings</td>
      <td>0.37</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail()
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
      <th>Eldon Base for stackable storage shelf, platinum</th>
      <th>Muhammed MacIntyre</th>
      <th>3</th>
      <th>-213.25</th>
      <th>38.94</th>
      <th>35</th>
      <th>Nunavut</th>
      <th>Storage &amp; Organization</th>
      <th>0.8</th>
    </tr>
    <tr>
      <th>1</th>
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
      <th>6</th>
      <td>G.E. Longer-Life Indoor Recessed Floodlight Bulbs</td>
      <td>Carlos Soltero</td>
      <td>515</td>
      <td>4.43</td>
      <td>6.64</td>
      <td>4.95</td>
      <td>Nunavut</td>
      <td>Office Furnishings</td>
      <td>0.37</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Angle-D Binders with Locking Rings, Label Holders</td>
      <td>Carl Jackson</td>
      <td>613</td>
      <td>-54.04</td>
      <td>7.30</td>
      <td>7.72</td>
      <td>Nunavut</td>
      <td>Binders and Binder Accessories</td>
      <td>0.38</td>
    </tr>
    <tr>
      <th>8</th>
      <td>SAFCO Mobile Desk Side File, Wire Frame</td>
      <td>Carl Jackson</td>
      <td>613</td>
      <td>127.70</td>
      <td>42.76</td>
      <td>6.22</td>
      <td>Nunavut</td>
      <td>Storage &amp; Organization</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>SAFCO Commercial Wire Shelving, Black</td>
      <td>Monica Federle</td>
      <td>643</td>
      <td>-695.26</td>
      <td>138.14</td>
      <td>35.00</td>
      <td>Nunavut</td>
      <td>Storage &amp; Organization</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Xerox 198</td>
      <td>Dorothy Badders</td>
      <td>678</td>
      <td>-226.36</td>
      <td>4.98</td>
      <td>8.33</td>
      <td>Nunavut</td>
      <td>Paper</td>
      <td>0.38</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 5**