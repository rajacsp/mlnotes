---
title: Wav-2-Txt
date: 2024-12-13
author: Your Name
cell_count: 5
score: 5
---

---
title: "Wav 2 Text"
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
'''
How to install ffmpeg:
brew tap varenc/ffmpeg
brew tap-pin varenc/ffmpeg
brew install ffmpeg $(brew options ffmpeg --compact)
    https://gist.github.com/clayton/6196167
'''
```




    '\nHow to install ffmpeg:\nbrew tap varenc/ffmpeg\nbrew tap-pin varenc/ffmpeg\nbrew install ffmpeg $(brew options ffmpeg --compact)\n    https://gist.github.com/clayton/6196167\n'




```python
# transcribe audio file                                                         
AUDIO_FILE = "/tmp/one.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file                  

print("Transcription: " + r.recognize_google(audio))
```

    Transcription: a pencil with black LED rights best coax a young calf to drink from a bucket schools for ladies teach charm and Grace the lamp Shone with a steady green flame they took the ax and the saw to the forest the ancient coin was quite a doll and warn the shaky Barn fell with a loud crash Jazz and swing fans like fast music rates the rubbish up and then let rake the rubbish up and then burn it stashed the gold cloth into fine ribbon the gold cloth into fine ribbons



```python

```


---
**Score: 5**