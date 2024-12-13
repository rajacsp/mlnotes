---
title: 5-Altair-1
date: 2024-12-13
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
#!pip install altair
```


```python
!pip show altair | grep "Version:"
```

    Version: 5.5.0



```python
import altair as alt
import pandas as pd

data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
alt.Chart(data).mark_line().encode(x='x', y='y')
```





<style>
  #altair-viz-e1d107bb28e049bb91b32d477a2ac2c2.vega-embed {
    width: 100%;
    display: flex;
  }

  #altair-viz-e1d107bb28e049bb91b32d477a2ac2c2.vega-embed details,
  #altair-viz-e1d107bb28e049bb91b32d477a2ac2c2.vega-embed details summary {
    position: relative;
  }
</style>
<div id="altair-viz-e1d107bb28e049bb91b32d477a2ac2c2"></div>
<script type="text/javascript">
  var VEGA_DEBUG = (typeof VEGA_DEBUG == "undefined") ? {} : VEGA_DEBUG;
  (function(spec, embedOpt){
    let outputDiv = document.currentScript.previousElementSibling;
    if (outputDiv.id !== "altair-viz-e1d107bb28e049bb91b32d477a2ac2c2") {
      outputDiv = document.getElementById("altair-viz-e1d107bb28e049bb91b32d477a2ac2c2");
    }

    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm/vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm/vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm/vega-lite@5.20.1?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm/vega-embed@6?noext",
    };

    function maybeLoadScript(lib, version) {
      var key = `${lib.replace("-", "")}_version`;
      return (VEGA_DEBUG[key] == version) ?
        Promise.resolve(paths[lib]) :
        new Promise(function(resolve, reject) {
          var s = document.createElement('script');
          document.getElementsByTagName("head")[0].appendChild(s);
          s.async = true;
          s.onload = () => {
            VEGA_DEBUG[key] = version;
            return resolve(paths[lib]);
          };
          s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
          s.src = paths[lib];
        });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      let deps = ["vega-embed"];
      require(deps, displayChart, err => showError(`Error loading script: ${err.message}`));
    } else {
      maybeLoadScript("vega", "5")
        .then(() => maybeLoadScript("vega-lite", "5.20.1"))
        .then(() => maybeLoadScript("vega-embed", "6"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 300, "continuousHeight": 300}}, "data": {"name": "data-54ce5fc5f3b61e53d857f3764dd891fc"}, "mark": {"type": "line"}, "encoding": {"x": {"field": "x", "type": "quantitative"}, "y": {"field": "y", "type": "quantitative"}}, "$schema": "https://vega.github.io/schema/vega-lite/v5.20.1.json", "datasets": {"data-54ce5fc5f3b61e53d857f3764dd891fc": [{"x": 1, "y": 4}, {"x": 2, "y": 5}, {"x": 3, "y": 6}]}}, {"mode": "vega-lite"});
</script>




```python

```


---
**Score: 5**