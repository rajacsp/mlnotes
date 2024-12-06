---
title: Query-By-Name
date: 2024-12-06
author: Your Name
cell_count: 9
score: 5
---

---
title: "Query By Name"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
```


```python
Base = declarative_base()
```


```python
class City(Base):
    __tablename__ = 'city'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    province = Column(String(50), nullable=True)
    country = Column(String(50), nullable=True)
```


```python
engine = create_engine('sqlite:///city.db')
Base.metadata.bind = engine

DBSession = sessionmaker()

DBSession.bind = engine

session = DBSession()
```


```python
city = session.query(City).filter(City.name == 'Toronto').first()
```


```python
city
```




    <__main__.City at 0x105433be0>




```python
city.name
```




    'Toronto'




```python

```


---
**Score: 5**