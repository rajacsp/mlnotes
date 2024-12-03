---
title: Streams
date: 2024-12-03
author: Your Name
cell_count: 13
score: 10
---

```python
from constants import OPENAI_API_KEY
```


```python
!pip show langchain-openai | grep "Version:"
```

    Version: 0.2.9



```python
import os
```


```python
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
```


```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
```


```python
chunks = []
for chunk in model.stream("what color is the sky?"):
    chunks.append(chunk)
    print(chunk.content, end="|", flush=True)
```

    |The| color| of| the| sky| can| vary| depending| on| several| factors|,| including| the| time| of| day|,| weather| conditions|,| and| atmospheric| particles|.| During| a| clear| day|,| the| sky| typically| appears| blue| due| to| Ray|leigh| scattering|,| which| causes| shorter| wavelengths| of| light| (|blue|)| to| be| scattered| more| than| longer| wavelengths| (|red|).| At| sunrise| and| sunset|,| the| sky| can| display| shades| of| orange|,| pink|,| and| red| as| the| sunlight| passes| through| more| of| the| Earth's| atmosphere|,| scattering| shorter| wavelengths| and| allowing| longer| wavelengths| to| dominate|.| On| cloudy| or| over|cast| days|,| the| sky| may| appear| gray|.| Additionally|,| pollution|,| dust|,| and| other| particles| can| affect| the| sky|'s| color| as| well|.||


```python
chunks
```




    [AIMessageChunk(content='', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content='The', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' color', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' of', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' the', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' sky', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' can', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' vary', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' depending', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' on', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' several', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' factors', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' including', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' the', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' time', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' of', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' day', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' weather', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' conditions', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' and', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' atmospheric', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' particles', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content='.', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' During', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' a', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' clear', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' day', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' the', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' sky', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' typically', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' appears', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' blue', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' due', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' to', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' Ray', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content='leigh', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' scattering', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' which', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' causes', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' shorter', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' wavelengths', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' of', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' light', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' (', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content='blue', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=')', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' to', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' be', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' scattered', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' more', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' than', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' longer', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' wavelengths', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' (', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content='red', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=').', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' At', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' sunrise', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' and', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' sunset', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' the', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' sky', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' can', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' display', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' shades', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' of', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' orange', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' pink', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' and', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' red', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' as', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' the', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' sunlight', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' passes', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' through', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' more', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' of', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' the', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=" Earth's", additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' atmosphere', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' scattering', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' shorter', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' wavelengths', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' and', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' allowing', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' longer', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' wavelengths', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' to', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' dominate', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content='.', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' On', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' cloudy', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' or', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' over', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content='cast', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' days', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' the', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' sky', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' may', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' appear', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' gray', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content='.', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' Additionally', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' pollution', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' dust', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=',', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' and', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' other', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' particles', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' can', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' affect', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' the', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' sky', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content="'s", additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' color', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' as', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content=' well', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content='.', additional_kwargs={}, response_metadata={}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14'),
     AIMessageChunk(content='', additional_kwargs={}, response_metadata={'finish_reason': 'stop', 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_0705bf87c0'}, id='run-a1aea264-40ed-44e7-a006-a568039dbc14')]




```python
ca_chunks = []
for chunk in model.stream("tell me about Canada"):
    ca_chunks.append(chunk)
    print(chunk.content, end="|", flush=True)
```

    |Canada| is| the| second|-largest| country| in| the| world| by| land| area|,| located| in| North| America|.| It| is| known| for| its| diverse| landscapes|,| multicultural| population|,| and| strong| economy|.| Here| are| some| key| aspects| of| Canada|:
    
    |###| Geography|
    |-| **|Size|**|:| Canada| covers| approximately| |9|.|98| million| square| kilometers| (|3|.|85| million| square| miles|).
    |-| **|Regions|**|:| It| consists| of| ten| provinces| and| three| territories|,| each| with| its| own| unique| geography| and| culture|.| Major| geographical| features| include| the| Rocky| Mountains|,| vast| forests|,| and| numerous| lakes| and| rivers|.
    |-| **|Natural| Wonders|**|:| Canada| is| home| to| natural| attractions| such| as| Niagara| Falls|,| Ban|ff| National| Park|,| and| the| Northern| Lights|.
    
    |###| Population|
    |-| **|D|iversity|**|:| Canada| is| known| for| its| multicultural| society|,| with| a| population| that| includes| a| wide| range| of| ethnic|ities| and| cultures|.| It| is| home| to| Indigenous| peoples| as| well| as| immigrants| from| around| the| world|.
    |-| **|Languages|**|:| The| two| official| languages| are| English| and| French|,| reflecting| the| country's| colonial| history| and| cultural| diversity|.
    
    |###| Government| and| Politics|
    |-| **|Political| System|**|:| Canada| is| a| parliamentary| democracy| and| a| constitutional| monarchy|,| with| the| British| monarch| as| the| head| of| state|.| The| government| is| led| by| the| Prime| Minister|.
    |-| **|Pro|vin|ces| and| Territories|**|:| The| country| is| divided| into| ten| provinces| (|e|.g|.,| Ontario|,| Quebec|,| British| Columbia|)| and| three| territories| (|Y|uk|on|,| Northwest| Territories|,| Nun|avut|),| each| with| its| own| government|.
    
    |###| Economy|
    |-| **|Resource| Rich|**|:| Canada| has| a| highly| developed| economy|,| rich| in| natural| resources| such| as| oil|,| gas|,| minerals|,| and| timber|.| It| is| one| of| the| largest| producers| of| natural| resources| in| the| world|.
    |-| **|Trade|**|:| Canada| has| strong| trade| relationships|,| particularly| with| the| United| States|,| and| is| a| member| of| organizations| like| the| United| Nations| and| the| North| American| Free| Trade| Agreement| (|NA|FTA|),| which| has| been| replaced| by| the| US|M|CA|.
    
    |###| Culture|
    |-| **|Arts| and| Entertainment|**|:| Canada| has| a| vibrant| cultural| scene|,| contributing| significantly| to| literature|,| music|,| film|,| and| the| arts|.| Not|able| Canadian| figures| include| authors| like| Margaret| At|wood| and| musicians| like| Leonard| Cohen| and| Drake|.
    |-| **|Sports|**|:| Ice| hockey| is| a| national| pastime|,| and| Canadian| teams| are| prominent| in| both| national| and| international| competitions|.
    
    |###| Education| and| Healthcare|
    |-| **|Education|**|:| Canada| boasts| a| high| standard| of| education|,| with| a| strong| emphasis| on| research| and| innovation|.| Its| universities| are| internationally| recognized|.
    |-| **|Healthcare|**|:| Canada| has| a| publicly| funded| healthcare| system|,| which| provides| access| to| medical| services| for| all| citizens| and| permanent| residents|.
    
    |###| Environment| and| Conservation|
    |-| **|Natural| Conservation|**|:| Canada| places| a| significant| emphasis| on| environmental| conservation| and| sustainability|,| with| many| national| parks| and| protected| areas|.
    
    |Overall|,| Canada| is| known| for| its| high| quality| of| life|,| stunning| natural| landscapes|,| and| welcoming| attitude| towards| newcomers|.| The| country| continues| to| evolve| and| adapt|,| maintaining| its| commitment| to| diversity| and| inclus|ivity|.||


```python
ca_chunks = []
for chunk in model.stream("tell me about Canada in 3 points"):
    ca_chunks.append(chunk)
    print(chunk.content, end="|", flush=True)
```

    |Sure|!| Here| are| three| key| points| about| Canada|:
    
    |1|.| **|D|iverse| Geography| and| Climate|**|:| Canada| is| the| second|-largest| country| in| the| world| by| land| area|,| featuring| a| wide| range| of| geographical| landscapes|,| from| the| Rocky| Mountains| in| the| west| to| the| vast| tund|ra| in| the| north| and| the| Atlantic| coastline| in| the| east|.| This| diversity| contributes| to| a| variety| of| climates|,| including| temper|ate| zones| in| the| south| and| polar| conditions| in| the| north|.
    
    |2|.| **|C|ultural| Mosaic|**|:| Canada| is| known| for| its| multicultural|ism| and| is| home| to| a| rich| tapestry| of| cultures|,| languages|,| and| traditions|.| The| country| officially| recognizes| both| English| and| French| as| its| official| languages|,| reflecting| its| colonial| history|.| Additionally|,| Indigenous| cultures| play| a| crucial| role| in| Canada's| identity|,| with| numerous| First| Nations|,| Mét|is|,| and| Inuit| communities| across| the| country|.
    
    |3|.| **|Strong| Economy| and| Social| Systems|**|:| Canada| has| a| highly| developed| economy|,| characterized| by| a| mix| of| natural| resources|,| manufacturing|,| and| technology| sectors|.| It| also| boasts| a| robust| social| welfare| system|,| including| universal| healthcare|,| which| is| funded| through| taxes| and| provides| citizens| and| permanent| residents| access| to| essential| medical| services| without| direct| charges| at| the| point| of| care|.||


```python

```


```python
chunks = []
async for chunk in model.astream("what color is the sky?"):
    chunks.append(chunk)
    print(chunk.content, end="|", flush=True)
```

    |The| sky| typically| appears| blue| during| the| day| due| to| the| scattering| of| sunlight| by| the| atmosphere|.| Short|er| blue| wavelengths| of| light| scatter| more| than| other| colors|,| making| the| sky| look| blue| to| our| eyes|.| However|,| the| sky| can| also| appear| in| other| colors| depending| on| the| time| of| day|,| weather| conditions|,| and| atmospheric| particles|.| For| example|,| it| can| appear| red| or| orange| during| sunrise| and| sunset|,| gray| during| over|cast| conditions|,| and| even| have| hues| of| pink| or| purple|.||


```python
chunks[0]
```




    AIMessageChunk(content='', additional_kwargs={}, response_metadata={}, id='run-fbee8efd-fccf-4989-bcd4-b8a5cc50bf68')




```python

```


---
**Score: 10**