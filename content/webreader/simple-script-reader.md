---
title: Simple-Script-Reader
date: 2025-05-17
author: Your Name
cell_count: 8
score: 5
---

---
title: "Simple Script Reader"
author: "Rj"
date: 2019-04-20
description: "-"
type: technical_note
draft: false
---

```python
import requests
from bs4 import BeautifulSoup
```


```python
# Collect and parse first page
page = requests.get('https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=two-and-a-half-men&episode=s01e01')
soup = BeautifulSoup(page.text, 'html.parser')  
```


```python
content = soup.select('div.scrolling-script-container')[0]

contents = content.children  
```


```python
lines = []
dcounter = 0
```


```python
for c in contents:

    dcounter += 1    

    #print(dcounter, c)
    if(c is None):
        continue

    #print(type(c))
    try:
        c = c.replace('<br/>', '')
        c = c.strip()
        lines.append(c)            
    except TypeError as e:
        #print('s error :')
        pass 
```


```python
counter = 0
for line in lines:
    print(counter, line)
    counter += 1
```

    0 - So, what do you think? - Wow.
    1 It's for you, right? It's for both of us.
    2 Don't go away.
    3 Don't worry.
    4 There's not enough blood left in my legs to go anywhere.
    5 Hey, it's Charlie.
    6 Do your thing when you hear the beep.
    7 Listen, you lousy S.
    8 O.
    9 B.
    10 , I will not be treated like this.
    11 Either you call me, or you are gonna be very, very sorry.
    12 I love you, Monkey Man.
    13 Charlie? Who was that? Damn telemarketers.
    14 A telemarketer who calls you Monkey Man? I'm on some weird list.
    15 Okay, it's a woman I went out with once and she got a little clingy.
    16 You are a bad, bad boy.
    17 And yet, you're always the one getting spanked.
    18 Jeez.
    19 Hey, it's Charlie.
    20 Do your thing when you hear the beep.
    21 Charlie, it's Alan.
    22 Your brother.
    23 No big deal, just wanted to touch base.
    24 My wife threw me out, and I'm kind of losing the will to live.
    25 So, when you get a chance, I'd really love to I don't know Alan, I'm sorry to hear about that.
    26 So, where you gonna go, to a hotel? Wow.
    27 Well, yeah, I guess you could stay here.
    28 Okay.
    29 I'll see you when you get here.
    30 We better hurry.
    31 Is she staying over? Because I may have parked behind her.
    32 Twelve years, and she just throws me out.
    33 I mean, what was the point of our wedding vows? You know, "Till death do us part.
    34 " Who died? Not me.
    35 Not her.
    36 How did you get in my house? Okay, Charlie, the key in the fake rock only works if it's among other rocks.
    37 Not sitting on your welcome mat.
    38 Excuse me, but if you put the fake rock in with a bunch of other rocks, it's impossible to find when you're drunk.
    39 You know, I'm a good husband.
    40 I'm faithful.
    41 - Is she? - Is she what? Faithful.
    42 Don't be ridiculous.
    43 Judith doesn't even like sex.
    44 I mean, all she kept saying was she feels suffocated, you know? She kept going on and on, "I'm suffocating.
    45 " What does that mean, you know? Has a woman ever said that to you? Well, yeah.
    46 But not a woman who doesn't like sex.
    47 And Jake.
    48 This could just destroy Jake.
    49 - Jake? - My son.
    50 Teenagers are pretty sophisticated these days.
    51 He's 10.
    52 - Charlie, I'm going to go.
    53 - No.
    54 You two need to talk.
    55 I'll call you tomorrow.
    56 I'm sorry to hear about you and your wife.
    57 Come on, you leaving isn't gonna bring them back together again.
    58 Look, okay, this is just until things settle out.
    59 A couple of days max.
    60 She will come to her senses.
    61 Yeah.
    62 That's what women do.
    63 Look, you can have the guest room.
    64 I'll grab some sheets.
    65 That's okay.
    66 I brought my own.
    67 You brought your own sheets? I like my sheets.
    68 - Okay, then, good night.
    69 - No, wait.
    70 I mean, we hardly ever talk to each other.
    71 What do you want to talk about, Alan? I don't know.
    72 I was named Chiropractor of the Year by the San Fernando Valley Chiropractic Association.
    73 - Okay, then.
    74 Good night.
    75 - No.
    76 Charlie, what about you? What's going on with you? Well, Alan, there's not much to say.
    77 I make a lot of money for doing very little work.
    78 I sleep with beautiful women who don't ask about my feelings.
    79 I drive a Jag, I live at the beach, and sometimes in the middle of the day, for no reason at all, I like to make myself a big pitcher of margaritas and take a nap out on the sundeck.
    80 - Okay, then.
    81 Good night, Charlie.
    82 - Good night.
    83 Good night, Monkey Man.
    84 Boy, is your eye red.
    85 You should see it from in here.
    86 What are you doing here, Jake? My mom brought me.
    87 Will you take me swimming in the ocean? Can we talk about it after my head stops exploding? Why is your head exploding? Well, I drank a little too much wine last night.
    88 If it makes you feel bad, why do you drink it? Nobody likes a wiseass, Jake.
    89 You have to put $1 in the swear jar.
    90 You said "ass.
    91 " Tell you what, here's $20.
    92 That should cover me till lunch.
    93 Now, what I think you need to do is to make a list.
    94 On one side, put what you don't like about our marriage, and on the other side, what you do.
    95 Alan, sometimes when I think about coming home to you, I start crying in my car.
    96 Okay, that would probably go on the "don't" side.
    97 Why would I lie? The ocean is closed today.
    98 For God's sake, do you think you could put some pants on? Look at me, Judy.
    99 I could barely make it down the stairs.
    100 Charlie, could you and Jake Yeah, come on, kid, we'll have breakfast out on the deck.
    101 I already had breakfast.
    102 - Okay, we'll have lunch.
    103 - It's not lunchtime.
    104 That's his head exploding.
    105 Judith, I can change.
    106 Please, Alan.
    107 You are the most rigid, inflexible, obsessive, anal-retentive man I've ever met.
    108 Rigid and inflexible? Don't you think that's a little redundant? My mom and dad are splitting up.
    109 Yeah.
    110 It looks that way.
    111 You're lucky.
    112 When I was your age, I could only dream about my parents splitting up.
    113 - Your mom is my grandma.
    114 - Yep.
    115 Grandma says you're a bitter disappointment.
    116 Hey, sport, your mom wants to say goodbye.
    117 Listen, he doesn't know anything about what's going on, so let's just keep this to ourselves.
    118 Our little secret.
    119 Why is she saying goodbye to him? She's gonna be spending the weekend with her sister in Vegas.
    120 So, we decided that Jake would stay with me.
    121 With you? Well, with us.
    122 I'm hungry.
    123 Is this gonna be a problem? I guess not.
    124 Thanks.
    125 Listen, I've got to call my office.
    126 Would you mind making him lunch? - Sure.
    127 - Thanks.
    128 What are you smiling about? You don't have any food.
    129 Yeah, but I'm not the one who's hungry.
    130 Who's smiling now, shorty? - You drink milk? - Just with cereal.
    131 - Okay.
    132 - Not that milk.
    133 That milk.
    134 - What's the difference? - That's Dairy Farm.
    135 We drink Dairy Barn.
    136 Fine.
    137 Happy? Why would I be happy? It's just milk.
    138 Cute.
    139 Keep it up, you'll be on one of the cartons.
    140 Okay, cereal.
    141 We got Lucky Charms, Cocoa Puffs, Frosted Flakes and Maple Loops.
    142 I want Maple Loops.
    143 You know who wrote that song? - Your uncle Charlie wrote that.
    144 - No lie? If I was to lie, I'd say I wrote Stairway to Heaven, not the Maple Loops song.
    145 - You two are really good together.
    146 - Thank you.
    147 So, does your wife sing, too? - No, I'm not married.
    148 - What a shame.
    149 Wow.
    150 You're even better than a dog.
    151 Dr.
    152 Bloom? Yes, this is Alan Harper.
    153 My wife and I need to cancel our marriage counseling appointment for this afternoon.
    154 Yes, well, something came up.
    155 Well, it's kind of personal.
    156 I mean Well, yeah, I know the point of these things is I've got to go.
    157 - Hello? - Is Charlie home? No.
    158 I'm Charlie's brother.
    159 Can I help you? Hi, Charlie's brother.
    160 I'm Rose.
    161 I'm Charlie's housekeeper.
    162 So, you're a housekeeper? Housekeeper /actress/hand model.
    163 I just do this to keep the wolf from the door.
    164 You know what I mean? Sure.
    165 Come on in.
    166 Yeah, I can smell him.
    167 Smell who? Your brother.
    168 He has a very musky scent.
    169 Well, I'll just let you get to work.
    170 Wait.
    171 No.
    172 It's okay.
    173 Jake, buddy.
    174 Take a break.
    175 What took you so long? We stopped for ice cream because I'm a babe magnet.
    176 I got to take a squirt.
    177 Why do you assume he learned that from me? Because I learned it from you.
    178 - Hey, thanks for cleaning up.
    179 - No, it wasn't me.
    180 Rose was here.
    181 Rose? You let Rose into my house? She said she was your maid.
    182 Hell, she glued the damn cabinets shut again.
    183 Again? You've got somebody who comes in regularly to glue your cabinets? You've met some of the whack jobs I've gone out with.
    184 - It's not that big a stretch.
    185 - So, this is my fault? Who let her in? You're a deeply disturbed man, you know? Move it.
    186 Come on.
    187 I'm deeply disturbed? Who came here in the middle of the night with his own sheets? At least, I care what I sleep on.
    188 Or should I say, who I sleep on.
    189 Hey, pal, of the two of us, I'll bet I'm the only one who's slept with a married woman recently.
    190 And isn't that something to brag about? Hi, Mom.
    191 Do you have any idea how hurtful it is to hear about your own son's divorce on the street? What divorce? What street? How did you get in my house? You stay out of this.
    192 I'm here to help your brother through a very difficult time.
    193 How could you do this to me? Do what? Now when I want to see my grandson I am going to have to make an appointment with Judith, who, let's face it, was never very warm to me.
    194 And what if there's another man there? Shacking up with her? Have we even stopped to consider that? I think he's considering it now, Mom.
    195 - Here's your iced tea, Grandma.
    196 - Thank you, my little angel.
    197 Darling, I asked for a lemon wedge.
    198 All right.
    199 Here's what you're going to do.
    200 You and Jake will come live with me.
    201 After all, I'm just rattling around in that big house all by myself.
    202 That's very considerate, but as soon as Judith and I work things out, I'm going to be back at my own house.
    203 Sweetheart, grow up.
    204 Think about what I said.
    205 You're my son, and I'll always have room for you in my house and in my heart.
    206 I love you, too, Mom.
    207 - I love you, too, Mom.
    208 - Too little.
    209 Too late.
    210 - So, Vegas was good? - It was fine.
    211 Alan, I really want to apologize for putting you through this.
    212 I was wrong to blame you for my unhappiness.
    213 No, no need to apologize.
    214 What's important is that we're here and we're working on our marriage.
    215 You look great, by the way.
    216 Must be all the extra oxygen they pump into the casinos.
    217 - Alan - And you were right.
    218 I see now that the time apart did us both a lot of good.
    219 I know I've grown.
    220 I'm not that suffocating guy you threw out of the house four and a half days ago, let me tell you that.
    221 Jake's doing fine.
    222 You were concerned about him being around my brother, but Charlie's great with kids.
    223 All right, last card, down and dirty.
    224 King's bet.
    225 - $1.
    226 - I'm in.
    227 In.
    228 I'll see $1 and raise it $5.
    229 You raised $5 on that? - I call.
    230 - I call.
    231 Queens full of nines.
    232 Kid, don't you know what a full house is? Yeah.
    233 And I also know what a psych-out is.
    234 I love this boy.
    235 And I think we're gonna look back on this as a new beginning for our marriage.
    236 A rebirth.
    237 A renaissance, if you will.
    238 Alan, I think I'm gay.
    239 All right.
    240 We'll make a list.
    241 On one side, we'll put gay stuff I'll see you and raise you $20.
    242 - I think he's got you, pal.
    243 - He's bluffing.
    244 He always pulls his ear when he bluffs.
    245 How about it, Mighty Mouse? You in? Take him down.
    246 Call you.
    247 I hate this kid.
    248 What the hell is going on here? You said "hell.
    249 " - Throw $1 in the pot.
    250 - What? Hey, we all had to.
    251 Charlie, may I speak with you privately, please? - Whose deal is it? - Jake, go to bed! I'm out.
    252 What is wrong with you? Are you insane? Do you have any sense of right and wrong? Probably not.
    253 How was dinner? How could you put Jake in a poker game with grown men? I obviously can't be trusted.
    254 So, how was dinner? I leave you alone with him for a couple of hours I'm just gonna keep asking, Alan.
    255 Dinner was swell.
    256 We both had the veal piccata and she's gay! Wow.
    257 Most chicks won't eat veal.
    258 Why do I even try talking to you? Come on, I'm just trying to get you to lighten up a little.
    259 I don't need to lighten up.
    260 The world I live in is dark.
    261 Dark and rainy.
    262 And you're useless in it! Really? I wasn't useless when you needed a place to stay.
    263 Obviously that was a mistake.
    264 Are you sure? Maybe we should make a list.
    265 Uncle Charlie? What's going on? Can't sleep? No.
    266 My dad says we're moving to Grandma's tomorrow.
    267 Yeah, that'd keep me up.
    268 If it makes you feel any better, you won $80 on that last hand.
    269 $85.
    270 $80.
    271 The house gets a cut.
    272 I wish my dad was as cool as you.
    273 Don't sell your dad short.
    274 He loves you more than anything in the world.
    275 You know that, don't you? I guess.
    276 How come you don't have any kids? I don't know.
    277 Maybe because I love me more than anything in the world.
    278 - Uncle Charlie? - Yeah? I don't want to go to Grandma's.
    279 I'd rather stay here.
    280 Yeah, well, your dad knows what's best for you.
    281 Okay.
    282 Good night, Uncle Charlie.
    283 I love you.
    284 Yeah.
    285 Okay.
    286 You got to love a kid like that.
    287 I even played him Stairway to Heaven and he still liked the Maple Loops song better.
    288 Charlie, I haven't seen you in two weeks.
    289 You finally got the house back to yourself.
    290 Now, do you want to talk about your nephew, or do you want to have sex? Sex.
    291 Definitely sex.
    292 - Let me ask you something.
    293 - Yeah? Do you ever think about having kids? Whoa, we've got a good thing going.
    294 Can't we just leave it at that? What are you doing? I thought we were gonna have sex.
    295 How am I supposed to have sex while your biological clock is going off? Hey, it's Charlie.
    296 Do your thing when you hear the beep.
    297 Hi, Monkey Man.
    298 I was just thinking about you and wondering why we hurt each other so much.
    299 Rose, it's me, Monkey Man.
    300 - Charlie? - Yeah, listen, let me ask you a question.
    301 Is there something inherently wrong with asking a woman you're involved with if she wants kids? Charlie, we got a good thing going, why do you want to mess it up? Look at you.
    302 All grown up and back living with Mom.
    303 How good do you feel about yourself right now? On a scale of one to two.
    304 I'm not back living with Mom.
    305 I'm simply staying here till Judith and I work things out.
    306 So, one? What do you want, Charlie? I figured you've been here a couple of weeks, you got to have blood in your stool by now.
    307 So, I thought if you and Jake wanted to come back to my place for a while, - that'd be okay.
    308 - Wait a minute.
    309 Are you saying you want me to come back and live with you? Well, truthfully, no.
    310 I want Jake to come back and live with me, but I figure you're a package deal.
    311 Thanks, but we're doing just fine here with Mom.
    312 Come on.
    313 We can't let Jake be exposed to her on any kind of ongoing basis.
    314 There's no ongoing basis.
    315 He's only here on weekends.
    316 That's too much.
    317 Piranhas can strip an entire cow in an hour.
    318 Alan, we've got to get him away from her.
    319 I mean, look what happened to us.
    320 And what happened to you? Hi, Mom.
    321 Charlie, you're a grown man.
    322 Perhaps it's time to stop blaming your mother for your own shortcomings.
    323 Alan, the divan is not for sitting.
    324 Charlie, get off the couch.
    325 Uncle Charlie.
    326 There's my good boy.
    327 And what did I tell you about yelling in the house? Grandma, I'm suffocating.
    328 Sound familiar? You're right, this madness must end.
    329 Here, I got you your own key.
    330 I am not comfortable with this.
    331 I mean, maybe I should go wait in the car.
    332 You're not waiting in the car.
    333 Trust me, this is a great way to meet women.
    334 I don't want to meet women.
    335 I'm still married.
    336 Come on, your wife's out meeting chicks, why shouldn't you? Your son is just adorable.
    337 - Thank you.
    338 - You and your life partner must be so proud.
    339 You're right.
    340 Go wait in the car.
    341 English
    342 



```python

```


---
**Score: 5**