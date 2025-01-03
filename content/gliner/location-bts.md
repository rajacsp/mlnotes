---
title: Location-Bts
date: 2025-01-03
author: Your Name
cell_count: 8
score: 5
---

```python
from gliner import GLiNER
```


```python
# https://genius.com/Genius-english-translations-bts-on-english-translation-lyrics
```


```python
# Initialize GLiNER with a pre-trained model
model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")  # Adjust to a location-specific model if needed
```


    Fetching 5 files:   0%|          | 0/5 [00:00<?, ?it/s]


    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/transformers/convert_slow_tokenizer.py:562: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
      warnings.warn(



```python
# Input text
text = """
[Verse 1: Jimin, V]
I can't understand what people are sayin'
Who and what do I need to follow
With each step then again grows the shadow
Where is this place I open my eyes to
Maybe Seoul or New York or Paris
I get up, unsteady on my feet (Yeah)

[Verse 2: RM]
(Look) Look at my feet, look down
The shadow resembles me
Is it the shadow that's shaking
Or is it my feet that are trembling
Of course I'm not unafraid
Of course it's not all okay
But I know
Awkwardly I flow
I fly together with that black wind

[Pre-Chorus: Jimin, Jung Kook, Jin]
(Hey, na-na-na) Gotta go insane to stay sane
(Hey, na-na-na) Throw myself whole into both worlds
(Hey, na-na-na) Can't hold me down 'cause you know I'm a fighter
Carried myself into this beautiful prison
Find me and I'm gonna live with ya

[Chorus: Jung Kook & Jimin, Jung Kook, Jimin]
(Eh-oh) Bring it, bring the pain, oh yeah
(Eh-oh) Come on up, bring the pain, oh yeah
Rain be pourin', sky keep fallin'
Everyday, oh na-na-na
(Eh-oh) Bring it, bring the pain, oh yeah

[Verse 3: j-hope]
Bring the pain
It'll become my blood and flesh
Bring the pain
No fear, now that I know the way
Breathe on the small things
My air and my light in the dark
The power of the things that make me, "me"
Even if I fall, I come right up, scream

[Verse 4: SUGA]
Even if I fall, I come right up, scream
That's how we've always been
Even if my knees drop to the ground
As long as they don't get buried
It's going to be just an ordinary happening
Win no matter what
Win no matter what
Win no matter what
Whatever you say, whatever they say
I don't give a uhh
I don't give a uhh
I don't give a uhh, yeah

[Pre-Chorus: Jimin, V, Jung Kook]
(Hey, na-na-na) Gotta go insane to stay sane
(Hey, na-na-na) Throw myself whole into both worlds
(Hey, na-na-na) Can't hold me down 'cause you know I'm a fighter
Carried myself into this beautiful prison
Find me and I'm gonna live with ya
"""
```


```python
# Define the entity label for location extraction
labels = ["LOCATION"]
```


```python
# Perform entity prediction
locations = model.predict_entities(text, labels, threshold=0.5)
```

    /home/rajaraman/miniconda3/envs/ml312/lib/python3.12/site-packages/gliner/data_processing/processor.py:269: UserWarning: Sentence of length 484 has been truncated to 384
      warnings.warn(f"Sentence of length {len(tokens)} has been truncated to {max_len}")
    Asking to truncate to max_length but no maximum length is provided and the model has no predefined maximum length. Default to no truncation.



```python
# Display the extracted locations
print("Extracted Locations:")
for loc in locations:
    print(f"{loc['text']} => {loc['label']}")
```

    Extracted Locations:
    Seoul => LOCATION
    New York => LOCATION
    Paris => LOCATION



```python

```


---
**Score: 5**