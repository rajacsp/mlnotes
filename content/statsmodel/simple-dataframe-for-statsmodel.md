---
title: Simple-Dataframe-For-Statsmodel
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

```python
from __future__ import print_function
import statsmodels.api as sm
import pandas as pd
from patsy import dmatrices
```


```python
df = sm.datasets.get_rdataset("Guerry", "HistData").data
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
      <th>dept</th>
      <th>Region</th>
      <th>Department</th>
      <th>Crime_pers</th>
      <th>Crime_prop</th>
      <th>Literacy</th>
      <th>Donations</th>
      <th>Infants</th>
      <th>Suicides</th>
      <th>MainCity</th>
      <th>...</th>
      <th>Crime_parents</th>
      <th>Infanticide</th>
      <th>Donation_clergy</th>
      <th>Lottery</th>
      <th>Desertion</th>
      <th>Instruction</th>
      <th>Prostitutes</th>
      <th>Distance</th>
      <th>Area</th>
      <th>Pop1831</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>E</td>
      <td>Ain</td>
      <td>28870</td>
      <td>15890</td>
      <td>37</td>
      <td>5098</td>
      <td>33120</td>
      <td>35039</td>
      <td>2:Med</td>
      <td>...</td>
      <td>71</td>
      <td>60</td>
      <td>69</td>
      <td>41</td>
      <td>55</td>
      <td>46</td>
      <td>13</td>
      <td>218.372</td>
      <td>5762</td>
      <td>346.03</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>N</td>
      <td>Aisne</td>
      <td>26226</td>
      <td>5521</td>
      <td>51</td>
      <td>8901</td>
      <td>14572</td>
      <td>12831</td>
      <td>2:Med</td>
      <td>...</td>
      <td>4</td>
      <td>82</td>
      <td>36</td>
      <td>38</td>
      <td>82</td>
      <td>24</td>
      <td>327</td>
      <td>65.945</td>
      <td>7369</td>
      <td>513.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>C</td>
      <td>Allier</td>
      <td>26747</td>
      <td>7925</td>
      <td>13</td>
      <td>10973</td>
      <td>17044</td>
      <td>114121</td>
      <td>2:Med</td>
      <td>...</td>
      <td>46</td>
      <td>42</td>
      <td>76</td>
      <td>66</td>
      <td>16</td>
      <td>85</td>
      <td>34</td>
      <td>161.927</td>
      <td>7340</td>
      <td>298.26</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>E</td>
      <td>Basses-Alpes</td>
      <td>12935</td>
      <td>7289</td>
      <td>46</td>
      <td>2733</td>
      <td>23018</td>
      <td>14238</td>
      <td>1:Sm</td>
      <td>...</td>
      <td>70</td>
      <td>12</td>
      <td>37</td>
      <td>80</td>
      <td>32</td>
      <td>29</td>
      <td>2</td>
      <td>351.399</td>
      <td>6925</td>
      <td>155.90</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>E</td>
      <td>Hautes-Alpes</td>
      <td>17488</td>
      <td>8174</td>
      <td>69</td>
      <td>6962</td>
      <td>23076</td>
      <td>16171</td>
      <td>1:Sm</td>
      <td>...</td>
      <td>22</td>
      <td>23</td>
      <td>64</td>
      <td>79</td>
      <td>35</td>
      <td>7</td>
      <td>1</td>
      <td>320.280</td>
      <td>5549</td>
      <td>129.10</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>




```python
df.shape
```




    (86, 23)




```python
df.describe()
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
      <th>dept</th>
      <th>Crime_pers</th>
      <th>Crime_prop</th>
      <th>Literacy</th>
      <th>Donations</th>
      <th>Infants</th>
      <th>Suicides</th>
      <th>Wealth</th>
      <th>Commerce</th>
      <th>Clergy</th>
      <th>Crime_parents</th>
      <th>Infanticide</th>
      <th>Donation_clergy</th>
      <th>Lottery</th>
      <th>Desertion</th>
      <th>Instruction</th>
      <th>Prostitutes</th>
      <th>Distance</th>
      <th>Area</th>
      <th>Pop1831</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>46.883721</td>
      <td>19754.406977</td>
      <td>7843.058140</td>
      <td>39.255814</td>
      <td>7075.546512</td>
      <td>19049.906977</td>
      <td>36522.604651</td>
      <td>43.500000</td>
      <td>42.802326</td>
      <td>43.430233</td>
      <td>43.500000</td>
      <td>43.511628</td>
      <td>43.500000</td>
      <td>43.500000</td>
      <td>43.500000</td>
      <td>43.127907</td>
      <td>141.872093</td>
      <td>207.953140</td>
      <td>6146.988372</td>
      <td>378.628721</td>
    </tr>
    <tr>
      <th>std</th>
      <td>30.426157</td>
      <td>7504.703073</td>
      <td>3051.352839</td>
      <td>17.364051</td>
      <td>5834.595216</td>
      <td>8820.233546</td>
      <td>31312.532649</td>
      <td>24.969982</td>
      <td>25.028370</td>
      <td>24.999549</td>
      <td>24.969982</td>
      <td>24.948297</td>
      <td>24.969982</td>
      <td>24.969982</td>
      <td>24.969982</td>
      <td>24.799809</td>
      <td>520.969318</td>
      <td>109.320837</td>
      <td>1398.246620</td>
      <td>148.777230</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>2199.000000</td>
      <td>1368.000000</td>
      <td>12.000000</td>
      <td>1246.000000</td>
      <td>2660.000000</td>
      <td>3460.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>762.000000</td>
      <td>129.100000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>24.250000</td>
      <td>14156.250000</td>
      <td>5933.000000</td>
      <td>25.000000</td>
      <td>3446.750000</td>
      <td>14299.750000</td>
      <td>15463.000000</td>
      <td>22.250000</td>
      <td>21.250000</td>
      <td>22.250000</td>
      <td>22.250000</td>
      <td>22.250000</td>
      <td>22.250000</td>
      <td>22.250000</td>
      <td>22.250000</td>
      <td>23.250000</td>
      <td>6.000000</td>
      <td>121.383000</td>
      <td>5400.750000</td>
      <td>283.005000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>45.500000</td>
      <td>18748.500000</td>
      <td>7595.000000</td>
      <td>38.000000</td>
      <td>5020.000000</td>
      <td>17141.500000</td>
      <td>26743.500000</td>
      <td>43.500000</td>
      <td>42.500000</td>
      <td>43.500000</td>
      <td>43.500000</td>
      <td>43.500000</td>
      <td>43.500000</td>
      <td>43.500000</td>
      <td>43.500000</td>
      <td>41.500000</td>
      <td>33.000000</td>
      <td>200.616000</td>
      <td>6070.500000</td>
      <td>346.165000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>66.750000</td>
      <td>25937.500000</td>
      <td>9182.250000</td>
      <td>51.750000</td>
      <td>9446.750000</td>
      <td>22682.250000</td>
      <td>44057.500000</td>
      <td>64.750000</td>
      <td>63.750000</td>
      <td>64.750000</td>
      <td>64.750000</td>
      <td>64.750000</td>
      <td>64.750000</td>
      <td>64.750000</td>
      <td>64.750000</td>
      <td>64.750000</td>
      <td>113.750000</td>
      <td>289.670500</td>
      <td>6816.500000</td>
      <td>444.407500</td>
    </tr>
    <tr>
      <th>max</th>
      <td>200.000000</td>
      <td>37014.000000</td>
      <td>20235.000000</td>
      <td>74.000000</td>
      <td>37015.000000</td>
      <td>62486.000000</td>
      <td>163241.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>86.000000</td>
      <td>4744.000000</td>
      <td>539.213000</td>
      <td>10000.000000</td>
      <td>989.940000</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 5**