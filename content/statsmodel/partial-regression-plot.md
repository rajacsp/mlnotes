---
title: Partial-Regression-Plot
date: 2024-12-07
author: Your Name
cell_count: 25
score: 25
---

---
title: "Partial Regression Plot"
author: "Raja CSP Raman"
date: 2019-04-24
description: "-"
type: technical_note
draft: false
---

```python
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
      <th>81</th>
      <td>86</td>
      <td>W</td>
      <td>Vienne</td>
      <td>15010</td>
      <td>4710</td>
      <td>25</td>
      <td>8922</td>
      <td>35224</td>
      <td>21851</td>
      <td>2:Med</td>
      <td>...</td>
      <td>20</td>
      <td>1</td>
      <td>44</td>
      <td>40</td>
      <td>38</td>
      <td>65</td>
      <td>18</td>
      <td>170.523</td>
      <td>6990</td>
      <td>282.73</td>
    </tr>
    <tr>
      <th>82</th>
      <td>87</td>
      <td>C</td>
      <td>Haute-Vienne</td>
      <td>16256</td>
      <td>6402</td>
      <td>13</td>
      <td>13817</td>
      <td>19940</td>
      <td>33497</td>
      <td>2:Med</td>
      <td>...</td>
      <td>68</td>
      <td>6</td>
      <td>78</td>
      <td>55</td>
      <td>11</td>
      <td>84</td>
      <td>7</td>
      <td>198.874</td>
      <td>5520</td>
      <td>285.13</td>
    </tr>
    <tr>
      <th>83</th>
      <td>88</td>
      <td>E</td>
      <td>Vosges</td>
      <td>18835</td>
      <td>9044</td>
      <td>62</td>
      <td>4040</td>
      <td>14978</td>
      <td>33029</td>
      <td>2:Med</td>
      <td>...</td>
      <td>58</td>
      <td>34</td>
      <td>5</td>
      <td>14</td>
      <td>85</td>
      <td>11</td>
      <td>43</td>
      <td>174.477</td>
      <td>5874</td>
      <td>397.99</td>
    </tr>
    <tr>
      <th>84</th>
      <td>89</td>
      <td>C</td>
      <td>Yonne</td>
      <td>18006</td>
      <td>6516</td>
      <td>47</td>
      <td>4276</td>
      <td>16616</td>
      <td>12789</td>
      <td>2:Med</td>
      <td>...</td>
      <td>32</td>
      <td>22</td>
      <td>35</td>
      <td>51</td>
      <td>66</td>
      <td>27</td>
      <td>272</td>
      <td>81.797</td>
      <td>7427</td>
      <td>352.49</td>
    </tr>
    <tr>
      <th>85</th>
      <td>200</td>
      <td>NaN</td>
      <td>Corse</td>
      <td>2199</td>
      <td>4589</td>
      <td>49</td>
      <td>37015</td>
      <td>24743</td>
      <td>37016</td>
      <td>2:Med</td>
      <td>...</td>
      <td>81</td>
      <td>2</td>
      <td>84</td>
      <td>83</td>
      <td>9</td>
      <td>25</td>
      <td>1</td>
      <td>539.213</td>
      <td>8680</td>
      <td>195.41</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>




```python
selective = ['Department', 'Lottery', 'Literacy', 'Wealth', 'Region']
```


```python
selective
```




    ['Department', 'Lottery', 'Literacy', 'Wealth', 'Region']




```python
df = df[selective]
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
      <th>Department</th>
      <th>Lottery</th>
      <th>Literacy</th>
      <th>Wealth</th>
      <th>Region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ain</td>
      <td>41</td>
      <td>37</td>
      <td>73</td>
      <td>E</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aisne</td>
      <td>38</td>
      <td>51</td>
      <td>22</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Allier</td>
      <td>66</td>
      <td>13</td>
      <td>61</td>
      <td>C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Basses-Alpes</td>
      <td>80</td>
      <td>46</td>
      <td>76</td>
      <td>E</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Hautes-Alpes</td>
      <td>79</td>
      <td>69</td>
      <td>83</td>
      <td>E</td>
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
      <th>Department</th>
      <th>Lottery</th>
      <th>Literacy</th>
      <th>Wealth</th>
      <th>Region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>81</th>
      <td>Vienne</td>
      <td>40</td>
      <td>25</td>
      <td>68</td>
      <td>W</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Haute-Vienne</td>
      <td>55</td>
      <td>13</td>
      <td>67</td>
      <td>C</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Vosges</td>
      <td>14</td>
      <td>62</td>
      <td>82</td>
      <td>E</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Yonne</td>
      <td>51</td>
      <td>47</td>
      <td>30</td>
      <td>C</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Corse</td>
      <td>83</td>
      <td>49</td>
      <td>37</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# drop na

df = df.dropna()
```


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
      <th>Department</th>
      <th>Lottery</th>
      <th>Literacy</th>
      <th>Wealth</th>
      <th>Region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>80</th>
      <td>Vendee</td>
      <td>68</td>
      <td>28</td>
      <td>56</td>
      <td>W</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Vienne</td>
      <td>40</td>
      <td>25</td>
      <td>68</td>
      <td>W</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Haute-Vienne</td>
      <td>55</td>
      <td>13</td>
      <td>67</td>
      <td>C</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Vosges</td>
      <td>14</td>
      <td>62</td>
      <td>82</td>
      <td>E</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Yonne</td>
      <td>51</td>
      <td>47</td>
      <td>30</td>
      <td>C</td>
    </tr>
  </tbody>
</table>
</div>




```python
y, X = dmatrices('Lottery ~ Literacy + Wealth + Region', data=df, return_type='dataframe')
```


```python
y.tail()
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
      <th>Lottery</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>80</th>
      <td>68.0</td>
    </tr>
    <tr>
      <th>81</th>
      <td>40.0</td>
    </tr>
    <tr>
      <th>82</th>
      <td>55.0</td>
    </tr>
    <tr>
      <th>83</th>
      <td>14.0</td>
    </tr>
    <tr>
      <th>84</th>
      <td>51.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
y.head()
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
      <th>Lottery</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>38.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>66.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>80.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>79.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
y[:3]
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
      <th>Lottery</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>38.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>66.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
X[:4]
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
      <th>Intercept</th>
      <th>Region[T.E]</th>
      <th>Region[T.N]</th>
      <th>Region[T.S]</th>
      <th>Region[T.W]</th>
      <th>Literacy</th>
      <th>Wealth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>37.0</td>
      <td>73.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>51.0</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>13.0</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>46.0</td>
      <td>76.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Model fit and Summary

model = sm.OLS(y, X)
```


```python
res = model.fit()
```


```python
print(res.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                Lottery   R-squared:                       0.338
    Model:                            OLS   Adj. R-squared:                  0.287
    Method:                 Least Squares   F-statistic:                     6.636
    Date:                Thu, 25 Apr 2019   Prob (F-statistic):           1.07e-05
    Time:                        20:54:07   Log-Likelihood:                -375.30
    No. Observations:                  85   AIC:                             764.6
    Df Residuals:                      78   BIC:                             781.7
    Df Model:                           6                                         
    Covariance Type:            nonrobust                                         
    ===============================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
    -------------------------------------------------------------------------------
    Intercept      38.6517      9.456      4.087      0.000      19.826      57.478
    Region[T.E]   -15.4278      9.727     -1.586      0.117     -34.793       3.938
    Region[T.N]   -10.0170      9.260     -1.082      0.283     -28.453       8.419
    Region[T.S]    -4.5483      7.279     -0.625      0.534     -19.039       9.943
    Region[T.W]   -10.0913      7.196     -1.402      0.165     -24.418       4.235
    Literacy       -0.1858      0.210     -0.886      0.378      -0.603       0.232
    Wealth          0.4515      0.103      4.390      0.000       0.247       0.656
    ==============================================================================
    Omnibus:                        3.049   Durbin-Watson:                   1.785
    Prob(Omnibus):                  0.218   Jarque-Bera (JB):                2.694
    Skew:                          -0.340   Prob(JB):                        0.260
    Kurtosis:                       2.454   Cond. No.                         371.
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



```python
# Check res params

res.params
```




    Intercept      38.651655
    Region[T.E]   -15.427785
    Region[T.N]   -10.016961
    Region[T.S]    -4.548257
    Region[T.W]   -10.091276
    Literacy       -0.185819
    Wealth          0.451475
    dtype: float64




```python
# Check rsquared

res.rsquared
```




    0.337950869192882




```python
# Rainbow test

sm.stats.linear_rainbow(res)
```




    (0.8472339976156916, 0.6997965543621643)




```python
# Plot 

sm.graphics.plot_partregress('Lottery', 'Wealth', ['Region' ,'Literacy'], data=df, obs_labels = False)
```




    
![png](/mlnotes/images/partial-regression-plot_23_0.png)
    




```python

```


---
**Score: 25**