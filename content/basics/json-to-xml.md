---
title: Json-To-Xml
date: 2024-12-26
author: Your Name
cell_count: 7
score: 5
---

---
title: "JSON to XML"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import xmltodict
```


```python
content = {
  "note" : {
    "to" : "Tove",
    "from" : "Jani",
    "heading" : "Reminder",
    "body" : "Don't forget me this weekend!"
  }
}
```


```python
content
```




    {'note': {'body': "Don't forget me this weekend!",
      'from': 'Jani',
      'heading': 'Reminder',
      'to': 'Tove'}}




```python
xml = xmltodict.unparse(content, pretty=True)
```


```python
xml
```




    '<?xml version="1.0" encoding="utf-8"?>\n<note>\n\t<to>Tove</to>\n\t<from>Jani</from>\n\t<heading>Reminder</heading>\n\t<body>Don\'t forget me this weekend!</body>\n</note>'




```python

```


---
**Score: 5**