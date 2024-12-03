---
title: Speech-2-Text
date: 2024-12-04
author: Your Name
cell_count: 4
score: 0
---

---
title: "Speech 2 Text"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
import speech_recognition as sr
```


```python
def startpy():
    
    # obtain audio from the microphone
    r = sr.Recognizer()
    d= ''
    while (d!='exit' and d!='quit'):
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
    
    # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            data = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        d = data
```


```python
#startpy()
```


---
**Score: 0**