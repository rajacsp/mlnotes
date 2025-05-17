---
title: Filter-Like
date: 2025-05-17
author: Your Name
cell_count: 13
score: 10
---

---
title: "Filter Like"
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
for c in session.query(City).\
          filter(City.name.like('%to%')):
        print(c.id, c.name)
```

    1 Toronto
    5 Toronto



```python
for c in session.query(City).\
          filter(City.name.like('%o%')):
        print(c.id, c.name)
```

    1 Toronto
    2 Montreal
    3 Waterloo
    5 Toronto
    6 Montreal
    7 Waterloo



```python
for c in session.query(City).\
          filter(City.name.like('%t%')):
        print(c.id, c.name)
```

    1 Toronto
    2 Montreal
    3 Waterloo
    4 Kitchener
    5 Toronto
    6 Montreal
    7 Waterloo
    8 Kitchener



```python
for c in session.query(City).\
          filter(City.name.like('%o')):
        print(c.id, c.name)
```

    1 Toronto
    3 Waterloo
    5 Toronto
    7 Waterloo



```python
# Get only one column
for c in session.query(City.name).\
          filter(City.name.like('%o')):
        print(c.name)
```

    Toronto
    Waterloo
    Toronto
    Waterloo



```python
# Get only two columns
for c in session.query(City.name, City.province).\
          filter(City.name.like('%o')):
        print(c.name, c.province)
```

    Toronto Ontario
    Waterloo Ontario
    Toronto Ontario
    Waterloo Ontario



```python
# Get only two columns
for name, state in session.query(City.name, City.province).\
          filter(City.name.like('%o')):
        print(state, name)
```

    Ontario Toronto
    Ontario Waterloo
    Ontario Toronto
    Ontario Waterloo



```python

```


---
**Score: 10**