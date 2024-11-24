---
title: Read-Text-File-Online
date: 2024-11-24
author: Your Name
cell_count: 5
score: 5
---

---
title: "Read Text File Online"
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
data = None
with urllib.request.urlopen("https://gitlab.com/rajacsp/datasets/raw/master/gandhi.txt") as url:
    data = url.read().decode()
```


```python
data
```




    'Mahatma Gandhi has been variously described as an anti-colonial protester, a religious thinker, a pragmatist, a radical who used non-violence effectively to fight for causes, a canny politician and a whimsical Hindu patriarch.\n\nBut was India\'s greatest leader also a racist?\n\nThe authors of a controversial new book on Gandhi\'s life and work in South Africa certainly believe so. South African academics Ashwin Desai and Goolam Vahed spent seven years exploring the complex story of a man who lived in their country for more than two decades - 1893 to 1914 - and campaigned for the rights of Indian people there.\n\nIn The South African Gandhi: Stretcher-Bearer of Empire, Desai and Vahed write that during his stay in Africa, Gandhi kept the Indian struggle "separate from that of Africans and coloureds even though the latter were also denied political rights on the basis of colour and could also lay claim to being British subjects".\n\nThey write that Gandhi\'s political strategies - fighting to repeal unjust laws or freedom of movement or trade - carved out an exclusivist Indian identity "that relied on him taking up \'Indian\' issues in ways that cut Indians off from Africans, while his attitudes paralleled those of whites in the early years". Gandhi, the authors write, was indifferent to the plight of the indentured, and believed that state power should remain in white hands, and called black Africans Kaffirs, a derogatory term, for a larger part of his stay in the country.\n\nRacial segregation\nIn 1893, Gandhi wrote to the Natal parliament saying that a "general belief seems to prevail in the Colony that the Indians are a little better, if at all, than savages or the Natives of Africa".\n\nIn 1904, he wrote to a health officer in Johannesburg that the council "must withdraw Kaffirs" from an unsanitary slum called the "Coolie Location" where a large number of Africans lived alongside Indians. "About the mixing of the Kaffirs with the Indians, I must confess I feel most strongly."\n\nThe same year he wrote that unlike the African, the Indian had no "war-dances, nor does he drink Kaffir beer". When Durban was hit by a plague in 1905, Gandhi wrote that the problem would persist as long as Indians and Africans were being "herded together indiscriminately at the hospital".\n\nThis, in itself, say historians, is not entirely new and revelatory. Also, some South Africans have always accused the man who led India to independence of working with the British colonial government to promote racial segregation. In April, a man was arrested in connection with vandalising a statue of Gandhi. A hashtag #Ghandimustfall (sic) has gained circulation on social media.\n\nGandhi\'s biographer and grandson, Rajmohan Gandhi, says the younger Gandhi - he arrived in South Africa as a 24-year-old briefless lawyer - was undoubtedly "at times ignorant and prejudiced about South Africa\'s blacks". He believes Gandhi\'s "struggle for Indian rights in South Africa paved the way for the struggle of black rights". He argues that "Gandhi too was an imperfect human being", but the "imperfect Gandhi was more radical and progressive than most contemporary compatriots".\n\nRamachandra Guha, writer of the magisterial Gandhi Before India, writes that "to speak of comprehensive equality for coloured people was premature in early 20th Century South Africa". Attacking Gandhi for racism, wrote another commentator, "takes a simplistic view of a complex life".\n\nThe authors of the new book disagree.\n\n"Gandhi believed in the Aryan brotherhood. This involved whites and Indians higher up than Africans on the civilised scale. To that extent he was a racist. To the extent that he wrote Africans out of history or was keen to join with whites in their subjugation he was a racist," Ashwin Desai told me.\n\n"To the extent that he accepted white minority power but was keen to be a junior partner, he was a racist. Thank God he did not succeed in this as we would have been culpable in the horrors of apartheid.\n\n"But if Gandhi was part of the racist common sense of the time then how does this qualify him to be a person that is seen as part of the pantheon of South African liberation heroes? You cannot have Gandhi as an accomplice of colonial subjugation in South Africa and then also defend his liberation credentials in South Africa."\n\n\'Blind eye\'\nDesai also rejects the assertion that Gandhi paved the way for the local struggle for black rights - "in one sentence," he says, "you are writing out the history of African resistance to colonialism that unfolded much before Gandhi even arrived".\n\nIn his book, Guha writes what a friend in Cape Town once told him about Gandhi. "You gave us a lawyer, we gave you back a Mahatma [Great Soul]". Ashwin Desai thinks this is a "ridiculous assertion" about a man who "supported more taxes on impoverished African people and turned a blind eye to the brutality of the Empire on Africans".\n\nThe authors of the new book are not the first to challenge the conventional Indian historiography on Gandhi. Historian Patrick French wrote tellingly in 2013 that "Gandhi\'s blanking of Africans is the black hole at the heart of his saintly mythology".\n\nMore than a century after he left Africa, there has been a resurrection of Gandhi in South Africa. Despite their reservations about the \'man of Empire\', Desai and Vahed acknowledge that Gandhi "did raise universal demands for equality and dignity".\n\nBut even the greatest men are flawed. And Gandhi was possibly no exception.\n\nsource: https://www.bbc.com/news/world-asia-india-34265882'




```python

```


---
**Score: 5**