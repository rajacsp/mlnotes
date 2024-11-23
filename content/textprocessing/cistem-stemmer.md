```python
from nltk.stem.cistem import Cistem
```


```python
c_stemmer = Cistem()
```


```python
c_stemmer.stem("filtering")
```




    'filtering'




```python
c_stemmer.segment("filtering")
```




    ('filtering', '')




```python
c_stemmer.segment("Ausgefeiltere")
```




    ('ausgefeilt', 'ere')



segment method will return both the stem and the rest that was removed at the end
