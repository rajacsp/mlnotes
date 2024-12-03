---
title: Date-Util
date: 2024-12-04
author: Your Name
cell_count: 15
score: 15
---

---
title: "Date Util"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import datetime
```


```python
now = datetime.datetime.now()
```


```python
print(now.year)
```

    2019



```python
print (now.strftime("%y"))
```

    19



```python
print (now.strftime("%d"))
```

    21



```python
print (now.strftime("%m"))
```

    04



```python
print(datetime.datetime.today())
```

    2019-04-21 18:34:57.280555



```python
cur_date = datetime.date.today()
current_year = cur_date.year # Extract current year only
current_month = cur_date.month # Extract current month only
current_day = cur_date.day # Extract current day only
```


```python
print(cur_date)
```

    2019-04-21



```python
print(current_month)
```

    4



```python
print(current_day)
```

    21



```python
current_date = cur_date.strftime("%d-%m-%Y")
print(current_date)
```

    21-04-2019



```python
current_date = cur_date.strftime("%d-%B-%Y")
print(current_date)
```

    21-April-2019



```python

```


---
**Score: 15**