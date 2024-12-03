---
title: Pretty Print Json
date: 2024-12-03
author: Your Name
cell_count: 7
score: 5
---

---
title: "Pretty Print Json"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import json
import pprint
```


```python
content = """{"system": {"commit": None, "python": "3.6.8.final.0", "python-bits": 64, "OS": "Darwin", "OS-release": "18.5.0", "machine": "x86_64", "processor": "i386", "byteorder": "little", "LC_ALL": "None", "LANG": "en_CA.UTF-8", "LOCALE": "en_CA.UTF-8"}, "dependencies": {"pandas": "0.24.2", "pytest": "4.5.0", "pip": "19.0.3", "setuptools": "40.8.0", "Cython": None, "numpy": "1.16.3", "scipy": "1.2.1", "pyarrow": None, "xarray": "0.12.1", "IPython": "6.2.1", "sphinx": None, "patsy": "0.5.1", "dateutil": "2.8.0", "pytz": "2019.1", "blosc": None, "bottleneck": None, "tables": None, "numexpr": None, "feather": None, "matplotlib": "3.0.3", "openpyxl": None, "xlrd": None, "xlwt": None, "xlsxwriter": None, "lxml.etree": "4.3.3", "bs4": "4.7.1", "html5lib": "1.0b10", "sqlalchemy": "1.3.3", "pymysql": None, "psycopg2": "2.8.2 (dt dec pq3 ext lo64)", "jinja2": "2.10.1", "s3fs": None, "fastparquet": None, "pandas_gbq": None, "pandas_datareader": "0.7.0", "gcsfs": None}}"""
```


```python
content
```




    '{"system": {"commit": None, "python": "3.6.8.final.0", "python-bits": 64, "OS": "Darwin", "OS-release": "18.5.0", "machine": "x86_64", "processor": "i386", "byteorder": "little", "LC_ALL": "None", "LANG": "en_CA.UTF-8", "LOCALE": "en_CA.UTF-8"}, "dependencies": {"pandas": "0.24.2", "pytest": "4.5.0", "pip": "19.0.3", "setuptools": "40.8.0", "Cython": None, "numpy": "1.16.3", "scipy": "1.2.1", "pyarrow": None, "xarray": "0.12.1", "IPython": "6.2.1", "sphinx": None, "patsy": "0.5.1", "dateutil": "2.8.0", "pytz": "2019.1", "blosc": None, "bottleneck": None, "tables": None, "numexpr": None, "feather": None, "matplotlib": "3.0.3", "openpyxl": None, "xlrd": None, "xlwt": None, "xlsxwriter": None, "lxml.etree": "4.3.3", "bs4": "4.7.1", "html5lib": "1.0b10", "sqlalchemy": "1.3.3", "pymysql": None, "psycopg2": "2.8.2 (dt dec pq3 ext lo64)", "jinja2": "2.10.1", "s3fs": None, "fastparquet": None, "pandas_gbq": None, "pandas_datareader": "0.7.0", "gcsfs": None}}'




```python
json_data = json.loads(content)
```


    ---------------------------------------------------------------------------

    JSONDecodeError                           Traceback (most recent call last)

    <ipython-input-10-c81e5ee0b888> in <module>()
    ----> 1 json_data = json.loads(content)
    

    ~/anaconda3/envs/py36/lib/python3.6/json/__init__.py in loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)
        352             parse_int is None and parse_float is None and
        353             parse_constant is None and object_pairs_hook is None and not kw):
    --> 354         return _default_decoder.decode(s)
        355     if cls is None:
        356         cls = JSONDecoder


    ~/anaconda3/envs/py36/lib/python3.6/json/decoder.py in decode(self, s, _w)
        337 
        338         """
    --> 339         obj, end = self.raw_decode(s, idx=_w(s, 0).end())
        340         end = _w(s, end).end()
        341         if end != len(s):


    ~/anaconda3/envs/py36/lib/python3.6/json/decoder.py in raw_decode(self, s, idx)
        355             obj, end = self.scan_once(s, idx)
        356         except StopIteration as err:
    --> 357             raise JSONDecodeError("Expecting value", s, err.value) from None
        358         return obj, end


    JSONDecodeError: Expecting value: line 1 column 23 (char 22)


(Jeez, I did something wrong here. Let me revisit this page and fix it for you)


```python

```


---
**Score: 5**