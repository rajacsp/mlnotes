---
title: Basic-Table
date: 2024-11-17
author: Your Name
cell_count: 21
score: 20
---

```python
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
```


```python
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
```

    /tmp/ipykernel_4126507/3500228846.py:2: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
      Base = declarative_base()



```python
engine
```




    Engine(sqlite:///:memory:)




```python
class City(Base):
     __tablename__ = 'city'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     province = Column(String)
     country = Column(String)

     def __repr__(self):
        return "<City(name='%s', province='%s', country='%s')>" % (
                             self.name, self.province, self.country)
```


```python
City.__table__ 
```




    Table('city', MetaData(), Column('id', Integer(), table=<city>, primary_key=True, nullable=False), Column('name', String(), table=<city>), Column('province', String(), table=<city>), Column('country', String(), table=<city>), schema=None)




```python
Base.metadata.create_all(engine)
```

    2024-11-16 13:50:11,009 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2024-11-16 13:50:11,010 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("city")
    2024-11-16 13:50:11,011 INFO sqlalchemy.engine.Engine [raw sql] ()
    2024-11-16 13:50:11,011 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("city")
    2024-11-16 13:50:11,012 INFO sqlalchemy.engine.Engine [raw sql] ()
    2024-11-16 13:50:11,013 INFO sqlalchemy.engine.Engine 
    CREATE TABLE city (
    	id INTEGER NOT NULL, 
    	name VARCHAR, 
    	province VARCHAR, 
    	country VARCHAR, 
    	PRIMARY KEY (id)
    )
    
    
    2024-11-16 13:50:11,013 INFO sqlalchemy.engine.Engine [no key 0.00045s] ()
    2024-11-16 13:50:11,014 INFO sqlalchemy.engine.Engine COMMIT



```python
toronto = City(name='Toronto', province='Ontario', country='Canada')
```


```python
# Create a session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
```


```python
session = Session()
```


```python
session.add(toronto)
```


```python
cities = session.query(City).all() 
```

    2024-11-16 13:50:32,379 INFO sqlalchemy.engine.Engine BEGIN (implicit)
    2024-11-16 13:50:32,382 INFO sqlalchemy.engine.Engine INSERT INTO city (name, province, country) VALUES (?, ?, ?)
    2024-11-16 13:50:32,383 INFO sqlalchemy.engine.Engine [generated in 0.00058s] ('Toronto', 'Ontario', 'Canada')
    2024-11-16 13:50:32,385 INFO sqlalchemy.engine.Engine SELECT city.id AS city_id, city.name AS city_name, city.province AS city_province, city.country AS city_country 
    FROM city
    2024-11-16 13:50:32,386 INFO sqlalchemy.engine.Engine [generated in 0.00042s] ()



```python
cities
```




    [<City(name='Toronto', province='Ontario', country='Canada')>]




```python
montreal = City(name='Montreal', province='Quebec', country='Canada')
```


```python
session.add(montreal)
```


```python
cities
```




    [<City(name='Toronto', province='Ontario', country='Canada')>]




```python
for city in cities:
    print(city)
```

    <City(name='Toronto', province='Ontario', country='Canada')>



```python
for city in cities:
    print(city.name)
```

    Toronto



```python
session.add_all([
    City(name='Waterloo', province='Ontario', country='Canada'),
    City(name='Kitchener', province='Ontario', country='Canada'),
    City(name='Quebec City', province='Quebec', country='Canada')
])
```


```python
cities = session.query(City).all() 
```

    2024-11-16 13:51:04,339 INFO sqlalchemy.engine.Engine INSERT INTO city (name, province, country) VALUES (?, ?, ?) RETURNING id
    2024-11-16 13:51:04,341 INFO sqlalchemy.engine.Engine [generated in 0.00023s (insertmanyvalues) 1/4 (ordered; batch not supported)] ('Montreal', 'Quebec', 'Canada')
    2024-11-16 13:51:04,341 INFO sqlalchemy.engine.Engine INSERT INTO city (name, province, country) VALUES (?, ?, ?) RETURNING id
    2024-11-16 13:51:04,342 INFO sqlalchemy.engine.Engine [insertmanyvalues 2/4 (ordered; batch not supported)] ('Waterloo', 'Ontario', 'Canada')
    2024-11-16 13:51:04,343 INFO sqlalchemy.engine.Engine INSERT INTO city (name, province, country) VALUES (?, ?, ?) RETURNING id
    2024-11-16 13:51:04,343 INFO sqlalchemy.engine.Engine [insertmanyvalues 3/4 (ordered; batch not supported)] ('Kitchener', 'Ontario', 'Canada')
    2024-11-16 13:51:04,344 INFO sqlalchemy.engine.Engine INSERT INTO city (name, province, country) VALUES (?, ?, ?) RETURNING id
    2024-11-16 13:51:04,344 INFO sqlalchemy.engine.Engine [insertmanyvalues 4/4 (ordered; batch not supported)] ('Quebec City', 'Quebec', 'Canada')
    2024-11-16 13:51:04,345 INFO sqlalchemy.engine.Engine SELECT city.id AS city_id, city.name AS city_name, city.province AS city_province, city.country AS city_country 
    FROM city
    2024-11-16 13:51:04,346 INFO sqlalchemy.engine.Engine [cached since 31.96s ago] ()



```python
for city in cities:
    print(city.name, city.province)
```

    Toronto Ontario
    Montreal Quebec
    Waterloo Ontario
    Kitchener Ontario
    Quebec City Quebec



```python

```


---
**Score: 20**
