---
title: Xml-To-Json
date: 2024-12-03
author: Your Name
cell_count: 6
score: 5
---

---
title: "XML to JSON"
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
xml_content = """
     <note>
       <to>Tove</to>
       <from>Jani</from>
       <heading>Reminder</heading>
       <body>Don't forget me this weekend!</body>
   </note>
"""
```


```python
xml_content
```




    "\n     <note>\n       <to>Tove</to>\n       <from>Jani</from>\n       <heading>Reminder</heading>\n       <body>Don't forget me this weekend!</body>\n   </note>\n"




```python
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.dumps(xml_content))
```

    ('"\\n     <note>\\n       <to>Tove</to>\\n       <from>Jani</from>\\n       '
     "<heading>Reminder</heading>\\n       <body>Don't forget me this "
     'weekend!</body>\\n   </note>\\n"')



```python

```


---
**Score: 5**