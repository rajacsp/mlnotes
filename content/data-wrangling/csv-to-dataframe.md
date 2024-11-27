---
title: Csv-To-Dataframe
date: 2024-11-27
author: Your Name
cell_count: 10
score: 10
---

---
title: "CSV to Dataframe"
author: "Rj"
date: 2019-04-22
description: "-"
type: technical_note
draft: false
---

```python
import numpy as np
import pandas as pd
```


```python
csv = pd.DataFrame.from_csv('uk-500.csv')
```

    /Users/rajacsp/anaconda3/envs/py36/lib/python3.6/site-packages/ipykernel_launcher.py:1: FutureWarning: from_csv is deprecated. Please use read_csv(...) instead. Note that some of the default arguments are different, so please refer to the documentation for from_csv when changing your function calls
      """Entry point for launching an IPython kernel.


##### Note

from_csv is deprecated


```python
csv = pd.read_csv('uk-500.csv')
```


```python
csv.head()
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
      <th>first_name</th>
      <th>last_name</th>
      <th>company_name</th>
      <th>address</th>
      <th>city</th>
      <th>county</th>
      <th>postal</th>
      <th>phone1</th>
      <th>phone2</th>
      <th>email</th>
      <th>web</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aleshia</td>
      <td>Tomkiewicz</td>
      <td>Alan D Rosenburg Cpa Pc</td>
      <td>14 Taylor St</td>
      <td>St. Stephens Ward</td>
      <td>Kent</td>
      <td>CT2 7PP</td>
      <td>01835-703597</td>
      <td>01944-369967</td>
      <td>atomkiewicz@hotmail.com</td>
      <td>http://www.alandrosenburgcpapc.co.uk</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Evan</td>
      <td>Zigomalas</td>
      <td>Cap Gemini America</td>
      <td>5 Binney St</td>
      <td>Abbey Ward</td>
      <td>Buckinghamshire</td>
      <td>HP11 2AX</td>
      <td>01937-864715</td>
      <td>01714-737668</td>
      <td>evan.zigomalas@gmail.com</td>
      <td>http://www.capgeminiamerica.co.uk</td>
    </tr>
    <tr>
      <th>2</th>
      <td>France</td>
      <td>Andrade</td>
      <td>Elliott, John W Esq</td>
      <td>8 Moor Place</td>
      <td>East Southbourne and Tuckton W</td>
      <td>Bournemouth</td>
      <td>BH6 3BE</td>
      <td>01347-368222</td>
      <td>01935-821636</td>
      <td>france.andrade@hotmail.com</td>
      <td>http://www.elliottjohnwesq.co.uk</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ulysses</td>
      <td>Mcwalters</td>
      <td>Mcmahan, Ben L</td>
      <td>505 Exeter Rd</td>
      <td>Hawerby cum Beesby</td>
      <td>Lincolnshire</td>
      <td>DN36 5RP</td>
      <td>01912-771311</td>
      <td>01302-601380</td>
      <td>ulysses@hotmail.com</td>
      <td>http://www.mcmahanbenl.co.uk</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tyisha</td>
      <td>Veness</td>
      <td>Champagne Room</td>
      <td>5396 Forth Street</td>
      <td>Greets Green and Lyng Ward</td>
      <td>West Midlands</td>
      <td>B70 9DT</td>
      <td>01547-429341</td>
      <td>01290-367248</td>
      <td>tyisha.veness@hotmail.com</td>
      <td>http://www.champagneroom.co.uk</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv.tail()
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
      <th>first_name</th>
      <th>last_name</th>
      <th>company_name</th>
      <th>address</th>
      <th>city</th>
      <th>county</th>
      <th>postal</th>
      <th>phone1</th>
      <th>phone2</th>
      <th>email</th>
      <th>web</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>495</th>
      <td>Avery</td>
      <td>Veit</td>
      <td>Plaza Gourmet Delicatessen</td>
      <td>9166 Devon St #905</td>
      <td>Knightsbridge and Belgravia Wa</td>
      <td>Greater London</td>
      <td>SW1W 8JY</td>
      <td>01748-625058</td>
      <td>01369-185737</td>
      <td>avery@veit.co.uk</td>
      <td>http://www.plazagourmetdelicatessen.co.uk</td>
    </tr>
    <tr>
      <th>496</th>
      <td>Reid</td>
      <td>Euresti</td>
      <td>Fitzgerald, Edward J</td>
      <td>70 Foster St</td>
      <td>Inverness Ness-Side Ward</td>
      <td>Highland</td>
      <td>IV2 6WT</td>
      <td>01916-963261</td>
      <td>01370-319414</td>
      <td>reuresti@euresti.co.uk</td>
      <td>http://www.fitzgeraldedwardj.co.uk</td>
    </tr>
    <tr>
      <th>497</th>
      <td>Charlette</td>
      <td>Brenning</td>
      <td>Furey &amp; Associates</td>
      <td>714 Fonthill Rd</td>
      <td>Darton West Ward</td>
      <td>South Yorkshire</td>
      <td>S75 5EJ</td>
      <td>01888-152110</td>
      <td>01301-312487</td>
      <td>cbrenning@brenning.co.uk</td>
      <td>http://www.fureyassociates.co.uk</td>
    </tr>
    <tr>
      <th>498</th>
      <td>Celestina</td>
      <td>Keeny</td>
      <td>Bfg Federal Credit Union</td>
      <td>9 Milton St</td>
      <td>Consett North ED</td>
      <td>County Durham</td>
      <td>DH8 5LP</td>
      <td>01877-379681</td>
      <td>01600-463475</td>
      <td>celestina_keeny@gmail.com</td>
      <td>http://www.bfgfederalcreditunion.co.uk</td>
    </tr>
    <tr>
      <th>499</th>
      <td>Mi</td>
      <td>Richan</td>
      <td>Nelson Wright Haworth Golf Crs</td>
      <td>6 Norwood Grove</td>
      <td>Tanworth-in-Arden</td>
      <td>Warwickshire</td>
      <td>B94 5RZ</td>
      <td>01451-785624</td>
      <td>01202-738406</td>
      <td>mi@hotmail.com</td>
      <td>http://www.nelsonwrighthaworthgolfcrs.co.uk</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv.shape
```




    (500, 11)




```python
csv.describe()
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
      <th>first_name</th>
      <th>last_name</th>
      <th>company_name</th>
      <th>address</th>
      <th>city</th>
      <th>county</th>
      <th>postal</th>
      <th>phone1</th>
      <th>phone2</th>
      <th>email</th>
      <th>web</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>479</td>
      <td>498</td>
      <td>498</td>
      <td>500</td>
      <td>468</td>
      <td>102</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>500</td>
      <td>498</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Erasmo</td>
      <td>Devereux</td>
      <td>Martin Morrissey</td>
      <td>860 Rokeby St</td>
      <td>City and Hunslet Ward</td>
      <td>Greater London</td>
      <td>DA17 6EF</td>
      <td>01943-467489</td>
      <td>01992-655281</td>
      <td>fernanda@writer.co.uk</td>
      <td>http://www.martinmorrissey.co.uk</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>44</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 10**