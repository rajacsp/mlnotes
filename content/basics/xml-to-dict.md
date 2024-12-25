---
title: Xml-To-Dict
date: 2024-12-25
author: Your Name
cell_count: 10
score: 10
---

---
title: "XML to Dictionary"
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
pp.pprint(json.dumps(xmltodict.parse(xml_content)))
```

    ('{"note": {"to": "Tove", "from": "Jani", "heading": "Reminder", "body": '
     '"Don\'t forget me this weekend!"}}')



```python
dict = xmltodict.parse(xml_content)
```


```python
dict
```




    OrderedDict([('note',
                  OrderedDict([('to', 'Tove'),
                               ('from', 'Jani'),
                               ('heading', 'Reminder'),
                               ('body', "Don't forget me this weekend!")]))])




```python
dict['note']
```




    OrderedDict([('to', 'Tove'),
                 ('from', 'Jani'),
                 ('heading', 'Reminder'),
                 ('body', "Don't forget me this weekend!")])




```python
dict['note']['to']
```




    'Tove'




```python

```


---
**Score: 10**