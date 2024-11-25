---
title: World Map
date: 2024-11-25
author: Your Name
cell_count: 6
score: 5
---

---
title: "World Map"
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
world
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
    <tr>
      <th>5</th>
      <td>18556698</td>
      <td>Asia</td>
      <td>Kazakhstan</td>
      <td>KAZ</td>
      <td>460700.0</td>
      <td>POLYGON ((87.35997033076265 49.21498078062912,...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>29748859</td>
      <td>Asia</td>
      <td>Uzbekistan</td>
      <td>UZB</td>
      <td>202300.0</td>
      <td>POLYGON ((55.96819135928291 41.30864166926936,...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6909701</td>
      <td>Oceania</td>
      <td>Papua New Guinea</td>
      <td>PNG</td>
      <td>28020.0</td>
      <td>(POLYGON ((141.0002104025918 -2.60015105551566...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>260580739</td>
      <td>Asia</td>
      <td>Indonesia</td>
      <td>IDN</td>
      <td>3028000.0</td>
      <td>(POLYGON ((141.0002104025918 -2.60015105551566...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>44293293</td>
      <td>South America</td>
      <td>Argentina</td>
      <td>ARG</td>
      <td>879400.0</td>
      <td>(POLYGON ((-68.63401022758323 -52.636370458874...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>17789267</td>
      <td>South America</td>
      <td>Chile</td>
      <td>CHL</td>
      <td>436100.0</td>
      <td>(POLYGON ((-68.63401022758323 -52.636370458874...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>83301151</td>
      <td>Africa</td>
      <td>Dem. Rep. Congo</td>
      <td>COD</td>
      <td>66010.0</td>
      <td>POLYGON ((29.33999759290035 -4.499983412294092...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>7531386</td>
      <td>Africa</td>
      <td>Somalia</td>
      <td>SOM</td>
      <td>4719.0</td>
      <td>POLYGON ((41.58513 -1.68325, 40.993 -0.85829, ...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>47615739</td>
      <td>Africa</td>
      <td>Kenya</td>
      <td>KEN</td>
      <td>152700.0</td>
      <td>POLYGON ((39.20222 -4.67677, 37.7669 -3.67712,...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>37345935</td>
      <td>Africa</td>
      <td>Sudan</td>
      <td>SDN</td>
      <td>176300.0</td>
      <td>POLYGON ((24.56736901215208 8.229187933785468,...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>12075985</td>
      <td>Africa</td>
      <td>Chad</td>
      <td>TCD</td>
      <td>30590.0</td>
      <td>POLYGON ((23.83766000000014 19.5804700000001, ...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>10646714</td>
      <td>North America</td>
      <td>Haiti</td>
      <td>HTI</td>
      <td>19340.0</td>
      <td>POLYGON ((-71.71236141629296 19.71445587816736...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>10734247</td>
      <td>North America</td>
      <td>Dominican Rep.</td>
      <td>DOM</td>
      <td>161900.0</td>
      <td>POLYGON ((-71.70830481635805 18.04499705654609...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>142257519</td>
      <td>Europe</td>
      <td>Russia</td>
      <td>RUS</td>
      <td>3745000.0</td>
      <td>(POLYGON ((178.7253 71.0988, 180.0000000000001...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>329988</td>
      <td>North America</td>
      <td>Bahamas</td>
      <td>BHS</td>
      <td>9066.0</td>
      <td>(POLYGON ((-78.98 26.79, -78.51000000000001 26...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2931</td>
      <td>South America</td>
      <td>Falkland Is.</td>
      <td>FLK</td>
      <td>281.8</td>
      <td>POLYGON ((-61.2 -51.85, -60 -51.25, -59.15 -51...</td>
    </tr>
    <tr>
      <th>21</th>
      <td>5320045</td>
      <td>Europe</td>
      <td>Norway</td>
      <td>-99</td>
      <td>364700.0</td>
      <td>(POLYGON ((15.14282 79.67431000000001, 15.5225...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>57713</td>
      <td>North America</td>
      <td>Greenland</td>
      <td>GRL</td>
      <td>2173.0</td>
      <td>POLYGON ((-46.76379 82.62796, -43.40644 83.225...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>140</td>
      <td>Seven seas (open ocean)</td>
      <td>Fr. S. Antarctic Lands</td>
      <td>ATF</td>
      <td>16.0</td>
      <td>POLYGON ((68.935 -48.62500000000001, 69.58 -48...</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1291358</td>
      <td>Asia</td>
      <td>Timor-Leste</td>
      <td>TLS</td>
      <td>4975.0</td>
      <td>POLYGON ((124.9686824891162 -8.892790215697083...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>54841552</td>
      <td>Africa</td>
      <td>South Africa</td>
      <td>ZAF</td>
      <td>739100.0</td>
      <td>POLYGON ((16.34497684089524 -28.5767050106977,...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1958042</td>
      <td>Africa</td>
      <td>Lesotho</td>
      <td>LSO</td>
      <td>6019.0</td>
      <td>POLYGON ((28.97826256685724 -28.95559661226171...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>124574795</td>
      <td>North America</td>
      <td>Mexico</td>
      <td>MEX</td>
      <td>2307000.0</td>
      <td>POLYGON ((-117.1277599999999 32.53533999999996...</td>
    </tr>
    <tr>
      <th>28</th>
      <td>3360148</td>
      <td>South America</td>
      <td>Uruguay</td>
      <td>URY</td>
      <td>73250.0</td>
      <td>POLYGON ((-57.62513342958296 -30.2162948544542...</td>
    </tr>
    <tr>
      <th>29</th>
      <td>207353391</td>
      <td>South America</td>
      <td>Brazil</td>
      <td>BRA</td>
      <td>3081000.0</td>
      <td>POLYGON ((-53.37366166849824 -33.7683777809007...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>147</th>
      <td>104256076</td>
      <td>Asia</td>
      <td>Philippines</td>
      <td>PHL</td>
      <td>801900.0</td>
      <td>(POLYGON ((120.8338961121466 12.70449616134243...</td>
    </tr>
    <tr>
      <th>148</th>
      <td>31381992</td>
      <td>Asia</td>
      <td>Malaysia</td>
      <td>MYS</td>
      <td>863000.0</td>
      <td>(POLYGON ((100.0857568705271 6.464489447450291...</td>
    </tr>
    <tr>
      <th>149</th>
      <td>443593</td>
      <td>Asia</td>
      <td>Brunei</td>
      <td>BRN</td>
      <td>33730.0</td>
      <td>POLYGON ((115.4507104838698 5.447729803891534,...</td>
    </tr>
    <tr>
      <th>150</th>
      <td>1972126</td>
      <td>Europe</td>
      <td>Slovenia</td>
      <td>SVN</td>
      <td>68350.0</td>
      <td>POLYGON ((13.80647545742153 46.50930613869122,...</td>
    </tr>
    <tr>
      <th>151</th>
      <td>5491218</td>
      <td>Europe</td>
      <td>Finland</td>
      <td>FIN</td>
      <td>224137.0</td>
      <td>POLYGON ((28.59192955904319 69.06477692328666,...</td>
    </tr>
    <tr>
      <th>152</th>
      <td>5445829</td>
      <td>Europe</td>
      <td>Slovakia</td>
      <td>SVK</td>
      <td>168800.0</td>
      <td>POLYGON ((22.55813764821175 49.08573802346714,...</td>
    </tr>
    <tr>
      <th>153</th>
      <td>10674723</td>
      <td>Europe</td>
      <td>Czechia</td>
      <td>CZE</td>
      <td>350900.0</td>
      <td>POLYGON ((15.01699588385867 51.10667409932158,...</td>
    </tr>
    <tr>
      <th>154</th>
      <td>5918919</td>
      <td>Africa</td>
      <td>Eritrea</td>
      <td>ERI</td>
      <td>9169.0</td>
      <td>POLYGON ((36.42951000000005 14.42211000000003,...</td>
    </tr>
    <tr>
      <th>155</th>
      <td>126451398</td>
      <td>Asia</td>
      <td>Japan</td>
      <td>JPN</td>
      <td>4932000.0</td>
      <td>(POLYGON ((141.884600864835 39.18086456965148,...</td>
    </tr>
    <tr>
      <th>156</th>
      <td>6943739</td>
      <td>South America</td>
      <td>Paraguay</td>
      <td>PRY</td>
      <td>64670.0</td>
      <td>POLYGON ((-58.16639238140804 -20.1767009416536...</td>
    </tr>
    <tr>
      <th>157</th>
      <td>28036829</td>
      <td>Asia</td>
      <td>Yemen</td>
      <td>YEM</td>
      <td>73450.0</td>
      <td>POLYGON ((52.00000980002224 19.00000336351606,...</td>
    </tr>
    <tr>
      <th>158</th>
      <td>28571770</td>
      <td>Asia</td>
      <td>Saudi Arabia</td>
      <td>SAU</td>
      <td>1731000.0</td>
      <td>POLYGON ((34.95603722508426 29.35655467377885,...</td>
    </tr>
    <tr>
      <th>159</th>
      <td>4050</td>
      <td>Antarctica</td>
      <td>Antarctica</td>
      <td>ATA</td>
      <td>810.0</td>
      <td>(POLYGON ((-48.66061601418252 -78.047018731598...</td>
    </tr>
    <tr>
      <th>160</th>
      <td>265100</td>
      <td>Asia</td>
      <td>N. Cyprus</td>
      <td>-99</td>
      <td>3600.0</td>
      <td>POLYGON ((32.73178022637745 35.14002594658844,...</td>
    </tr>
    <tr>
      <th>161</th>
      <td>1221549</td>
      <td>Asia</td>
      <td>Cyprus</td>
      <td>CYP</td>
      <td>29260.0</td>
      <td>POLYGON ((32.73178022637745 35.14002594658844,...</td>
    </tr>
    <tr>
      <th>162</th>
      <td>33986655</td>
      <td>Africa</td>
      <td>Morocco</td>
      <td>MAR</td>
      <td>282800.0</td>
      <td>POLYGON ((-2.169913702798624 35.16839630791668...</td>
    </tr>
    <tr>
      <th>163</th>
      <td>97041072</td>
      <td>Africa</td>
      <td>Egypt</td>
      <td>EGY</td>
      <td>1105000.0</td>
      <td>POLYGON ((36.86622999999997 22, 32.89999999999...</td>
    </tr>
    <tr>
      <th>164</th>
      <td>6653210</td>
      <td>Africa</td>
      <td>Libya</td>
      <td>LBY</td>
      <td>90890.0</td>
      <td>POLYGON ((25 22, 25.00000000000011 20.00304000...</td>
    </tr>
    <tr>
      <th>165</th>
      <td>105350020</td>
      <td>Africa</td>
      <td>Ethiopia</td>
      <td>ETH</td>
      <td>174700.0</td>
      <td>POLYGON ((47.78942 8.003, 44.96360000000001 5....</td>
    </tr>
    <tr>
      <th>166</th>
      <td>865267</td>
      <td>Africa</td>
      <td>Djibouti</td>
      <td>DJI</td>
      <td>3345.0</td>
      <td>POLYGON ((42.35156000000012 12.54223000000013,...</td>
    </tr>
    <tr>
      <th>167</th>
      <td>3500000</td>
      <td>Africa</td>
      <td>Somaliland</td>
      <td>-99</td>
      <td>12250.0</td>
      <td>POLYGON ((48.94820475850985 11.41061728169797,...</td>
    </tr>
    <tr>
      <th>168</th>
      <td>39570125</td>
      <td>Africa</td>
      <td>Uganda</td>
      <td>UGA</td>
      <td>84930.0</td>
      <td>POLYGON ((33.90371119710453 -0.950000000000000...</td>
    </tr>
    <tr>
      <th>169</th>
      <td>11901484</td>
      <td>Africa</td>
      <td>Rwanda</td>
      <td>RWA</td>
      <td>21970.0</td>
      <td>POLYGON ((30.41910485201925 -1.134659112150416...</td>
    </tr>
    <tr>
      <th>170</th>
      <td>3856181</td>
      <td>Europe</td>
      <td>Bosnia and Herz.</td>
      <td>BIH</td>
      <td>42530.0</td>
      <td>POLYGON ((18.55999999999995 42.64999999999998,...</td>
    </tr>
    <tr>
      <th>171</th>
      <td>2103721</td>
      <td>Europe</td>
      <td>Macedonia</td>
      <td>MKD</td>
      <td>29520.0</td>
      <td>POLYGON ((22.38052575042459 42.32025950781509,...</td>
    </tr>
    <tr>
      <th>172</th>
      <td>7111024</td>
      <td>Europe</td>
      <td>Serbia</td>
      <td>SRB</td>
      <td>101800.0</td>
      <td>POLYGON ((18.82982479287395 45.90887235802528,...</td>
    </tr>
    <tr>
      <th>173</th>
      <td>642550</td>
      <td>Europe</td>
      <td>Montenegro</td>
      <td>MNE</td>
      <td>10610.0</td>
      <td>POLYGON ((20.07070000000004 42.58863000000008,...</td>
    </tr>
    <tr>
      <th>174</th>
      <td>1895250</td>
      <td>Europe</td>
      <td>Kosovo</td>
      <td>-99</td>
      <td>18490.0</td>
      <td>POLYGON ((20.59024654668023 41.85540891928363,...</td>
    </tr>
    <tr>
      <th>175</th>
      <td>1218208</td>
      <td>North America</td>
      <td>Trinidad and Tobago</td>
      <td>TTO</td>
      <td>43570.0</td>
      <td>POLYGON ((-61.68000000000001 10.76, -61.105 10...</td>
    </tr>
    <tr>
      <th>176</th>
      <td>13026129</td>
      <td>Africa</td>
      <td>S. Sudan</td>
      <td>SSD</td>
      <td>20880.0</td>
      <td>POLYGON ((30.83385242171543 3.509171604222463,...</td>
    </tr>
  </tbody>
</table>
<p>177 rows × 6 columns</p>
</div>




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
world.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x128a30748>




    
![png](/mlnotes/images/world_map_5_1.png)
    



---
**Score: 5**