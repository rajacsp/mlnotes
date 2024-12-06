---
title: Prettify-Xml
date: 2024-12-06
author: Your Name
cell_count: 6
score: 5
---

---
title: "Prettify XML"
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

import xml.dom.minidom
```


```python
dom = xml.dom.minidom.parse('sample.xml') # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = dom.toprettyxml()
```


```python
pretty_xml_as_string
```




    '<?xml version="1.0" ?>\n<note>\n\t\n       \n\t<to>Tove</to>\n\t\n       \n\t<from>Jani</from>\n\t\n       \n\t<heading>Reminder</heading>\n\t\n       \n\t<body>Don\'t forget me this weekend!</body>\n\t\n   \n</note>\n'




```python
dom
```




    <xml.dom.minidom.Document at 0x105ef7588>




```python

```


---
**Score: 5**