---
title: Read-Online-Csv
date: 2024-12-25
author: Your Name
cell_count: 7
score: 5
---

---
title: "Read Online CSV"
author: "Raja CSP Raman"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from io import BytesIO
import requests
import pandas as pd
```


```python
filename = 'https://gitlab.com/rajacsp/datasets/raw/master/amazon_co_ecommerce_sample.csv'

r = requests.get(filename)
data = r.content
```


```python
df = pd.read_csv(BytesIO(data), index_col=0)
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
      <th>product_name</th>
      <th>manufacturer</th>
      <th>price</th>
      <th>number_available_in_stock</th>
      <th>number_of_reviews</th>
      <th>number_of_answered_questions</th>
      <th>average_review_rating</th>
      <th>amazon_category_and_sub_category</th>
      <th>customers_who_bought_this_item_also_bought</th>
      <th>description</th>
      <th>product_information</th>
      <th>product_description</th>
      <th>items_customers_buy_after_viewing_this_item</th>
      <th>customer_questions_and_answers</th>
      <th>customer_reviews</th>
      <th>sellers</th>
    </tr>
    <tr>
      <th>uniq_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
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
      <th>eac7efa5dbd3d667f26eb3d3ab504464</th>
      <td>Hornby 2014 Catalogue</td>
      <td>Hornby</td>
      <td>£3.42</td>
      <td>5 new</td>
      <td>15.0</td>
      <td>1.0</td>
      <td>4.9 out of 5 stars</td>
      <td>Hobbies &gt; Model Trains &amp; Railway Sets &gt; Rail V...</td>
      <td>http://www.amazon.co.uk/Hornby-R8150-Catalogue...</td>
      <td>Product Description Hornby 2014 Catalogue Box ...</td>
      <td>Technical Details Item Weight640 g Product Dim...</td>
      <td>Product Description Hornby 2014 Catalogue Box ...</td>
      <td>http://www.amazon.co.uk/Hornby-R8150-Catalogue...</td>
      <td>Does this catalogue detail all the previous Ho...</td>
      <td>Worth Buying For The Pictures Alone (As Ever) ...</td>
      <td>{"seller"=&gt;[{"Seller_name_1"=&gt;"Amazon.co.uk", ...</td>
    </tr>
    <tr>
      <th>b17540ef7e86e461d37f3ae58b7b72ac</th>
      <td>FunkyBuys® Large Christmas Holiday Express Fes...</td>
      <td>FunkyBuys</td>
      <td>£16.99</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>4.5 out of 5 stars</td>
      <td>Hobbies &gt; Model Trains &amp; Railway Sets &gt; Rail V...</td>
      <td>http://www.amazon.co.uk/Christmas-Holiday-Expr...</td>
      <td>Size Name:Large FunkyBuys® Large Christmas Hol...</td>
      <td>Technical Details Manufacturer recommended age...</td>
      <td>Size Name:Large FunkyBuys® Large Christmas Hol...</td>
      <td>http://www.amazon.co.uk/Christmas-Holiday-Expr...</td>
      <td>can you turn off sounds // hi no you cant turn...</td>
      <td>Four Stars // 4.0 // 18 Dec. 2015 // By\n    \...</td>
      <td>{"seller"=&gt;{"Seller_name_1"=&gt;"UHD WHOLESALE", ...</td>
    </tr>
    <tr>
      <th>348f344247b0c1a935b1223072ef9d8a</th>
      <td>CLASSIC TOY TRAIN SET TRACK CARRIAGES LIGHT EN...</td>
      <td>ccf</td>
      <td>£9.99</td>
      <td>2 new</td>
      <td>17.0</td>
      <td>2.0</td>
      <td>3.9 out of 5 stars</td>
      <td>Hobbies &gt; Model Trains &amp; Railway Sets &gt; Rail V...</td>
      <td>http://www.amazon.co.uk/Classic-Train-Lights-B...</td>
      <td>BIG CLASSIC TOY TRAIN SET TRACK CARRIAGE LIGHT...</td>
      <td>Technical Details Manufacturer recommended age...</td>
      <td>BIG CLASSIC TOY TRAIN SET TRACK CARRIAGE LIGHT...</td>
      <td>http://www.amazon.co.uk/Train-With-Tracks-Batt...</td>
      <td>What is the gauge of the track // Hi Paul.Trut...</td>
      <td>**Highly Recommended!** // 5.0 // 26 May 2015 ...</td>
      <td>{"seller"=&gt;[{"Seller_name_1"=&gt;"DEAL-BOX", "Sel...</td>
    </tr>
    <tr>
      <th>e12b92dbb8eaee78b22965d2a9bbbd9f</th>
      <td>HORNBY Coach R4410A BR Hawksworth Corridor 3rd</td>
      <td>Hornby</td>
      <td>£39.99</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>5.0 out of 5 stars</td>
      <td>Hobbies &gt; Model Trains &amp; Railway Sets &gt; Rail V...</td>
      <td>NaN</td>
      <td>Hornby 00 Gauge BR Hawksworth 3rd Class W 2107...</td>
      <td>Technical Details Item Weight259 g Product Dim...</td>
      <td>Hornby 00 Gauge BR Hawksworth 3rd Class W 2107...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>I love it // 5.0 // 22 July 2013 // By\n    \n...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>e33a9adeed5f36840ccc227db4682a36</th>
      <td>Hornby 00 Gauge 0-4-0 Gildenlow Salt Co. Steam...</td>
      <td>Hornby</td>
      <td>£32.19</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.7 out of 5 stars</td>
      <td>Hobbies &gt; Model Trains &amp; Railway Sets &gt; Rail V...</td>
      <td>http://www.amazon.co.uk/Hornby-R6367-RailRoad-...</td>
      <td>Product Description Hornby RailRoad 0-4-0 Gild...</td>
      <td>Technical Details Item Weight159 g Product Dim...</td>
      <td>Product Description Hornby RailRoad 0-4-0 Gild...</td>
      <td>http://www.amazon.co.uk/Hornby-R2672-RailRoad-...</td>
      <td>NaN</td>
      <td>Birthday present // 5.0 // 14 April 2014 // By...</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# source : https://stackoverflow.com/questions/19611729/getting-google-spreadsheet-csv-into-a-pandas-dataframe
```


```python

```


---
**Score: 5**