---
title: Simple Query
date: 2024-12-04
author: Your Name
cell_count: 15
score: 15
---

---
title: "Simple Query"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///city.db')
```


```python
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
```


```python
DBSession = sessionmaker(bind=engine)
session = DBSession()
```


```python
# Insert a City in the person table
to = City(name='Toronto', province='Ontario', country = 'Canada')
session.add(to)
session.commit()
```


```python
# Make a query to find all Cities in the database
cities = session.query(City).all()
```


```python
cities
```




    [<__main__.City at 0x112cfe278>,
     <__main__.City at 0x112cfe2e8>,
     <__main__.City at 0x112cfe358>,
     <__main__.City at 0x112cfe3c8>,
     <__main__.City at 0x112cbd588>]




```python
for city in cities:
    print(city.id, city.name)
```

    1 Toronto
    2 Montreal
    3 Waterloo
    4 Kitchener
    5 Toronto



```python
session.add_all([
    City(name='Montreal', province='Quebec', country = 'Canada'),
    City(name='Waterloo', province='Ontario', country = 'Canada'),
    City(name='Kitchener', province='Ontario', country = 'Canada')
])
session.commit()
```


```python
cities = session.query(City).all()
```


```python
for city in cities:
    print(city.id, city.name)
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
for city in session.query(City).all():
    print(city.id, city.name)
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

```


---
**Score: 15**