---
title: Time With Periods
date: 2024-11-24
author: Your Name
cell_count: 5
score: 5
---

---
title: "Time With Periods"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import pandas as pd
```


```python
times = pd.date_range('2000-01-01', periods=4)

print(times)
```

    DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04'], dtype='datetime64[ns]', freq='D')



```python
for time in times:
    print(time)
```

    2000-01-01 00:00:00
    2000-01-02 00:00:00
    2000-01-03 00:00:00
    2000-01-04 00:00:00



```python

```


---
**Score: 5**