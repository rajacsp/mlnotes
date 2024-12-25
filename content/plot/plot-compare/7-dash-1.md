---
title: 7-Dash-1
date: 2024-12-25
author: Your Name
cell_count: 7
score: 5
---

```python
import pyutil as pyu
```


```python
pyu.get_local_pyinfo()
```




    'conda env: ml312-2024; pyv: 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:27:36) [GCC 11.2.0]'




```python

```


```python
!pip show dash | grep "Version:"
```

    Version: 2.18.2



```python
from dash import Dash, dcc, html
import plotly.express as px

app = Dash(__name__)
fig = px.scatter(x=[1, 2, 3], y=[4, 5, 6])

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
```



<iframe
    width="100%"
    height="650"
    src="http://127.0.0.1:8050/"
    frameborder="0"
    allowfullscreen

></iframe>




```python

```


```python

```


---
**Score: 5**