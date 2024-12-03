---
title: Xml-File-To-Dict
date: 2024-12-03
author: Your Name
cell_count: 6
score: 5
---

---
title: "XML File to Dictionary"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import xmltodict
import pprint
import json
```


```python
with open('sample.xml') as fd:
    doc1 = xmltodict.parse(fd.read())
```


```python
doc1
```




    OrderedDict([('note',
                  OrderedDict([('to', 'Tove'),
                               ('from', 'Jani'),
                               ('heading', 'Reminder'),
                               ('body', "Don't forget me this weekend!")]))])




```python
doc1['note']['heading']
```




    'Reminder'




```python

```


---
**Score: 5**