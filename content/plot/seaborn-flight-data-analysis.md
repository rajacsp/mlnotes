---
title: Seaborn-Flight-Data-Analysis
date: 2024-12-06
author: Your Name
cell_count: 23
score: 20
---

```python
# https://seaborn.pydata.org/generated/seaborn.lineplot.html
# https://rajacsp.github.io/mlnotes/python/data-wrangling/food_points/
```


```python
import seaborn as sns
```


```python
flights = sns.load_dataset("flights")
flights.head()
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
      <th>year</th>
      <th>month</th>
      <th>passengers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1949</td>
      <td>Jan</td>
      <td>112</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949</td>
      <td>Feb</td>
      <td>118</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1949</td>
      <td>Mar</td>
      <td>132</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1949</td>
      <td>Apr</td>
      <td>129</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1949</td>
      <td>May</td>
      <td>121</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(flights)
```




    pandas.core.frame.DataFrame




```python
may_flights = flights.query("month == 'May'")
sns.lineplot(data=may_flights, x="year", y="passengers")
```




    <Axes: xlabel='year', ylabel='passengers'>




    
![png](/mlnotes/images/seaborn-flight-data-analysis_4_1.png)
    



```python
flights.head()
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
      <th>year</th>
      <th>month</th>
      <th>passengers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1949</td>
      <td>Jan</td>
      <td>112</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949</td>
      <td>Feb</td>
      <td>118</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1949</td>
      <td>Mar</td>
      <td>132</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1949</td>
      <td>Apr</td>
      <td>129</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1949</td>
      <td>May</td>
      <td>121</td>
    </tr>
  </tbody>
</table>
</div>




```python
flights_wide = flights.pivot(index="year", columns="month", values="passengers")
flights_wide.head()
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
      <th>month</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
      <th>Apr</th>
      <th>May</th>
      <th>Jun</th>
      <th>Jul</th>
      <th>Aug</th>
      <th>Sep</th>
      <th>Oct</th>
      <th>Nov</th>
      <th>Dec</th>
    </tr>
    <tr>
      <th>year</th>
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
      <th>1949</th>
      <td>112</td>
      <td>118</td>
      <td>132</td>
      <td>129</td>
      <td>121</td>
      <td>135</td>
      <td>148</td>
      <td>148</td>
      <td>136</td>
      <td>119</td>
      <td>104</td>
      <td>118</td>
    </tr>
    <tr>
      <th>1950</th>
      <td>115</td>
      <td>126</td>
      <td>141</td>
      <td>135</td>
      <td>125</td>
      <td>149</td>
      <td>170</td>
      <td>170</td>
      <td>158</td>
      <td>133</td>
      <td>114</td>
      <td>140</td>
    </tr>
    <tr>
      <th>1951</th>
      <td>145</td>
      <td>150</td>
      <td>178</td>
      <td>163</td>
      <td>172</td>
      <td>178</td>
      <td>199</td>
      <td>199</td>
      <td>184</td>
      <td>162</td>
      <td>146</td>
      <td>166</td>
    </tr>
    <tr>
      <th>1952</th>
      <td>171</td>
      <td>180</td>
      <td>193</td>
      <td>181</td>
      <td>183</td>
      <td>218</td>
      <td>230</td>
      <td>242</td>
      <td>209</td>
      <td>191</td>
      <td>172</td>
      <td>194</td>
    </tr>
    <tr>
      <th>1953</th>
      <td>196</td>
      <td>196</td>
      <td>236</td>
      <td>235</td>
      <td>229</td>
      <td>243</td>
      <td>264</td>
      <td>272</td>
      <td>237</td>
      <td>211</td>
      <td>180</td>
      <td>201</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.lineplot(data=flights_wide["May"])
```




    <Axes: xlabel='year', ylabel='May'>




    
![png](/mlnotes/images/seaborn-flight-data-analysis_7_1.png)
    



```python
sns.lineplot(data=flights_wide["Oct"])
```




    <Axes: xlabel='year', ylabel='Oct'>




    
![png](/mlnotes/images/seaborn-flight-data-analysis_8_1.png)
    



```python
sns.lineplot(data=flights_wide)
```




    <Axes: xlabel='year'>




    
![png](/mlnotes/images/seaborn-flight-data-analysis_9_1.png)
    



```python
flights_wide
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
      <th>month</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
      <th>Apr</th>
      <th>May</th>
      <th>Jun</th>
      <th>Jul</th>
      <th>Aug</th>
      <th>Sep</th>
      <th>Oct</th>
      <th>Nov</th>
      <th>Dec</th>
    </tr>
    <tr>
      <th>year</th>
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
      <th>1949</th>
      <td>112</td>
      <td>118</td>
      <td>132</td>
      <td>129</td>
      <td>121</td>
      <td>135</td>
      <td>148</td>
      <td>148</td>
      <td>136</td>
      <td>119</td>
      <td>104</td>
      <td>118</td>
    </tr>
    <tr>
      <th>1950</th>
      <td>115</td>
      <td>126</td>
      <td>141</td>
      <td>135</td>
      <td>125</td>
      <td>149</td>
      <td>170</td>
      <td>170</td>
      <td>158</td>
      <td>133</td>
      <td>114</td>
      <td>140</td>
    </tr>
    <tr>
      <th>1951</th>
      <td>145</td>
      <td>150</td>
      <td>178</td>
      <td>163</td>
      <td>172</td>
      <td>178</td>
      <td>199</td>
      <td>199</td>
      <td>184</td>
      <td>162</td>
      <td>146</td>
      <td>166</td>
    </tr>
    <tr>
      <th>1952</th>
      <td>171</td>
      <td>180</td>
      <td>193</td>
      <td>181</td>
      <td>183</td>
      <td>218</td>
      <td>230</td>
      <td>242</td>
      <td>209</td>
      <td>191</td>
      <td>172</td>
      <td>194</td>
    </tr>
    <tr>
      <th>1953</th>
      <td>196</td>
      <td>196</td>
      <td>236</td>
      <td>235</td>
      <td>229</td>
      <td>243</td>
      <td>264</td>
      <td>272</td>
      <td>237</td>
      <td>211</td>
      <td>180</td>
      <td>201</td>
    </tr>
    <tr>
      <th>1954</th>
      <td>204</td>
      <td>188</td>
      <td>235</td>
      <td>227</td>
      <td>234</td>
      <td>264</td>
      <td>302</td>
      <td>293</td>
      <td>259</td>
      <td>229</td>
      <td>203</td>
      <td>229</td>
    </tr>
    <tr>
      <th>1955</th>
      <td>242</td>
      <td>233</td>
      <td>267</td>
      <td>269</td>
      <td>270</td>
      <td>315</td>
      <td>364</td>
      <td>347</td>
      <td>312</td>
      <td>274</td>
      <td>237</td>
      <td>278</td>
    </tr>
    <tr>
      <th>1956</th>
      <td>284</td>
      <td>277</td>
      <td>317</td>
      <td>313</td>
      <td>318</td>
      <td>374</td>
      <td>413</td>
      <td>405</td>
      <td>355</td>
      <td>306</td>
      <td>271</td>
      <td>306</td>
    </tr>
    <tr>
      <th>1957</th>
      <td>315</td>
      <td>301</td>
      <td>356</td>
      <td>348</td>
      <td>355</td>
      <td>422</td>
      <td>465</td>
      <td>467</td>
      <td>404</td>
      <td>347</td>
      <td>305</td>
      <td>336</td>
    </tr>
    <tr>
      <th>1958</th>
      <td>340</td>
      <td>318</td>
      <td>362</td>
      <td>348</td>
      <td>363</td>
      <td>435</td>
      <td>491</td>
      <td>505</td>
      <td>404</td>
      <td>359</td>
      <td>310</td>
      <td>337</td>
    </tr>
    <tr>
      <th>1959</th>
      <td>360</td>
      <td>342</td>
      <td>406</td>
      <td>396</td>
      <td>420</td>
      <td>472</td>
      <td>548</td>
      <td>559</td>
      <td>463</td>
      <td>407</td>
      <td>362</td>
      <td>405</td>
    </tr>
    <tr>
      <th>1960</th>
      <td>417</td>
      <td>391</td>
      <td>419</td>
      <td>461</td>
      <td>472</td>
      <td>535</td>
      <td>622</td>
      <td>606</td>
      <td>508</td>
      <td>461</td>
      <td>390</td>
      <td>432</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd
```


```python
data = {
    'month' : [0, 1, 2],
    'raja' : [0, 300, 450],
    'hari' : [0, 200, 500]
}
```


```python
df = pd.DataFrame(data)
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
      <th>month</th>
      <th>raja</th>
      <th>hari</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>300</td>
      <td>200</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>450</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.lineplot(data=df)
```




    <Axes: >




    
![png](/mlnotes/images/seaborn-flight-data-analysis_15_1.png)
    



```python

```


```python
data = {
    'days' : [1, 1, 1, 2, 2, 2],
    'learners' : ['raja', 'hari', 'steve', 'raja', 'hari', 'steve'],
    'score' : [0, 0, 0, 50, 40, 60]
}

# 1949 Jan 112
# day:1 hari 0
# day:1 steve 0
```


```python
df = pd.DataFrame(data)
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
      <th>days</th>
      <th>learners</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>raja</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>hari</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>steve</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>raja</td>
      <td>50</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>hari</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>steve</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_wide = df.pivot(index="days", columns="learners", values="score")
df_wide.head()
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
      <th>learners</th>
      <th>hari</th>
      <th>raja</th>
      <th>steve</th>
    </tr>
    <tr>
      <th>days</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40</td>
      <td>50</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.lineplot(data=df_wide)
```




    <Axes: xlabel='days'>




    
![png](/mlnotes/images/seaborn-flight-data-analysis_21_1.png)
    



```python

```


---
**Score: 20**