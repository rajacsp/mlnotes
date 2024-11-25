---
title: Read-Json-Csv
date: 2024-11-25
author: Your Name
cell_count: 4
score: 0
---

---
title: "Read JSON Online"
author: "Rj"
date: 2019-04-20
description: "List Test"
type: technical_note
draft: false
---

```python
import urllib.request, json 
```


```python
with urllib.request.urlopen("https://gitlab.com/rajacsp/datasets/raw/master/trump.json") as url:
    data = json.loads(url.read().decode())
    print(data['tweets'][0])
```

    {'source': 'Twitter for iPhone', 'id_str': '947824196909961216', 'text': 'Will be leaving Florida for Washington (D.C.) today at 4:00 P.M. Much work to be done, but it will be a great New Year!', 'created_at': 'Mon Jan 01 13:37:52 +0000 2018', 'retweet_count': 8656, 'in_reply_to_user_id_str': None, 'favorite_count': 54056, 'is_retweet': False}



```python

```


---
**Score: 0**