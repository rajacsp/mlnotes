---
title: List-Files
date: 2024-12-05
author: Your Name
cell_count: 4
score: 0
---

---
title: "List Files"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
from os import listdir
from os.path import isfile, join
```


```python
def list_files(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    for x in onlyfiles:
        print(x)
```


```python
list_files('/tmp/datasets')
```

    credit.zip
    occupancy.zip
    concrete.zip
    energy.zip
    spam.zip
    game.zip
    hobbies.zip
    bikeshare.zip
    mushroom.zip



---
**Score: 0**