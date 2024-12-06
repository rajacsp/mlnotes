---
title: Decision-Tree-Graph
date: 2024-12-06
author: Your Name
cell_count: 11
score: 10
---

---
title: "Decision Tree Graph"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
import pydotplus
from sklearn.datasets import load_iris
from sklearn import tree
import collections
```


```python
# Data Collection
#heigh, length of hair, voice pitch
X = [ [180, 15,0],     
      [177, 42,0],
      [136, 35,1],
      [174, 65,0],
      [141, 28,1]]
```


```python
Y = ['man', 'woman', 'woman', 'man', 'woman']    
 
data_feature_names = [ 'height', 'hair length', 'voice pitch' ]
```


```python
print(data_feature_names)
```

    ['height', 'hair length', 'voice pitch']



```python
# Training
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
```


```python
# Visualize data
dot_data = tree.export_graphviz(clf,
                                feature_names=data_feature_names,
                                out_file=None,
                                filled=True,
                                rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data)
```


```python
colors = ('turquoise', 'orange')
edges = collections.defaultdict(list)
```


```python
for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))
```


```python
for edge in edges:
    edges[edge].sort()    
    for i in range(2):
        dest = graph.get_node(str(edges[edge][i]))[0]
        dest.set_fillcolor(colors[i])
```


```python
graph
```




    <pydotplus.graphviz.Dot at 0x1209bf198>




---
**Score: 10**