---
title: Lexical-Diversity
date: 2024-12-25
author: Your Name
cell_count: 10
score: 10
---

---
title: "Lexical Diversity"
author: "Rj"
date: 2019-04-21
description: "-"
type: technical_note
draft: false
---

```python
import nltk
```


```python
f =open('canola.txt','r')
raw = f.read()
```


```python
raw
```




    'OTTAWA—The federal Liberals promised Wednesday to give Canada’s canola farmers much-needed financial aid to help lessen the impact of China’s decision to ban the product as part of a trade dispute with no immediate end in sight.\n\nThe changes made to a special agricultural program will raise loan limits to $1 million from $400,000, and the portion that will be interest-free is rising to $500,000 from $100,000 for canola producers.\n\nOTTAWA—The federal Liberals promised Wednesday to give Canada’s canola farmers much-needed financial aid to help lessen the impact of China’s decision to ban the product as part of a trade dispute with no immediate end in sight.\n\nThe changes made to a special agricultural program will raise loan limits to $1 million from $400,000, and the portion that will be interest-free is rising to $500,000 from $100,000 for canola producers.\n\n“We stand shoulder-to-shoulder with Canada’s canola producers and farm families across the country and we will continue to listen to their needs,” Agriculture Minister Marie-Claude Bibeau said on Parliament Hill Wednesday morning.\n\n“Canada has the best canola in the world as well as a very robust inspection system.”\n\nInternational Trade Diversification Minister Jim Carr said he will lead a canola trade mission to Japan and South Korea in early June to help farmers find new markets for their products.\n\nHe also said he will be promoting canola in all of his upcoming visits, including in France.\n\n“It is critical that Canadian exporters have other readily available markets when faced with trade disruptions,” he said.\n\n“Our country’s continued prosperity and job creation depends on security markets abroad.”\n\nConservative foreign affairs critic Erin O’Toole called Wednesday’s announcement positive, adding it is a step his party has long called for. But he warned it is a stop-gap measure that does not address the underlying diplomatic tensions.\n\n“The Trudeau government has allowed our diplomatic situation with China to descend into chaos, where we are not sure what commodity could be at risk next,” O’Toole said while standing outside the House of Commons.\n\nConservative Leader Andrew Scheer has previously called for the federal government to take a more confrontational approach with China, including launching a complaint with the World Trade Organization and cut Canadian funding to China’s Asian Infrastructure Investment Bank, to which the government has committed $256 million over five years.\n\nScheer has also pressed the Liberals to appoint a new ambassador to China. On his way into the weekly caucus meeting, Prime Minister Justin Trudeau said the government has a strong, career diplomat who is handling “the particulars of this very well.”\n\nCarr told reporters there is agreement across the sector, including with provincial governments and producers, that Canada should engage China on the basis of their allegation — that there are impurities in the canola inspected twice by the Canadian Food Inspection Agency. Canada will navigate this challenging period with China through careful, deliberate and strategic engagement, he said.\n\nSaskatchewan Premier Scott Moe said Wednesday’s announcement buys “some breathing space” for nervous farmers and suggested China will ultimately relent because it needs canola.\n\n“We just need to ensure that we have the relationship that we are actually able to trade that commerce and we are going to support our federal government in those conversations moving forward,” he said.\n\nChina’s refusal thus far to accept a Canadian delegation to work out a solution to an ongoing canola seed trade dispute that’s left farmers and exporters scrambling calls for more urgent action from Ottawa, says an industry group.\n\nThe Canola Council of Canada wants the federal government to “consider all available options” as weeks have passed since China suspended the licences of two major exporters of canola seed, citing concerns about pests, and Chinese companies stopped buying the product from Canadian producers.\n\n\nWinnipeg-based Richardson International Ltd.’s permit to export canola was revoked in early March, while Regina-based Viterra Inc.’s shipments were blocked later that month.\n\nThe government has said it wants to send a delegation to China to find a scientific solution to the dispute. Agriculture minister Marie-Claude Bibeau said earlier this month she sent a letter to her Chinese counterpart with that request.\n\nHowever, despite that letter being sent more than two weeks ago, the canola council has not been informed during its regular conversation with government if that request has been accepted, said Brian Innes, vice-president of public affairs for the Canola Council of Canada.\n\n“Time has ticked on without this meeting happening and that is costing the industry and growers significantly,” he said.\n\nThe group wants both governments to intensify efforts to make the meeting happen as quickly as possible, said Innes.\n\nIt recommends Canada appoint an ambassador to China as soon as possible. It wants the government to review diplomatic, technical and legal tools to engage Chinese officials in resuming trade.\n\nLastly, it wants support for producers, including helping growers pay their bills by expanding the advanced payments program, said Innes. The program provides farmers with credit, he explained.\n\nThe seed dispute comes after Canadian authorities arrested Chinese tech executive, Meng Wanzhou, in Vancouver in December at the behest of the U.S.\n\n\nChina’s been a major market for Canadian canola and accounts for about 40 per cent of all seed, oil and meal exports, according to the council. In 2018, canola seed exports to China were worth $2.7 billion, the council said, with very strong demand until recent disruptions.\n'




```python
tokens = nltk.word_tokenize(raw.lower())
text = nltk.Text(tokens)
```


```python
def get_lexical_diversity(content):
    return len(content)/len(set(content))
```


```python
def get_percentage(content, word):
    return 100 * content.count(word)/len(content)
```


```python
print(get_lexical_diversity(text))
```

    2.49636803874092



```python
print(get_percentage(text, 'canola'))
```

    1.7458777885548011



```python

```


---
**Score: 10**