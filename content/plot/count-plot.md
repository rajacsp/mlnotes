---
title: Count-Plot
date: 2025-05-17
author: Your Name
cell_count: 8
score: 5
---

---
title: "Count Plot (Buggy)"
author: "Rj"
date: 2020-09-05
description: "List Test"
type: technical_note
draft: false
---

```python
# https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/
```


```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
df_counts = df.groupby(['hwy', 'cty']).size().reset_index(name='counts')

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
      <th>manufacturer</th>
      <th>model</th>
      <th>displ</th>
      <th>year</th>
      <th>cyl</th>
      <th>trans</th>
      <th>drv</th>
      <th>cty</th>
      <th>hwy</th>
      <th>fl</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>audi</td>
      <td>a4</td>
      <td>1.8</td>
      <td>1999</td>
      <td>4</td>
      <td>auto(l5)</td>
      <td>f</td>
      <td>18</td>
      <td>29</td>
      <td>p</td>
      <td>compact</td>
    </tr>
    <tr>
      <th>1</th>
      <td>audi</td>
      <td>a4</td>
      <td>1.8</td>
      <td>1999</td>
      <td>4</td>
      <td>manual(m5)</td>
      <td>f</td>
      <td>21</td>
      <td>29</td>
      <td>p</td>
      <td>compact</td>
    </tr>
    <tr>
      <th>2</th>
      <td>audi</td>
      <td>a4</td>
      <td>2.0</td>
      <td>2008</td>
      <td>4</td>
      <td>manual(m6)</td>
      <td>f</td>
      <td>20</td>
      <td>31</td>
      <td>p</td>
      <td>compact</td>
    </tr>
    <tr>
      <th>3</th>
      <td>audi</td>
      <td>a4</td>
      <td>2.0</td>
      <td>2008</td>
      <td>4</td>
      <td>auto(av)</td>
      <td>f</td>
      <td>21</td>
      <td>30</td>
      <td>p</td>
      <td>compact</td>
    </tr>
    <tr>
      <th>4</th>
      <td>audi</td>
      <td>a4</td>
      <td>2.8</td>
      <td>1999</td>
      <td>6</td>
      <td>auto(l5)</td>
      <td>f</td>
      <td>16</td>
      <td>26</td>
      <td>p</td>
      <td>compact</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_counts
```

    /Users/rajacsp/opt/anaconda3/envs/py38_jupyter/lib/python3.8/site-packages/ipykernel/ipkernel.py:287: DeprecationWarning: `should_run_async` will not call `transform_cell` automatically in the future. Please pass the result to `transformed_cell` argument and any exception that happen during thetransform in `preprocessing_exc_tuple` in IPython 7.17 and above.
      and should_run_async(code)





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
      <th>hwy</th>
      <th>cty</th>
      <th>counts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>12</td>
      <td>9</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14</td>
      <td>11</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15</td>
      <td>11</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16</td>
      <td>11</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>16</td>
      <td>12</td>
      <td>2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>73</th>
      <td>36</td>
      <td>25</td>
      <td>1</td>
    </tr>
    <tr>
      <th>74</th>
      <td>37</td>
      <td>28</td>
      <td>1</td>
    </tr>
    <tr>
      <th>75</th>
      <td>41</td>
      <td>29</td>
      <td>1</td>
    </tr>
    <tr>
      <th>76</th>
      <td>44</td>
      <td>33</td>
      <td>1</td>
    </tr>
    <tr>
      <th>77</th>
      <td>44</td>
      <td>35</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>78 rows × 3 columns</p>
</div>




```python
# Draw Stripplot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)    
sns.stripplot(df_counts.cty, df_counts.hwy, size=df_counts.counts*2, ax=ax)

# Decorations
plt.title('Counts Plot - Size of circle is bigger as more points overlap', fontsize=22)
plt.show()
```

    /Users/rajacsp/opt/anaconda3/envs/py38_jupyter/lib/python3.8/site-packages/ipykernel/ipkernel.py:287: DeprecationWarning: `should_run_async` will not call `transform_cell` automatically in the future. Please pass the result to `transformed_cell` argument and any exception that happen during thetransform in `preprocessing_exc_tuple` in IPython 7.17 and above.
      and should_run_async(code)



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-11-74fe28045231> in <module>
          1 # Draw Stripplot
          2 fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
    ----> 3 sns.stripplot(df_counts.cty, df_counts.hwy, size=df_counts.counts*2, ax=ax)
          4 
          5 # Decorations


    ~/opt/anaconda3/envs/py38_jupyter/lib/python3.8/site-packages/seaborn/categorical.py in stripplot(x, y, hue, data, order, hue_order, jitter, dodge, orient, color, palette, size, edgecolor, linewidth, ax, **kwargs)
       2796                        linewidth=linewidth))
       2797 
    -> 2798     plotter.plot(ax, kwargs)
       2799     return ax
       2800 


    ~/opt/anaconda3/envs/py38_jupyter/lib/python3.8/site-packages/seaborn/categorical.py in plot(self, ax, kws)
       1187     def plot(self, ax, kws):
       1188         """Make the plot."""
    -> 1189         self.draw_stripplot(ax, kws)
       1190         self.add_legend_data(ax)
       1191         self.annotate_axes(ax)


    ~/opt/anaconda3/envs/py38_jupyter/lib/python3.8/site-packages/seaborn/categorical.py in draw_stripplot(self, ax, kws)
       1163                 kws.update(c=palette[point_colors])
       1164                 if self.orient == "v":
    -> 1165                     ax.scatter(cat_pos, strip_data, **kws)
       1166                 else:
       1167                     ax.scatter(strip_data, cat_pos, **kws)


    ~/opt/anaconda3/envs/py38_jupyter/lib/python3.8/site-packages/matplotlib/__init__.py in inner(ax, data, *args, **kwargs)
       1436     def inner(ax, *args, data=None, **kwargs):
       1437         if data is None:
    -> 1438             return func(ax, *map(sanitize_sequence, args), **kwargs)
       1439 
       1440         bound = new_sig.bind(ax, *args, **kwargs)


    ~/opt/anaconda3/envs/py38_jupyter/lib/python3.8/site-packages/matplotlib/cbook/deprecation.py in wrapper(*inner_args, **inner_kwargs)
        409                          else deprecation_addendum,
        410                 **kwargs)
    --> 411         return func(*inner_args, **inner_kwargs)
        412 
        413     return wrapper


    ~/opt/anaconda3/envs/py38_jupyter/lib/python3.8/site-packages/matplotlib/axes/_axes.py in scatter(self, x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, verts, edgecolors, plotnonfinite, **kwargs)
       4446         s = np.ma.ravel(s)
       4447         if len(s) not in (1, x.size):
    -> 4448             raise ValueError("s must be a scalar, or the same size as x and y")
       4449 
       4450         c, colors, edgecolors = \


    ValueError: s must be a scalar, or the same size as x and y



    
![png](/mlnotes/images/count-plot_4_2.png)
    



```python

```


```python

```


```python

```


---
**Score: 5**