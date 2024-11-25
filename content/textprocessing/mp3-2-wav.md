---
title: Mp3-2-Wav
date: 2024-11-25
author: Your Name
cell_count: 4
score: 0
---

---
title: "mp3 2 wav"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
import speech_recognition as sr
from os import path
from pydub import AudioSegment
```


```python
# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("/tmp/two.mp3")
sound.export("/tmp/two.wav", format="wav")

print('Done')
```

    Done



```python

```


---
**Score: 0**