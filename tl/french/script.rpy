define tc = Character("[[PROFESSEURE]", color="#ffffff",)
define c = Character("[[CAMARADE A]", color="#ffffff",)
define cb = Character("[[CAMARADE B]", color="#ffffff",)
define cc = Character("[[CAMARADE C]", color="#ffffff",)
define cd = Character("[[CAMARADE D]", color="#ffffff",)
define mm = Character("[[MÈRE]", color="#ffffff",)
define d = Character("[[PÈRE]", color="#ffffff",)
define lb = Character("[[BIBLIOTHÉCAIRE]", color="#ffffff",)
define k = Character("[[ENFANT]", color="#ffffff",)
define w = Character("[[FEMME]", color="#ffffff",)
define mc = Character("[[CAMARADE DE MARINA]", color="#ffffff",)
define n = Character("", kind=nvl, color="#ffffff",)
define aa = Character("[[MOI]", color="#ffffff",)
define tt = Character("[[FILLE]", color="#ffffff",)
define bb = Character("[[GARÇON]", color="#ffffff",)
define up = Character("[[ÉTUDIANT A]", color="#ffffff",)
define ud = Character("[[ÉTUDIANT B]", color="#ffffff",)

# Bloc de code servant à remplacer l'intro du jeu (Merci ChatGPT)
#--------------------------------------------------------------------------------------------------------------
init python:
    import renpy.exports as renpy_exports

    intro_originale = renpy_exports.movie_cutscene

    def nouvelle_intro(chemin_intro, *args, **kwargs):
        if chemin_intro == 'images/intro.webm':
            chemin_intro = "tl/French-Translation-Patch-For-Z.A.T.O/tl/french/videos/intro.webm"
        return intro_originale(chemin_intro, *args, **kwargs)

    renpy_exports.movie_cutscene = nouvelle_intro
#--------------------------------------------------------------------------------------------------------------

# game/script.rpy:73
translate french start_2b370c74:

    # "Did you know that our Sun is a very unusual star?"
    "Savais-tu que notre Soleil était une étoile inabituelle?"

# game/script.rpy:75
translate french start_463eb867:

    # "To start with, it’s a yellow dwarf."
    "Pour commencer, c’est une naine jaune."

# game/script.rpy:76
translate french start_f4fe890b:

    # extend " Those constitute for just 7-10%% of all stars in the universe."
    extend " Elles constituent tout juste entre 7 et 10 %% de toutes les étoiles dans l’univers."

# game/script.rpy:77
translate french start_c9aa57f0:

    # extend " \nIt's an outlier even among those."
    extend " \nC’est un cas particulier même parmi celles-ci."

# game/script.rpy:78
translate french start_9d40a536:

    # "Most yellow dwarves are primarily covered with dark spots."
    "La plupart des naines jaunes sont principalement recouvertes de tâches sombres."

# game/script.rpy:79
translate french start_447850d4:

    # extend " The Sun isn’t."
    extend " Le Soleil n’en a pas."

# game/script.rpy:80
translate french start_3c22fee5:

    # "The majority of its surface is bright – in fact, it has three times the number of light spots than it does dark spots."
    "La majorité de sa surface est brillante - en réalité, il y a trois fois plus de tâches claires que de tâches foncées."

# game/script.rpy:81
translate french start_7d12504d:

    # "Sure, its overall brightness index is nothing special."
    "Bien sûr, son indice de luminosité global n’a rien de spécial."

# game/script.rpy:82
translate french start_e44aabaa:

    # extend " You could even call it underwhelming compared to other stars of its type."
    extend " Nous pouvons même la qualifier de décevante comparée aux autres étoiles de son genre."

# game/script.rpy:83
translate french start_9ea3fb72:

    # "But even so, it works harder than most to shine as bright as it can."
    "Et pourtant, elle travaille plus dure que les autres pour essayer de briller aussi fort que possible."

# game/script.rpy:84
translate french start_38aafcbc:

    # extend " And I find that really cute."
    extend " Et je trouve ça\nvraiment mignon."

# game/script.rpy:92
translate french start_d6911c56:

    # "I don’t remember where I read about this."
    "Je ne me souviens pas quand j’ai lu ça."

# game/script.rpy:93
translate french start_ce4b1e27:

    # extend " Must have been some newspaper from years ago."
    extend " Mais cela devait être dans un journal datant de quelques années."

# game/script.rpy:94
translate french start_61b68228:

    # "But that small piece of trivia still pops in my mind whenever I look up at the morning sky."
    "Mais cette petite anecdote continue de me revenir en tête dès lors que je lève les yeux vers le ciel matinal."

# game/script.rpy:95
translate french start_362016be:

    # "It’s not much of a view, to be honest."
    "Pour être honnête, ce n’est pas une vue terrible."

# game/script.rpy:96
translate french start_e19da8bc:

    # extend " Not much of a sky, not much of a sun."
    extend " Ce n’est pas non plus terrible ni pour un ciel ni pour\nun soleil."

# game/script.rpy:97
translate french start_a69c39d1:

    # extend " I guess that’s the kind of region it is."
    extend " Mais je suppose que ce sont les conditions régionnales."

# game/script.rpy:98
translate french start_04d817f8:

    # "Some people say the sun is just lazing around in our parts, what with the constant snow."
    "Certaines personnes disent que le soleil paresse dans cette partie du monde vu toute la neige constante."

# game/script.rpy:99
translate french start_fa761844:

    # "But people that go around saying that, well..."
    "Mais les gens qui n’arrêtent pas de répéter ça, alors..."

# game/script.rpy:100
translate french start_996e471b:

    # extend " \nThey clearly haven’t read that newspaper."
    extend " \nIls n’ont clairement pas lu ce journal."

# game/script.rpy:109
translate french start_a064a290:

    # "The more I thought about things like that and the more I learned, the more I realised how incredible everything is."
    "Dès lors que j’ai commencé à réfléchir sur des choses comme ça, plus j’ai appris, et plus j’ai réalisé à quel point tout est si incroyable."

# game/script.rpy:110
translate french start_bd6a15bc:

    # "I'm not just saying that to mean “amazing”."
    "Et je ne dis pas ça pour dire que c’est “extraordinaire”."

# game/script.rpy:111
translate french start_4f18e5d7:

    # extend " I mean “improbable”."
    extend " Je dis ça pour dire “improbable”."

# game/script.rpy:112
translate french start_54e10e89:

    # "You can't deny the world is full of great coincidences."
    "Tu ne peux pas nier que ce monde est rempli de nombreuses coïncidences géniales."

# game/script.rpy:113
translate french start_f63310dd:

    # extend " It's to the point where I've begun to ask myself how much of it we can attribute to pure chance."
    extend " Je suis arrivée à un point où j’ai commencé à me demander à quel point nous sommes le résultat de la chance pure."

# game/script.rpy:114
translate french start_cd312a8a:

    # "The universe was so kind as to give us both a star and a planet with the perfect conditions for sentient life."
    "L’univers a été si aimable de nous donner une étoile et une planète avec les parfaites conditions pour la vie sentiente."

# game/script.rpy:115
translate french start_3e5faf55:

    # "Just the slightest fluctuation in the composition of our atmosphere, the size of the globe, or the distance between Earth and the Sun – and none of us, none of the beauty surrounding us, would exist."
    "Juste la plus petite des fluctuations dans la composition de l’atmosphère, la taille du globe, ou la distance entre la Terre et le Soleil - et plus rien de nous et de la beauté qui nous entoure ne pourrait exister."

# game/script.rpy:116
translate french start_5c45ea35:

    # "Some would call it a miracle."
    "Certains pourraient appeller ça un miracle."

# game/script.rpy:117
translate french start_f664b285:

    # extend " And of course, that's a lovely way to put it..."
    extend " Et évidemment, c’est une très belle manière de l’énoncer..."

# game/script.rpy:118
translate french start_1ad929b4:

    # extend " But isn't that giving the world we're living in too little credit?"
    extend " Mais est-ce que ce n’est pas donner trop peu de crédit au monde dans lequel nous vivons tous?"

# game/script.rpy:128
translate french start_7d0f6a58:

    # "Ah, but it’s not that I subscribe to the anthropic principle or anything!"
    "Ah, mais ce n’est pas que je crois au principe anthropique ou quoi que ce soit d’autre!"

# game/script.rpy:129
translate french start_7d05f8fa:

    # "I'm not so arrogant as to believe the universe exists just for our sake."
    "Je ne suis pas si arrogante de croire que l’univers existe juste pour notre propre intérêt."

# game/script.rpy:130
translate french start_de622ee1:

    # extend " Or rather, I'm not so sure it exists solely to be observed."
    extend " Ou alors, je ne suis pas sûre qu’il existe uniquement pour être observé."

# game/script.rpy:131
translate french start_a0a5e7e0:

    # "When a baby is born, it's not preoccupied with how it is perceived."
    "Quand un bébé naît, il n’est pas préoccupé par la manière dont il est perçu par les autres."

# game/script.rpy:132
translate french start_526fb5ae:

    # extend " That conscious need emerges later, as the child develops self-awareness."
    extend " Cette conscience a besoin d’émerger plus tard, dès que l’enfant développe une conscience de soi."

# game/script.rpy:133
translate french start_4d81d390:

    # "Until that point, its curiosity is aimed at its surroundings."
    "Jusqu’à ce stade, sa curiosité est ciblée sur tout ce qui l’entoure."

# game/script.rpy:134
translate french start_f0bda892:

    # extend " So if anything, it's the opposite of what the anthropic principle entails."
    extend " Alors, s’il y a quoi que ce soit, c’est\nl’opposé même de ce que le principe anthropique implique."

# game/script.rpy:135
translate french start_d2a60c5c:

    # "We're social creatures, so the need to be observed makes sense for our survival."
    "Nous sommes des créatures sociales, alors le besoin d’être observé fait sens avec notre but de survie."

# game/script.rpy:136
translate french start_97744645:

    # extend " But to say the universe itself shares that priority..."
    extend " Mais\nà dire que l’univers lui-même partage cette priorité..."

# game/script.rpy:137
translate french start_5611d603:

    # extend " It just doesn’t make sense to me."
    extend " Cela ne fait pas sens pour moi."

# game/script.rpy:146
translate french start_a20cefa7:

    # "..."
    "..."

# game/script.rpy:147
translate french start_8a2dc954:

    # extend "\nAlthough, you can also think about it this way."
    extend "\nCependant, tu peux aussi y penser de cette manière."

# game/script.rpy:148
translate french start_0f13e903:

    # "A child is curious about the world because it perceives the world as external."
    "Un enfant est curieux du monde car il le perçoit comme externe."

# game/script.rpy:149
translate french start_796416ff:

    # extend " But what if the child {i}is{/i} the world?"
    extend " Mais si l’enfant {i}est{/i} le monde?"

# game/script.rpy:150
translate french start_49cf68d4:

    # extend " What if all that it could ever observe existed within itself?"
    extend " Et si tout ce qu’il pouvait observer existait en lui-même?"

# game/script.rpy:151
translate french start_0b00e471:

    # "What can the all-encompassing universe be curious about?"
    "De quoi l’univers dans sa globalité pourrait être curieux?"

# game/script.rpy:152
translate french start_44134584:

    # extend " There’s nothing but itself, so nothing but itself!"
    extend " Vu qu’il n’y a rien d’autre que lui même, alors, rien d'autre que lui même!"

# game/script.rpy:153
translate french start_96d76f07:

    # "There’s nothing else to care about in the whole wide world!"
    "Il n’y a rien qui puisse assez compter dans tout le monde entier!"

# game/script.rpy:154
translate french start_fa127ab0:

    # extend " It is the world!"
    extend " Vu que c’est le monde!"

# game/script.rpy:155
translate french start_b61bcdc3:

    # extend " Duh!"
    extend " Évidemment!"

# game/script.rpy:156
translate french start_0abd53b0:

    # "Ah, wait, now this makes perfect sense."
    "Ah, mais attends, ça fait parfaitement sens maintenant."

# game/script.rpy:157
translate french start_551703c4:

    # extend " If I put it like that..."
    extend " Si je l’énonce comme ça..."

# game/script.rpy:158
translate french start_11c3dbf5:

    # extend " I guess the universe has no choice but to be self-centered."
    extend " Je suppose que l’univers n’a d’autre choix qu’être autocentré."

# game/script.rpy:167
translate french start_487dc364:

    # "Even if this wasn’t the case when it was born..."
    "Même si ce n’était pas son cas quand il était né..."

# game/script.rpy:168
translate french start_5b403766:

    # extend " What if the universe developed a desire to be perceived by others as it matured?"
    extend " Et\nsi l’univers avait développé un désir d’être perçu par les autres pendant sa croissance?"

# game/script.rpy:169
translate french start_f3ec063f:

    # extend " The same way that a child would."
    extend " Exactement de la même manière qu’un enfant."

# game/script.rpy:170
translate french start_e3672880:

    # "And what do we do when we want others to perceive us a certain way?"
    "Et que faisons-nous quand nous voulons être perçu par\nles autres d’une manière précise?"

# game/script.rpy:171
translate french start_fb54e549:

    # extend " We try to mold ourselves accordingly."
    extend " Nous essayons de nous adapter en conséquence."

# game/script.rpy:172
translate french start_0bff4179:

    # "Ah!"
    "Ah!"

# game/script.rpy:173
translate french start_8e4403d1:

    # extend " I think I get it now!"
    extend " Je pense que j’ai enfin compris!"

# game/script.rpy:174
translate french start_5c16fd9e:

    # "The universe gradually felt the desire to be seen."
    "L’univers a progressivement ressenti le besoin d’être\nvu."

# game/script.rpy:175
translate french start_ca4bec69:

    # extend " It wanted to be admired, loved and observed, because there’s nothing more a world can do but to observe itself."
    extend " Il veut être admiré, aimé et observé parce qu’il n’y a rien d’autre qu’un monde puisse faire à part de se regarder soi-même."

# game/script.rpy:176
translate french start_1d445be1:

    # "It’s the best and only pastime there is, as far as the world is concerned."
    "C’est le meilleur et seul passe-temps qui existe,\nd’aussi loin que le monde puisse être concerné."

# game/script.rpy:177
translate french start_a4bba089:

    # extend " And if observation is good, more observation is even better!"
    extend " Et si l’observation c’est bien, encore plus d’observation, c’est encore mieux!"

# game/script.rpy:178
translate french start_2cc38dd9:

    # "Of course, an endless universe can observe itself endlessly."
    "Évidemment, un univers infini peut s’observer infinimment."

# game/script.rpy:179
translate french start_7bb963bb:

    # extend " You can say that its observation value equals infinity."
    extend " On peut même dire que sa valeur d’observation est égale à infini."

# game/script.rpy:180
translate french start_1e5eb113:

    # "That value may seem absolute, but it isn’t really, not in mathematics."
    "Cette valeur peut sembler absolue, mais pas réellement, en tout cas, pas en mathématiques."

# game/script.rpy:181
translate french start_73988101:

    # extend " “Infinity plus one” exists."
    extend " “Infini plus un” existe."

# game/script.rpy:182
translate french start_56fdc8de:

    # "It’s a value that the universe could never reach as a singular, albeit infinite observer."
    "C’est une valeur que l’univers ne pourra jamais atteindre seul, bien qu’il soit un observateur infini."

# game/script.rpy:183
translate french start_2dcb8741:

    # "So it had to create new, finite observers to add to its infinity - it needed to create sentient life."
    "Alors, il a dû créé de nouveaux observateurs finis pour ajouter à son infinité - C’était nécessaire pour créer la vie sentiente."

# game/script.rpy:184
translate french start_f4ba2dd9:

    # extend " Sentient life is the plus one!"
    extend " La vie sentiente est le plus un!"

# game/script.rpy:185
translate french start_b1edf035:

    # "When I put it like that, it sounds like all of us are extras at a party..."
    "Quand je l’énonce comme ça, cela sonne comme si nous étions tous des invités supplémentaires à une fête..."

# game/script.rpy:186
translate french start_e7e0f1c3:

    # extend " Now isn’t that fun!"
    extend " Et ça, ce n’est pas amusant!"

# game/script.rpy:193
translate french start_064dcf7d:

    # "This vast mighty universe changed itself so meticulously to make new observers possible, it fine-tuned all of its systems so precisely..."
    "Ce vaste univers puissant s’est changé si méticuleusement pour créer de nouveaux observateurs possibles, il a ajusté si précisémment tous ses systèmes..."

# game/script.rpy:194
translate french start_da3b7298:

    # extend " just to have us here."
    extend " juste pour nous avoir là."

# game/script.rpy:195
translate french start_b79c8faa:

    # "It worked so hard just to share its one joy with us - us, worthless insects...!"
    "Il a travaillé si dur juste pour nous partager sa seule joie avec nous - nous, insectes sans valeur...!"

# game/script.rpy:196
translate french start_ac9cb1d4:

    # "Oh no..."
    "Oh non..."

# game/script.rpy:197
translate french start_653f65fc:

    # extend " Oh no, this can’t be...!"
    extend " Oh non, cela ne peut pas être...!"

# game/script.rpy:198
translate french start_bed1fd0d:

    # extend " That’s cute!"
    extend " C’est mignon!"

# game/script.rpy:199
translate french start_7de510d0:

    # extend " That’s really cute!"
    extend " C’est vraiment mignon!"

# game/script.rpy:200
translate french start_f841b73a:

    # "Ah, I should’ve expected this."
    "Ah, j’aurais dû m’y attendre."

# game/script.rpy:201
translate french start_6b529fb6:

    # extend " I should’ve known the infinite universe would be infinitely cute."
    extend " J’aurais dû savoir que l’univers infini serait infiniemment mignon."

# game/script.rpy:202
translate french start_9bc4357e:

    # "This world truly is wonderful, wonderful, wonderful!"
    "Ce monde est véritablement merveilleux, merveilleux, merveilleux!"

# game/script.rpy:208
translate french start_ab6d295d:

    # tc "Ira Grachevskaya is missing."
    tc "Ira Grachevskaya est absente."

# game/script.rpy:209
translate french start_0c5f900b:

    # a hmm "Huh?"
    a hmm "Huh?"

# game/script.rpy:210
translate french start_c01bb290:

    # "I look up from my desk."
    "Je lève les yeux de mon bureau."

# game/script.rpy:211
translate french start_9535a023:

    # "A low hum runs through the class."
    "Un léger bourdonnement se fait entendre dans la classe."

# game/script.rpy:212
translate french start_e7874cb1:

    # c "Grachevskaya?"
    c "Grachevskaya?"

# game/script.rpy:213
translate french start_983c803f:

    # cb "What?"
    cb "Quoi?"

# game/script.rpy:214
translate french start_a1578152:

    # cc "Seriously?"
    cc "Sérieusement?"

# game/script.rpy:215
translate french start_b7026667:

    # extend " She’s just skipping..."
    extend " Elle doit juste encore sécher..."

# game/script.rpy:216
translate french start_7c571234:

    # cd "Nah, she ran off with that one guy."
    cd "Nan, elle est partie avec ce mec-là."

# game/script.rpy:217
translate french start_e2f4f09e:

    # cb "You saw?"
    cb "Tu l’as vu?"

# game/script.rpy:218
translate french start_cb7d9092:

    # cd "No, but come on! You know her, she’s totally-"
    cd "Non, mais enfin! Tu la connais, elle est totalement-"

# game/script.rpy:220
translate french start_5487915c:

    # tc "{cps=0}{size=+5}Silence!"
    tc "{cps=0}{size=+5}Silence!"

# game/script.rpy:221
translate french start_6ca2b227:

    # "The teacher taps her journal on the desk."
    "La professeure tape avec son journal sur son bureau."

# game/script.rpy:222
translate french start_eea46458:

    # tc "Ira’s parents filed the report yesterday night."
    tc "Les parents d’Ira ont rempli un signalement hier soir."

# game/script.rpy:223
translate french start_fb764f46:

    # extend " They haven’t seen her since she left for school."
    extend " Ils ne l’ont pas revue depuis qu’elle a quitté l’école hier."

# game/script.rpy:224
translate french start_888070b9:

    # "Another round of whispers."
    "D’autres chuchotements se font entendre."

# game/script.rpy:225
translate french start_6f89c2df:

    # extend " The teacher raises her voice."
    extend " La professeure hausse sa voix."

# game/script.rpy:226
translate french start_1ccd3708:

    # tc "So if any of you have any information that might help in finding Ira, please report it to the teacher’s office or the police after class."
    tc "Alors si l’un d’entre vous a des informations pouvant aider à retrouver Ira, merci vous signaler au bureau des professeurs ou à la police après les cours."

# game/script.rpy:227
translate french start_5268d645:

    # extend " That is all."
    extend " C’est tout."

# game/script.rpy:228
translate french start_4de175ef:

    # extend " Onto the lesson."
    extend " Commençons le cours."

# game/script.rpy:229
translate french start_525f00d6:

    # "A chair creaks in the back."
    "Une chaise grince à l’arrière."

# game/script.rpy:232
translate french start_e7d41d1b:

    # g "Wait!"
    g "Attendez!"

# game/script.rpy:233
translate french start_73f72e8a:

    # extend " You really expect us to just study like normal after hearing that?"
    extend " Vous vous attendez vraiment à ce que l’on étudie normalement après avoir entendu ça?"

# game/script.rpy:234
translate french start_6266dd1c:

    # c "Yeah!"
    c "Ouais!"

# game/script.rpy:235
translate french start_9d36e996:

    # cb "Yeah!! We’re shocked, you know."
    cb "Ouais!! Vous savez, nous sommes vraiment boulversés par ça."

# game/script.rpy:236
translate french start_6b3cf13a:

    # cc "We’re worried sick!"
    cc "Nous sommes vraiment inquiets!"

# game/script.rpy:240
translate french start_ee98c5c7:

    # g "Seriously, our classmate’s missing."
    g "Sérieusement, notre camarade a disparu."

# game/script.rpy:241
translate french start_f605ade0:

    # extend " Our friend, our Irochka!"
    extend " Notre amie, notre Irochka!"

# game/script.rpy:242
translate french start_816b2e57:

    # "The room fills with repulsive giggles."
    "De plus en plus de rires répugnants se firent entendre."

# game/script.rpy:243
translate french start_38dd56ba:

    # tc "Cut it out."
    tc "Arrêtez tous de rire."

# game/script.rpy:244
translate french start_c466a4e5:

    # extend " Garin, sit back down."
    extend " Garin, rassieds-toi."

# game/script.rpy:247
translate french start_cb6155f9:

    # "The teacher’s voice sounds just as dry as it did when she broke the news."
    "La voix de la professeure est aussi sèche que lorsqu’elle a annoncé la nouvelle."

# game/script.rpy:248
translate french start_6d19de0f:

    # extend " She turns towards the blackboard to write down the date."
    extend " Elle se tourne vers le tableau noir pour écrire la date du jour."

# game/script.rpy:249
translate french start_b1140ae4:

    # tc "We all know the situation will probably..."
    tc "Nous savons tous que cette situation va probablement..."

# game/script.rpy:250
translate french start_c65dc8d7:

    # extend " resolve itself just fine."
    extend " juste se résoudre assez bien d’elle-même."

# game/script.rpy:251
translate french start_be6b251f:

    # extend " So let’s not act dramatic."
    extend " Alors, ne soit pas aussi dramatique."

# game/script.rpy:252
translate french start_a32fad53:

    # tc "If you have anything valuable to say, I’ll be happy to hear it in the office."
    tc "Si tu as quoi ce soit à dire qui ait de l’importance, je serais heureuse de l’entendre dans le bureau."

# game/script.rpy:253
translate french start_a3891bef:

    # "She puts the chalk down and begins the lesson."
    "Elle prit la craie et commença le cours."

# game/script.rpy:254
translate french start_8ae2ccb7:

    # extend " \nIt’s December 19th."
    extend " \nOn est le 19 décembre."

# game/script.rpy:255
translate french start_37e2de7a:

    # "A bird flies past the window."
    "Un oiseau passe devant la fenêtre."

# game/script.rpy:274
translate french start_5ec13ae8:

    # g "Disappearance, gimme a break!"
    g "Oh Disparition, donne-moi juste une pause!"

# game/script.rpy:275
translate french start_b3b11fb1:

    # extend " Aren’t you supposed to wait three days or something?"
    extend " N’es-tu pas supposé attendre trois jours avant de faire un signalement?"

# game/script.rpy:276
translate french start_a695b413:

    # c "That’s a myth."
    c "C’est une légende."

# game/script.rpy:277
translate french start_671e5d87:

    # extend " You can file a missing report whenever, ’specially if it’s a kid."
    extend " Tu peux faire un signalement de disparition quand tu veux, particulièrement quand c’est un enfant."

# game/script.rpy:281
translate french start_040b39e1:

    # g "Oh yeah?"
    g "Ah bon?"

# game/script.rpy:282
translate french start_3a569376:

    # extend " Hey, let’s report each other as missing and see who they find first."
    extend " Allons tous signaler chaqu’un d’entre nous comme disparu et regardons qui sera trouvé en premier."

# game/script.rpy:283
translate french start_65a54aad:

    # cb "Ha, you're on!"
    cb "Allez, c’est parti!"

# game/script.rpy:284
translate french start_5159b7e5:

    # c "No, but seriously... what's with the sudden hubbub?"
    c "Non, mais plus sérieusement... c’est quoi tout ce vacarme soudain?"

# game/script.rpy:285
translate french start_bb2145f4:

    # extend " So she didn't come home - big deal!"
    extend " Elle n’est pas rentrée chez elle - Et donc?"

# game/script.rpy:286
translate french start_55b4ef9a:

    # extend " I thought wandering off was her whole thing."
    extend " Je pensais que vagabonder était tout sa personne."

# game/script.rpy:287
translate french start_0bad426a:

    # cb "Right?"
    cb "Pas vrai?"

# game/script.rpy:288
translate french start_dc60a9e2:

    # extend " That’s just Grachevskaya for ya."
    extend " C’est tout à fait Grachevskaya."

# game/script.rpy:289
translate french start_e9c48756:

    # extend " Bet her parents just want some attention."
    extend " Je parie que ses parents veulent juste un peu d’attention."

# game/script.rpy:290
translate french start_a3918646:

    # c "Like they need any more of that."
    c "Comme s’ils en avaient besoin."

# game/script.rpy:291
translate french start_3debe6f5:

    # cc "I mean, I've heard of some weird cases..."
    cc "Je veux dire, j’ai entendu parler de certaines histoires louches..."

# game/script.rpy:294
translate french start_9ed05acd:

    # g "Yeah, never say never, crazy is genetic."
    g "Ouais, ne jamais dire jamais, la génétique est folle."

# game/script.rpy:296
translate french start_f9c92c2f:

    # extend " You think she’s in some crackhouse now?"
    extend " Tu penses qu’elle est actuellement dans une maison à crack?"

# game/script.rpy:297
translate french start_53d1c7bb:

    # cb "Haha, no way."
    cb "Haha, aucune chance."

# game/script.rpy:298
translate french start_7e474871:

    # extend " Do we even have any?"
    extend " Est-ce que déjà ça existe ici?"

# game/script.rpy:299
translate french start_01f411a3:

    # g "I wish."
    g "Je le souhaite."

# game/script.rpy:300
translate french start_490cc6ea:

    # extend " At least there’d be something fun to do."
    extend " Comme ça, il y aura au moins quelque chose d'amusant à faire."

# game/script.rpy:301
translate french start_10b2e6a7:

    # cb "Hahaha!"
    cb "Hahaha!"

# game/script.rpy:302
translate french start_e6ad011b:

    # cc "Honestly..."
    cc "Honnêtement..."

# game/script.rpy:303
translate french start_d67fc9c1:

    # c "Hey, hey."
    c "Attendez, attendez."

# game/script.rpy:304
translate french start_4d5b4918:

    # extend " But she's, like, for sure with the guy, right?"
    extend " Peut-être, est-elle, sans doute, avec ce mec-là, pas vrai?"

# game/script.rpy:308
translate french start_5e1d4a7c:

    # g "The guy?"
    g "Le mec?"

# game/script.rpy:309
translate french start_1d154c06:

    # c "You don’t know?"
    c "Tu ne sais pas?"

# game/script.rpy:310
translate french start_8828e5e0:

    # c "Buncha people have seen them together."
    c "Des gens disent qu’ils les ont vus ensemble."

# game/script.rpy:311
translate french start_8a9db1aa:

    # extend " It’s some older dude, he’s like..."
    extend " C'est une sorte de vieux gars, il a genre..."

# game/script.rpy:312
translate french start_5b5d6b55:

    # extend " thirty or something."
    extend " trente ans ou quelque chose comme ça."

# game/script.rpy:313
translate french start_a3160fbe:

    # cb "Ew!"
    cb "Beurk!"

# game/script.rpy:314
translate french start_63de225d:

    # extend " You serious?"
    extend " T’es sérieux?"

# game/script.rpy:315
translate french start_69893244:

    # cc "Yeah, it’s so trashy."
    cc "Ouais, c’est si dégueu."

# game/script.rpy:319
translate french start_62358c71:

    # "I slowly walk behind my classmates as we head to the next lesson."
    "Je marche lentement derrière mes camarades de classe pour me diriger au prochain cours."

# game/script.rpy:320
translate french start_3824adac:

    # "It’s irritating."
    "C’est frustrant."

# game/script.rpy:321
translate french start_f80ca47b:

    # extend " Their conversation is ticking me off, I’m not sure why."
    extend " Leur conversation m'énerve et je ne sais pas pourquoi."

# game/script.rpy:322
translate french start_9b061a6f:

    # "It’s not as if they aren’t making sense."
    "Ce n’est pas comme si cela faisait un quelconque sens."

# game/script.rpy:323
translate french start_51b2d3e0:

    # extend " It's not unusual for Ira to wander off somewhere on her own."
    extend " Ce n'est pas anormal pour Ira de vagabonder quelque part librement à sa guise."

# game/script.rpy:324
translate french start_cc9965a6:

    # extend " I'm not treating this news with any real gravity."
    extend " Je pense que je ne traite pas cette disparition avec assez de sérieux."

# game/script.rpy:325
translate french start_3d887658:

    # "Really, I'm no better than them."
    "Vraiment, je ne vaux pas mieux qu'eux."

# game/script.rpy:326
translate french start_eaf89da8:

    # extend " There is a trace of worry in my head, but it isn't directed towards Ira."
    extend " Il y a une trace d'inquiétude dans ma tête, mais elle n'est pas dirigée vers Ira."

# game/script.rpy:327
translate french start_3c9e52ee:

    # extend " Instead..."
    extend " Au lieu de ça..."

# game/script.rpy:328
translate french start_fa9c199a:

    # "When I first heard about her disappearance, the thought that flashed into my mind was rather ugly."
    "Quand j'ai commencé à entendre parler de sa disparition, la première pensée qui m'est venu à l'esprit était assez sale."

# game/script.rpy:335
translate french start_635f3ec5:

    # centered "{i}Now nobody will come to save me."
    centered "{i}Maintenent, personne ne viendra me sauver."

# game/script.rpy:345
translate french start_c83bc301:

    # "Gross."
    "Répugnant."

# game/script.rpy:346
translate french start_fa652857:

    # "But regardless of what people are saying..."
    "Malgré ce que les gens disent..."

# game/script.rpy:347
translate french start_e96842fe:

    # extend " and regardless of what I personally think, that's still a missing person."
    extend " et en dépit de ce que je pense personnellement, ça reste une personne disparue."

# game/script.rpy:348
translate french start_d38688df:

    # "Her poor parents must be so worried."
    "Ses pauvres parents doivent être si inquiets."

# game/script.rpy:349
translate french start_1c85b8ef:

    # extend " Just picturing it makes me feel glum."
    extend " Et juste visualiser cette situation de leur point de vue me chagrine."

# game/script.rpy:350
translate french start_767f1dc3:

    # "I'm not surprised Ira would just run off somewhere without telling anybody, but still..."
    "Je ne serais pas surprise qu'Ira se serait juste enfuie sans le dire à personne, mais pourtant..."

# game/script.rpy:351
translate french start_6dd545f9:

    # extend " still..."
    extend " pourtant..."

# game/script.rpy:358
translate french start_a20cefa7_1:

    # "..."
    "..."

# game/script.rpy:359
translate french start_cd657ead:

    # "It's not like we’ve ever been friends."
    "Ce n’est pas comme si nous étions déjà amis."

# game/script.rpy:360
translate french start_4bffa3ff:

    # extend " It would be stranger if I acted all torn up about it, right?"
    extend " Ça serait étrange si j’agissais comme si je lui en voulait pour ça, pas vrai? "

# game/script.rpy:361
translate french start_85d3f999:

    # "She’s just that kind of person."
    "Elle est juste ce type de personne."

# game/script.rpy:362
translate french start_a18e188e:

    # extend " Always getting herself in trouble, always hanging out in places she’s not supposed to be at."
    extend " Toujours à s'attirer les problèmes, à traîner là où elle ne devrait pas être."

# game/script.rpy:363
translate french start_7e29faee:

    # "They’re right, this wouldn’t be the first time Ira left for god knows where."
    "Ils ont raison, ça ne serait pas la premier fois qu'Ira parte on ne sait où pour aucune bonne raison."

# game/script.rpy:364
translate french start_ddcdf56a:

    # "But is it really true?"
    "Mais est-ce bien vrai?"

# game/script.rpy:365
translate french start_87a5de14:

    # extend " The stuff they said about that older man..."
    extend " Tout ce qu'ils ont dit sur ce vieil homme..."

# game/script.rpy:366
translate french start_23516847:

    # "I’ve never even..."
    "Je n'ai même jamais..."

# game/script.rpy:367
translate french start_208f65d4:

    # extend " I've never seen or heard anything like that."
    extend " Je n'ai jamais vu ou entendu quelque chose comme ça."

# game/script.rpy:368
translate french start_0e5aa80b:

    # extend " Even though this whole time..."
    extend " Même après tout ce temps..."

# game/script.rpy:375
translate french start_a20cefa7_2:

    # "..."
    "..."

# game/script.rpy:376
translate french start_2eec9a39:

    # extend "I suppose it’s plausible, knowing how some girls are."
    extend " Je supppose que c'est possible, sachant comment sont certaines filles."

# game/script.rpy:377
translate french start_a91326a7:

    # extend " Even so, I’d never have thought Ira would be the type to be lovestruck like that."
    extend " Même si je n'aurais jamais pensé qu'Ira serait ce type de personne à être amoureuse comme ça."

# game/script.rpy:378
translate french start_f0b18387:

    # "Lovestruck, huh..."
    "Amoureuse, hein..."

# game/script.rpy:379
translate french start_802aedc6:

    # extend " When I put it that way, then it’s almost..."
    extend " Même quand je n’énonce comme ça, cela en devient presque..."

# game/script.rpy:380
translate french start_21adb742:

    # extend " Yeah, it’s most definitely cute."
    extend " Ouais, c’est vraiment mignon."

# game/script.rpy:381
translate french start_eb823057:

    # extend " \nIra in love..."
    extend " \nIra amoureuse..."

# game/script.rpy:382
translate french start_381fedb2:

    # extend " Forbidden love, too!"
    extend " Un amour interdit, aussi!"

# game/script.rpy:383
translate french start_47c60844:

    # "Wow, I’d never have guessed."
    "Woah, je n’aurais jamais deviné."

# game/script.rpy:384
translate french start_a92c0db8:

    # extend " I never took that girl for a romantic."
    extend " Je ne l’ai jamais prise comme une romantique."

# game/script.rpy:385
translate french start_7f9f9613:

    # extend " But she is a girl at the end of the day."
    extend " Mais au final, ça reste quand même une fille."

# game/script.rpy:386
translate french start_d9ea39f4:

    # extend " And she does like those types of books..."
    extend " Et elle aime sans doute ce type de livres..."

# game/script.rpy:387
translate french start_306179aa:

    # extend " So perhaps..."
    extend " Alors peut-être que..."

# game/script.rpy:388
translate french start_5f932624:

    # "{size=+5}{cps=100}{b}She was planning to elope all along?!"
    "{size=+5}{cps=100}{b}Peut-être avait-elle prévue de s’enfuir avec son amant depuis tout ce trmps?!"

# game/script.rpy:389
translate french start_68afa09a:

    # "{cps=100}Augh, crap!"
    "{cps=100}Ah, merde!"

# game/script.rpy:390
translate french start_42e5ec0a:

    # extend " Crap, crap, it’s all so complicated...!"
    extend " Merde, merde, tout est si compliqué...!"

# game/script.rpy:391
translate french start_4d42bdcb:

    # "{cps=100}I’m really torn on this, I really am."
    "{cps=100}Je suis partagée, vraiment partagée."

# game/script.rpy:392
translate french start_8ca5fc27:

    # "{cps=100}On one hand, it’s super romantic."
    "{cps=100}D’un côté, c'est super romantique."

# game/script.rpy:393
translate french start_53aa2b34:

    # extend " Such beautiful young love with no regard for what anyone thinks..."
    extend " Un si bel amour de jeunesse, sans se préoccuper du regard des autres..."

# game/script.rpy:394
translate french start_8699f590:

    # extend " It’s so incredible!"
    extend " C’est si incroyable!"

# game/script.rpy:395
translate french start_8d5ebb01:

    # extend " It’s incredibly cute!"
    extend " Si incroyablement mignon!"

# game/script.rpy:399
translate french start_abb554b5:

    # "But on the other hand, I'm really..."
    "Mais d’un autre côté, je suis vraiment..."

# game/script.rpy:400
translate french start_546159b0:

    # extend " sad."
    extend " triste."

# game/script.rpy:401
translate french start_d14e7e2c:

    # "It's selfish and it's dumb, but if Ira is really gone..."
    "C’est égoïste et si stupide, mais si Ira a vraiment disparue..."

# game/script.rpy:402
translate french start_f0080d7b:

    # extend " It's like I've got nothing to hope for anymore."
    extend " C'est comme si je n'avais plus d'espoir en rien."

# game/script.rpy:407
translate french start_4b0219d0:

    # g "Hey, Shubina."
    g "Hey, Shubina."

# game/script.rpy:408
translate french start_b10695fa:

    # a neutral "Ah?"
    a neutral "Hein?"

# game/script.rpy:411
translate french start_499774a2:

    # g "You know anything about this?"
    g "Sais-tu quelque chose à propos de cette histoire?"

# game/script.rpy:412
translate french start_3c2d5d43:

    # a troubled "N-no..."
    a troubled "N-non..."

# game/script.rpy:413
translate french start_5846b251:

    # extend " Why would I?"
    extend " Pourquoi devrais-je?"

# game/script.rpy:414
translate french start_96494572:

    # g "Well, you two were pretty close, right?"
    g "Hé bah, vous étiez quand même assez proches, pas vrai?"

# game/script.rpy:415
translate french start_4b60ff30:

    # "Their whole group chuckles."
    "Tout le groupe éclate de rire."

# game/script.rpy:416
translate french start_06afbe4d:

    # a um "We weren't..."
    a um "Bah, nous n’étions pas..."

# game/script.rpy:417
translate french start_aea1b648:

    # g "No?"
    g "Non?"

# game/script.rpy:418
translate french start_83b34ee3:

    # a "No, not at all."
    a "Non, pas du tout."

# game/script.rpy:419
translate french start_6f0203a1:

    # g "Really?"
    g "Vraiment?"

# game/script.rpy:423
translate french start_d78ee35c:

    # extend " I thought you two were dykes."
    extend " Je pensais que vous étiez toutes les deux des gouines."

# game/script.rpy:424
translate french start_72077561:

    # a ah "Wha-"
    a ah "Quo-"

# game/script.rpy:425
translate french start_44942c28:

    # "They all erupt in laughter."
    "Ils explosèrent tous de rire."

# game/script.rpy:426
translate french start_b19c75ff:

    # a ramble "We weren't, I..."
    a ramble "Nous n’étions pas, Je..."

# game/script.rpy:427
translate french start_92a51a41:

    # extend " We didn't even talk!"
    extend " On ne se parlait même pas!"

# game/script.rpy:428
translate french start_f013b6b6:

    # c "Gahaha, Vadim, you dumbass!"
    c "Haha, Vadim, mais quel idiot!"

# game/script.rpy:429
translate french start_553cc184:

    # extend " Grachevskaya's screwing the old guy, she ain't like that."
    extend " Grachevskaya’s baise avec le vieux mec, donc elle n’est pas de ce bord."

# game/script.rpy:431
translate french start_40ff54bb:

    # g "I dunno, some chicks swing both ways."
    g "J’en sais rien moi, tu vois, certaines meufs aiment bien se taper les deux sexes."

# game/script.rpy:432
translate french start_a07f62b2:

    # extend " You never know these days, hahaha!"
    extend " On ne sait jamais de nos jours, hahaha!"

# game/script.rpy:433
translate french start_f3d41c81:

    # a concern "I don't, it's..."
    a concern "Non, c’est que..."

# game/script.rpy:434
translate french start_13b3178c:

    # c "Haha, look at her face!"
    c "Haha, regardez son visage!"

# game/script.rpy:435
translate french start_3c58abb3:

    # extend " Chill out, Shubina, we're just kidding, geez."
    extend " Détends-toi Shubina, on plaisante juste bon sang."

# game/script.rpy:438
translate french start_511858d4:

    # g "Why are you getting so scared anyways?"
    g "Pourquoi as-tu si peur de tout façon?"

# game/script.rpy:439
translate french start_68f6717a:

    # extend " You really a lesbo or something?"
    extend " Tu es vraiment lesbienne ou quoi?"

# game/script.rpy:440
translate french start_94dc30a3:

    # a ramble "I'm not...!!"
    a ramble "Non, je ne suis...!!"

# game/script.rpy:443
translate french start_7b212045:

    # "They just keep laughing."
    "Ils continuèrent à rire."

# game/script.rpy:444
translate french start_d84c307e:

    # "What can I even say to that?"
    "De toute façon, je pourrais faire quoi face à ça?"

# game/script.rpy:445
translate french start_78c1fd43:

    # extend " No matter what I do they just keep laughing."
    extend " Qu’importe ce que je fais, ils vont continuer à rire."

# game/script.rpy:446
translate french start_a3d95d5c:

    # "If Ira came in through the door right now and heard what they were saying..."
    "Si Ira passe la porte là maintenant et qu’elle entend tout ce qu’ils disent..."

# game/script.rpy:447
translate french start_61ad3e51:

    # extend " Hehe, all hell would break loose."
    extend " Héhé, tous les enfers se déchaîneraient."

# game/script.rpy:448
translate french start_4ce935a4:

    # "I mean, she only “disappeared” a day ago."
    "Je veux dire, elle n’a “disparue” qu’un jour."

# game/script.rpy:449
translate french start_6d8cc217:

    # extend " She's probably just coming late today."
    extend " Elle\nva probablement venir plus tard aujourd’hui."

# game/script.rpy:450
translate french start_51dba0f9:

    # extend " She doesn't even know there's a missing report."
    extend " Peut-être ne sait-elle même pas qu’il y a eu un signalement de disparition."

# game/script.rpy:451
translate french start_8658fba2:

    # "Maybe she has already left her lover’s place."
    "Peut-être a-t-elle déjà quitté la maison de son amant."

# game/script.rpy:452
translate french start_5f0cf7d2:

    # extend " Maybe she's trudging through our snowy schoolyard as we speak."
    extend " Peut-être est-elle en train de progresser péniblement dans toute la neige de la cour pendant qu'on parle."

# game/script.rpy:453
translate french start_0ccba116:

    # extend " No, no, she's already inside!"
    extend " Non, non, elle est déjà à l’intérieur!"

# game/script.rpy:454
translate french start_cfb074dd:

    # "She's already left her wet puffy jacket in the cloakroom."
    "Elle a déjà laissé son épaisse veste imperméable dans le vestiaire."

# game/script.rpy:455
translate french start_ea47a953:

    # extend " And now she's going down the corridor."
    extend " Et maintenant, elle descend le couloir."

# game/script.rpy:456
translate french start_42b25f1a:

    # extend " Up the stairs, to the left..."
    extend " Et là, elle monte les escaliers, vers la gauche..."

# game/script.rpy:457
translate french start_9c618390:

    # "That's right, she's coming!"
    "J’ai raison, elle arrive!"

# game/script.rpy:458
translate french start_47f8bb5c:

    # extend " She's gonna storm in any minute now!"
    extend " Elle va débarquer d'une minute à l’autre!"

# game/script.rpy:459
translate french start_7e00678a:

    # extend " Right, right, that's it!"
    extend " Ouais, ouais, c'est ça!"

# game/script.rpy:460
translate french start_e1da3a15:

    # extend " I hear her, I can hear her footsteps!"
    extend " Je l’entends, j'entends le bruit de ses pas!"

# game/script.rpy:461
translate french start_d6772e0b:

    # extend " She's coming!"
    extend " Elle arrive!"

# game/script.rpy:462
translate french start_528e9afa:

    # extend " Ira’s coming!!"
    extend " Ira arrive!!"

# game/script.rpy:467
translate french start_31c1bda8:

    # g "What's with that face?"
    g "C'est quoi cette tête?"

# game/script.rpy:468
translate french start_f4c72a82:

    # extend " You look like you're holding in a shit."
    extend " On a l’impression que tu es en train de te retenir de chier là."

# game/script.rpy:469
translate french start_30d8fa3f:

    # c "Hahaha, she's totally a lesbo."
    c "Hahaha, c'est totalement une lesbienne."

# game/script.rpy:470
translate french start_6ce4733f:

    # a concern "I'm-"
    a concern "Je..."

# game/script.rpy:471
translate french start_b6bb25b3:

    # extend " I’m not!!"
    extend " Je ne le suis pas!!"

# game/script.rpy:472
translate french start_39648e48:

    # extend sadaway " I've never talked to her, I told \nyou..."
    extend sadaway " Je ne lui ai jamais parlé, comme je vous l’ai dit..."

# game/script.rpy:473
translate french start_730596c1:

    # "The steps walk past the classroom."
    "Les pas passent devant de la salle de classe."

# game/script.rpy:474
translate french start_0fd54a8a:

    # extend " Now that they're closer, they don't sound like her at all."
    extend " Maintenant qu'ils sont plus proches, ils ne sonnent pas du tout comme elle."

# game/script.rpy:475
translate french start_23202ebd:

    # extend " They never sounded like her in the first place."
    extend " Ils ne sonnaient déjà pas comme elle en premier lieu."

# game/script.rpy:476
translate french start_e5587083:

    # g "Well maybe not with her, but like in general."
    g "Bon peut-être pas avec elle, mais peut-être plus en général alors."

# game/script.rpy:477
translate french start_0414e9d0:

    # c "Yeah, you don't have a boyfriend, right, Shubina?"
    c "Ouais, c'est vrai ça, tu n’as pas de petit copain Shubina?"

# game/script.rpy:478
translate french start_70eb4a13:

    # extend " Why's that?"
    extend " Pour quelles raisons?"

# game/script.rpy:479
translate french start_2f9f03e5:

    # a ehh "Huh?!"
    a ehh "Hein?!"

# game/script.rpy:480
translate french start_58573c0d:

    # extend " I don't know..."
    extend " Je ne sais pas..."

# game/script.rpy:481
translate french start_03edd8a2:

    # extend troubled " I just-"
    extend troubled " C’est juste-"

# game/script.rpy:482
translate french start_42db1c79:

    # g "Dude, look at her."
    g "Mec, regarde-la."

# game/script.rpy:483
translate french start_e5b1d309:

    # extend " Be real."
    extend " Soit réaliste."

# game/script.rpy:484
translate french start_f95adcb7:

    # c "Hahaha! Come on, don't say that..."
    c "Hahaha! Allez, ne dis pas ça..."

# game/script.rpy:485
translate french start_31f5ab1f:

    # g "What, you wanna be her boyfriend?"
    g "Quoi, tu veux être sa chérie?"

# game/script.rpy:487
translate french start_f57a18bd:

    # extend " Hey, Shubina, wanna go out with Igor?"
    extend " Hé, Shubina, tu veux sortir avec Igor?"

# game/script.rpy:488
translate french start_bc32ba74:

    # c "Oi!!"
    c "Hé!!"

# game/script.rpy:489
translate french start_d591a9df:

    # a concern "W-what...?"
    a concern "Q-Quoi...?"

# game/script.rpy:492
translate french start_4f4a84b3:

    # g "Come on, he's a great guy."
    g "Allez, c'est un bon gars."

# game/script.rpy:493
translate french start_163973e3:

    # extend " Right, Igor?"
    extend " N’est-ce pas Igor?"

# game/script.rpy:494
translate french start_4d967232:

    # extend " You'd treat her right."
    extend " Tu vas bien la traiter."

# game/script.rpy:495
translate french start_3e88de93:

    # c "Piss off, man!"
    c "Va te faire foutre mec!"

# game/script.rpy:496
translate french start_f55e9544:

    # extend " I'm not doing this!"
    extend " Je ne ferais pas ça!"

# game/script.rpy:498
translate french start_57aeaec8:

    # g "Gahahaha!"
    g "Hahaha!"

# game/script.rpy:499
translate french start_9be571f6:

    # a um "..."
    a um "..."

# game/script.rpy:503
translate french start_b47731c1:

    # "I bite my tongue."
    "Je me mords la langue."

# game/script.rpy:504
translate french start_d211a252:

    # "Tsk."
    "Tss."

# game/script.rpy:505
translate french start_c2ce5815:

    # extend " There I go again."
    extend " Et c'est reparti."

# game/script.rpy:506
translate french start_336067e1:

    # extend " Bad habit."
    extend " Mauvaise habitude."

# game/script.rpy:507
translate french start_8b242d0c:

    # extend " It's not like it works anyway, so why do I keep doing it?"
    extend " Ce n’est pas comme si ça marchait de tout façon alors pourquoi je continue à le faire?"

# game/script.rpy:508
translate french start_f9e0c1bf:

    # "I plop down at my desk and start mindlessly flipping through the textbook."
    "Je me laisse tomber sur mon bureau et commence sans réfléchir à feuilleter le manuel."

# game/script.rpy:509
translate french start_9b44fe0b:

    # extend " I need to stop indulging fantasies like that."
    extend " Je dois vraiment arrêter de me laisser aller à ce genre de fantaisies."

# game/script.rpy:510
translate french start_3500765a:

    # extend " It just makes me feel stupid every time."
    extend " Ça me fait juste me sentir plus stupide à chaque fois."

# game/script.rpy:511
translate french start_a2eff528:

    # "If Ira came in through that door and beat them up right then and there, would it really help my case?"
    "Si Ira passe cette porte et les tabassait sur-le-champ, est-ce que ça réglerait vraiment le problème?"

# game/script.rpy:512
translate french start_1e7532a0:

    # "They'd probably keep saying those same things behind her back."
    "Elle dit probalement les mêmes choses derrière mon dos."

# game/script.rpy:513
translate french start_3372b664:

    # extend " And to my face..."
    extend " Alors en face..."

# game/script.rpy:514
translate french start_a45aeb59:

    # "I guess it really would be for the worse."
    "Je suppose que ça serait encore pire."

# game/script.rpy:515
translate french start_c29080bf:

    # extend " Yeah, I shouldn't have wished for that."
    extend " Ouais, je ne devrais pas souhaiter ça."

# game/script.rpy:516
translate french start_60702c97:

    # extend " If Ira saw that, it would just add fuel to the fire."
    extend " Si Ira avait pu voir ça, elle aurait juste jeter de l’huile sur le feu."

# game/script.rpy:517
translate french start_24c24517:

    # "So it's a good thing that she didn't interfere."
    "Alors c’est une bonne chose qu’elle ne soit pas intervenue."

# game/script.rpy:518
translate french start_849ebc50:

    # extend " \nIt's a good thing, it's a really great thing."
    extend "\nC’est une bonne chose, une très bonne chose."

# game/script.rpy:524
translate french start_09d64919:

    # "Hah..."
    "Ha ha..."

# game/script.rpy:525
translate french start_804e7cb6:

    # "At least these guys don’t bother me for the rest of the day."
    "Au moins, ils ne m’ont pas embêtés durant le reste de la journée."

# game/script.rpy:526
translate french start_9c73ee07:

    # extend " Everyone's too preoccupied with gossip."
    extend " Tout le monde est beaucoup trop préoccupé par les ragots."

# game/script.rpy:527
translate french start_1ae8fd52:

    # "I can’t focus on studying either."
    "Je n'arrive pas plus à me concentrer sur le fait d’étudier."

# game/script.rpy:528
translate french start_2de72e36:

    # extend " I keep thinking..."
    extend " Je n’arrête pas d’y penser..."

# game/script.rpy:534
translate french start_c4373e5b:

    # "The last time I saw Ira..."
    "La dernière fois que j’ai vu Ira..."

# game/script.rpy:535
translate french start_f3a6162c:

    # "The teacher says her parents saw her leaving in the morning."
    "La professeure a dit que ses parents l’ont vu pour la dernière fois dans la matinée."

# game/script.rpy:536
translate french start_ab902ff7:

    # extend " But she didn’t show up to class."
    extend " Mais elle ne s'est pas présentée en classe."

# game/script.rpy:537
translate french start_c0f486d3:

    # "That part's nothing new."
    "Mais là, rien de nouveau."

# game/script.rpy:538
translate french start_f234dcd7:

    # extend " Ira has always had a bad attendance record."
    extend " Ira a toujours eu un haut taux d'absence en cours."

# game/script.rpy:539
translate french start_6e99bb30:

    # "So I assume she skipped as usual..."
    "Alors j’en déduis qu’elle a séché les cours comme à son habitude..."

# game/script.rpy:540
translate french start_f9c2bd3c:

    # extend " and went to see that man they talked about?"
    extend " et qu’elle est allé voir l’homme dont ils parlent tous?"

# game/script.rpy:541
translate french start_677a1ab7:

    # extend " Did she go to him right away?"
    extend " Est-elle allée le voir immédiatement?"

# game/script.rpy:542
translate french start_c138523d:

    # "Because in that case..."
    "Parce que dans ce cas..."

# game/script.rpy:543
translate french start_33b959a6:

    # extend " in that case, yesterday evening..."
    extend " dans ce cas, l’évènement d’hier..."

# Ajout manuel numéro 1
translate french strings:

    old "{i}“Go home, Asya.”"
    new "{i}“Retourne chez toi, Asya.”"

# game/script.rpy:567
translate french start_61e86d26:

    # "The teacher’s office, was it...?"
    "Le bureau des professeurs, est-ce...?"

# game/script.rpy:568
translate french start_899e030c:

    # "I’m kinda scared of going straight to the police."
    "Je suis assez apeurée d'aller directement voir la police."

# game/script.rpy:569
translate french start_6ca272ac:

    # extend " But I should..."
    extend " Mais je devrais..."

# game/script.rpy:570
translate french start_a7f6d6cc:

    # extend " I should probably report that."
    extend " Je devrais probablement signaler ça."

# game/script.rpy:571
translate french start_dc0f3e6b:

    # "Not sure if it will be of any help."
    "Je ne suis pas sûre que cela sera utile."

# game/script.rpy:572
translate french start_9cfebb8e:

    # extend " And for some reason the idea of telling anyone what I saw..."
    extend " Et pour une raison ou une autre, l'idée de dire à quelqu’un ce que j'ai vu..."

# game/script.rpy:573
translate french start_afbb7242:

    # extend " something about it just doesn’t sit right with me."
    extend " quelque chose là-dedans me dérange."

# game/script.rpy:574
translate french start_784ad581:

    # "But there's no logical reason for that."
    ""

# game/script.rpy:575
translate french start_f43e597f:

    # extend " I need to get over myself."
    extend ""

# game/script.rpy:576
translate french start_7d17c9e8:

    # "Sure, she’s probably fine - I know that, freaking everyone knows that!"
    ""

# game/script.rpy:577
translate french start_a1ecd9c3:

    # extend " But if she’s not, well..."
    extend ""

# game/script.rpy:578
translate french start_4e2dea3b:

    # extend "\nI’m gonna regret it big time!"
    extend ""

# game/script.rpy:580
translate french start_179c806b:

    # "Oh, but I might also be tearing star-crossed lovers apart..."
    ""

# game/script.rpy:581
translate french start_b5db9ce2:

    # "If Ira really ran away to be with someone that she cares about so deeply, away from society’s ridicule, would it really be right to ruin it?"
    ""

# game/script.rpy:582
translate french start_cc1509f1:

    # "...Crap."
    ""

# game/script.rpy:583
translate french start_bb7b3b20:

    # extend " I have to admit..."
    extend ""

# game/script.rpy:584
translate french start_54d93eb2:

    # extend " I’m also a little judgemental."
    extend ""

# game/script.rpy:585
translate french start_b6db7069:

    # "I mean, it’s really beautiful, I do believe that judging love like that is ugly, ugly, ugly, but whenever I start to consider it closely, I just can’t brush off how much older that man is, I just can’t."
    ""

# game/script.rpy:586
translate french start_0a340a2f:

    # "Ugh, I’m really no better than the rest..."
    ""

# game/script.rpy:588
translate french start_8e9b38a6:

    # "Wait!"
    ""

# game/script.rpy:589
translate french start_3545ffdc:

    # extend " That's it!"
    extend ""

# game/script.rpy:590
translate french start_a012686e:

    # extend " So that’s why I don’t want to tell anyone about what I saw!"
    extend ""

# game/script.rpy:591
translate french start_c7cfcd72:

    # "It must be the good in me screaming, {w=0.2}{cps=100}“Don’t ruin their good fortune! {w=0.2}They’re probably so happy together right now! {w=0.2}It’s none of your business!”"
    ""

# game/script.rpy:592
translate french start_e60d580b:

    # "Gosh, yes, that must be it."
    ""

# game/script.rpy:593
translate french start_fe8c20f5:

    # extend " That explains everything."
    extend ""

# game/script.rpy:594
translate french start_50fe0797:

    # "Should I follow my heart then?"
    ""

# game/script.rpy:595
translate french start_38eaaab3:

    # extend " Should I keep silent?"
    extend ""

# game/script.rpy:600
translate french start_dd83981b:

    # "It’s not as if what I had seen will make a difference."
    ""

# game/script.rpy:601
translate french start_f6de8c73:

    # extend " It was kind of inconsequential."
    extend ""

# game/script.rpy:602
translate french start_2e62c6bd:

    # extend " There’s no point in telling anyone about it at all."
    extend ""

# game/script.rpy:603
translate french start_4caf9da6:

    # "It's not the kind of information that points to any particular location or culprit."
    ""

# game/script.rpy:604
translate french start_55a3bf7d:

    # extend " Not that there is one."
    extend ""

# game/script.rpy:605
translate french start_33e4ca6f:

    # "{cps=80}So let’s keep silent and everyone will be happy!"
    ""

# game/script.rpy:606
translate french start_619b62e2:

    # extend " I’ll be happy, the good irrational me will be happy, and the cold reasonable me will be happy as well."
    extend ""

# game/script.rpy:607
translate french start_73076c1a:

    # extend " {cps=80}Yup, yup!"
    extend ""

# game/script.rpy:608
translate french start_d9716129:

    # "{cps=80}Good job, Asya, you solved it."
    ""

# game/script.rpy:609
translate french start_c48d9f88:

    # extend " Ah, it sure is nice to have a clean conscience."
    extend ""

# game/script.rpy:610
translate french start_59e18383:

    # "{cps=80}Welp, no need to loaf around here any longer!"
    ""

# game/script.rpy:611
translate french start_468e837f:

    # extend " Guess I better head home!"
    extend ""

# game/script.rpy:617
translate french start_f43ee050:

    # "{cps=100}{size=+10}{b}Counterpoooooint!!{/b}" with vpunch
    "" with vpunch

# game/script.rpy:618
translate french start_01bb8187:

    # extend " {/size}\nCounterpoint, counterpoint!"
    extend ""

# game/script.rpy:619
translate french start_73a8f757:

    # "{cps=100}What if, and bear with me here, what if Ira is actually missing?"
    ""

# game/script.rpy:620
translate french start_e44cf88d:

    # extend " Despite all odds, there’s always a possibility that she is in danger."
    extend ""

# game/script.rpy:621
translate french start_16328e8d:

    # "{cps=100}If there’s even the tiniest chance that my report will help in finding her, then that info is worth providing!"
    ""

# game/script.rpy:622
translate french start_be60bc2d:

    # "{cps=100}And if she really did elope with her beloved, then my testimony won't change a thing."
    ""

# game/script.rpy:623
translate french start_aaccd201:

    # extend " It's worthless at worst!"
    extend ""

# game/script.rpy:628
translate french start_a20cefa7_3:

    # "..."
    ""

# game/script.rpy:629
translate french start_c57e2b79:

    # extend "That’s true."
    extend ""

# game/script.rpy:630
translate french start_b6ef972f:

    # "{cps=100}If I carefully weigh the pros and cons, that off chance of Ira being in danger and my words being the key to saving her makes for a strong argument."
    ""

# game/script.rpy:631
translate french start_011ae1bd:

    # "Woah..."
    ""

# game/script.rpy:632
translate french start_67f68254:

    # extend " “My words being the key to saving her”..."
    extend ""

# game/script.rpy:633
translate french start_33e7ae55:

    # "{cps=100}Wow, yeah!"
    ""

# game/script.rpy:634
translate french start_ccee20c7:

    # extend " {cps=100}That would be so amazing!"
    extend ""

# game/script.rpy:637
translate french start_4c527c6f:

    # "{cps=100}And then I’d come and visit her in the hospital, and she wouldn’t know how to thank me."
    ""

# game/script.rpy:638
translate french start_31379655:

    # extend " She’d say I shouldn’t have, she’d say, {w=0.2}“I told you to leave me alone, dummy”."
    extend ""

# game/script.rpy:639
translate french start_cb279d72:

    # "{cps=100}But then I’d just shake my head and respond, “It’s nothing. {w=0.2}I was just doing what I was supposed to...”"
    ""

# game/script.rpy:640
translate french start_1c637cd3:

    # "Hm, no, I gotta come up with something cooler."
    ""

# game/script.rpy:641
translate french start_32efc09e:

    # extend " I’ll need to think about that..."
    extend ""

# game/script.rpy:646
translate french start_f220f517:

    # "{cps=100}{size=+5}Wait, wait, why is she in the hospital?!"
    ""

# game/script.rpy:647
translate french start_9705c78e:

    # "{cps=100}Do I hope Ira ends up in the hospital?"
    ""

# game/script.rpy:648
translate french start_21d28aad:

    # extend " Geez, of course not!"
    extend ""

# game/script.rpy:649
translate french start_98003e4c:

    # "{cps=100}I don’t need my freaking testimony to save her."
    ""

# game/script.rpy:650
translate french start_e1c42bef:

    # extend " I hope my testimony is useless because she’s already home."
    extend ""

# game/script.rpy:651
translate french start_5245f8be:

    # extend " Or is calling home, telling her parents how happy she is with the love of her life."
    extend ""

# game/script.rpy:652
translate french start_7e682148:

    # extend " That’s what I hope for."
    extend ""

# game/script.rpy:653
translate french start_58ef6680:

    # "Ugh, I just keep having stupid thoughts today."
    ""

# game/script.rpy:659
translate french start_01c71600:

    # "At least I know what I should do now."
    ""

# game/script.rpy:660
translate french start_615a4f8c:

    # extend " I’ve made my decision."
    extend ""

# game/script.rpy:661
translate french start_a5f4b41e:

    # "I’m going to the teacher’s office."
    ""

# game/script.rpy:662
translate french start_ef2d473b:

    # extend " Where was it again?"
    extend ""

# game/script.rpy:663
translate french start_eb4366a7:

    # "I doubt they expect anyone to come."
    ""

# game/script.rpy:664
translate french start_1aa9f9a4:

    # extend " I’ll probably look kind of silly..."
    extend ""

# game/script.rpy:665
translate french start_f1fd3f9c:

    # extend " Wouldn’t be the first time."
    extend ""

# game/script.rpy:666
translate french start_0fccfc8e:

    # "Well, who cares."
    ""

# game/script.rpy:667
translate french start_1c401398:

    # "Walking, walking."
    ""

# game/script.rpy:668
translate french start_ac52cfe5:

    # extend " Down the staircase, to the right, down the hall."
    extend ""

# game/script.rpy:669
translate french start_43db9e3b:

    # "There, that’s the teacher’s office!"
    ""

# game/script.rpy:678
translate french start_04d8e3bd:

    # "...Oh?"
    ""

# game/script.rpy:683
translate french start_b0452b4c:

    # "A girl."
    ""

# game/script.rpy:684
translate french start_64891d92:

    # extend " There’s a girl standing there, right by the door."
    extend ""

# game/script.rpy:685
translate french start_af1edad2:

    # "I think I’ve seen her before..."
    ""

# game/script.rpy:686
translate french start_34fe90e1:

    # extend " Is she an upperclassman?"
    extend ""

# game/script.rpy:687
translate french start_8a8212bd:

    # "Our town is really tiny, and so is our school – if I were a better person, I would know her name."
    ""

# game/script.rpy:689
translate french start_cfc47ad1:

    # q "Hm?"
    q ""

# game/script.rpy:690
translate french start_00d4946b:

    # "She turns to look at me."
    ""

# game/script.rpy:691
translate french start_e34d5de2:

    # extend " I’m not sure what she is expecting so I nod a little."
    extend ""

# game/script.rpy:692
translate french start_ab5a3eda:

    # a neutral "Um..."
    a neutral ""

# game/script.rpy:693
translate french start_2ddb273a:

    # extend " Is there a queue?"
    extend ""

# game/script.rpy:698
translate french start_d580d3a8:

    # q "A queue?"
    q ""

# game/script.rpy:699
translate french start_cd27cb62:

    # a "To the office."
    a ""

# game/script.rpy:700
translate french start_f7653c39:

    # q "Oh..."
    q "Oh..."

# game/script.rpy:707
translate french start_7cab623c:

    # extend " Oh, no!"
    extend "Oh, non!"

# game/script.rpy:708
translate french start_414b8ee2:

    # extend " I’m just waiting for someone."
    extend "J'attends juste quelqu'un. "

# game/script.rpy:709
translate french start_2eeb52e6:

    # a "Ah, okay."
    a ""

# game/script.rpy:714
translate french start_cb594cfa:

    # q "Hey."
    q ""

# game/script.rpy:715
translate french start_419d5750:

    # a "What?"
    a ""

# game/script.rpy:716
translate french start_73351caa:

    # q "You’re Asya, right?"
    q ""

# game/script.rpy:717
translate french start_aa5dd74a:

    # a woah "Ah-"
    a woah ""

# game/script.rpy:718
translate french start_bc5ce564:

    # extend " Yes!"
    extend ""

# game/script.rpy:719
translate french start_51d6cd0a:

    # extend " How did you know?"
    extend ""

# game/script.rpy:725
translate french start_19121f83:

    # q "That's kind of a loaded question."
    q ""

# game/script.rpy:726
translate french start_b722324a:

    # extend " How do we know anything?"
    extend ""

# game/script.rpy:727
translate french start_3f1f3e73:

    # a pout "Er...?"
    a pout ""

# game/script.rpy:733
translate french start_c163df86:

    # q "I mean, it’s not like we have lotsa faces to remember here."
    q ""

# game/script.rpy:734
translate french start_47d57edf:

    # extend " You know me too, right?"
    extend ""

# game/script.rpy:735
translate french start_b9ba9647:

    # a troubled "Umm..."
    a troubled ""

# game/script.rpy:736
translate french start_d274c660:

    # extend uff " Sorry."
    extend uff ""

# game/script.rpy:741
translate french start_a6f85296:

    # q "Really...?"
    q ""

# game/script.rpy:743
translate french start_070becd0:

    # "{cps=100}Guh, that’s what I was talking about...!"
    ""

# game/script.rpy:745
translate french start_a58596ae:

    # "It’s not that I don’t care to remember everyone’s names."
    ""

# game/script.rpy:746
translate french start_74cd0f54:

    # extend " I just don’t know where other people get them from."
    extend ""

# game/script.rpy:747
translate french start_3bb01d90:

    # "They say that in tiny cities like this everyone knows each other, but that’s just not true."
    ""

# game/script.rpy:748
translate french start_2a4b0753:

    # "We learn about the people outside of our immediate circle through gossip or common friends."
    ""

# game/script.rpy:749
translate french start_52ff36a8:

    # extend " But I haven’t made any new ones since the day Tosya left."
    extend ""

# game/script.rpy:750
translate french start_13c68873:

    # extend " And gossip..."
    extend ""

# game/script.rpy:751
translate french start_0da34f20:

    # "Sure, sometimes I overhear my classmates chatting about this and that."
    ""

# game/script.rpy:752
translate french start_d9047790:

    # "But I don’t like listening to them, I don’t like their voices, so I try not to pay them too much attention."
    ""

# game/script.rpy:753
translate french start_e81efaa7:

    # "Wait..."
    ""

# game/script.rpy:754
translate french start_90718421:

    # extend " When I put it like that, it kinda does sound like my fault..."
    extend ""

# game/script.rpy:755
translate french start_10ee9ec5:

    # "My point is, when people regurgitate that idea of “everyone knows everyone”, the word “everyone” doesn’t include me."
    ""

# game/script.rpy:761
translate french start_e5c60e2f:

    # q "The name’s Marina."
    q ""

# game/script.rpy:762
translate french start_b466ac7d:

    # a neutral "...Oh!"
    a neutral ""

# game/script.rpy:763
translate french start_2d4f5287:

    # extend " Nice to meet you."
    extend ""

# game/script.rpy:768
translate french start_cd8e37aa:

    # m "Nice to meet ya too."
    m ""

# game/script.rpy:769
translate french start_7425bc38:

    # extend " You got something to share about Grachevskaya?"
    extend ""

# game/script.rpy:770
translate french start_adb04f86:

    # a surprised "H-how did you know?!"
    a surprised ""

# game/script.rpy:774
translate french start_d46cfedc:

    # m "Whadya mean, how?"
    m ""

# game/script.rpy:775
translate french start_57db30b4:

    # extend " We had an announcement, same as you."
    extend ""

# game/script.rpy:778
translate french start_8e2e43cb:

    # extend " They told us to report to the teachers and all."
    extend ""

# game/script.rpy:779
translate french start_34178bec:

    # a hmm "Ah."
    a hmm ""

# game/script.rpy:780
translate french start_83d0f6c0:

    # extend " I see..."
    extend ""

# game/script.rpy:782
translate french start_8d946cae:

    # "For some reason I thought they only broke the news to us, Ira’s classmates."
    ""

# game/script.rpy:783
translate french start_2e11f0ff:

    # extend " But it makes sense they’d at least give the upperclassmen a heads up, just in case they happened to know her."
    extend ""

# game/script.rpy:784
translate french start_5a54d224:

    # "Which means..."
    ""

# game/script.rpy:785
translate french start_66b82a71:

    # a neutral "You also know something about Ira?"
    a neutral ""

# game/script.rpy:786
translate french start_c46c0332:

    # m "Yup."
    m ""

# game/script.rpy:787
translate french start_befbf63a:

    # a woah "Ah! That’s..."
    a woah ""

# game/script.rpy:788
translate french start_b647b3a3:

    # extend " That’s great!"
    extend ""

# game/script.rpy:789
translate french start_84f1f348:

    # a neutral "S-so you talked to the teachers already?"
    a neutral ""

# game/script.rpy:792
translate french start_4a471581:

    # m "Sure did!"
    m ""

# game/script.rpy:793
translate french start_ffb5e2c5:

    # a hmm "Wow..."
    a hmm ""

# game/script.rpy:794
translate french start_ffc38752:

    # extend " Um."
    extend ""

# game/script.rpy:795
translate french start_f92bee29:

    # extend awkward " A-and what did you tell them...?"
    extend awkward ""

# game/script.rpy:799
translate french start_770f1dec:

    # m "Tsk-tsk-tsk."
    m ""

# game/script.rpy:800
translate french start_a340eefb:

    # extend " That's between me and the investigation."
    extend ""

# game/script.rpy:803
translate french start_0c2879c1:

    # extend " You can't just spout info like that out in the open, Asya."
    extend ""

# game/script.rpy:804
translate french start_3431ce06:

    # extend " The walls got ears!"
    extend ""

# game/script.rpy:805
translate french start_5bd43de2:

    # a concern "O-oh..."
    a concern ""

# game/script.rpy:806
translate french start_5ab551e5:

    # extend " I-I understand..."
    extend ""

# game/script.rpy:807
translate french start_b5f4f2c6:

    # extend troubled " Sorry."
    extend troubled ""

# game/script.rpy:810
translate french start_0f1a0d5a:

    # m "Okay, well, you don't have to apologise..."
    m ""

# game/script.rpy:812
translate french start_4916825d:

    # "Crap, crap."
    ""

# game/script.rpy:813
translate french start_8a4e20ef:

    # extend " I'm making an awful first impression."
    extend ""

# game/script.rpy:814
translate french start_529c3554:

    # "Not only did I not know her name like I was supposed to, but now I look like I don't know the first thing about vigilance..."
    ""

# game/script.rpy:815
translate french start_6362ee0a:

    # "{cps=100}Aaagh, who am I kidding!!"
    ""

# game/script.rpy:816
translate french start_ca18113c:

    # extend " I really don't!!!"
    extend ""

# game/script.rpy:818
translate french start_8b345740:

    # a awkward "U-um!"
    a awkward ""

# game/script.rpy:819
translate french start_ee9d035a:

    # extend " I’ll just go in then...!"
    extend ""

# game/script.rpy:820
translate french start_960eaf25:

    # "Marina suddenly blocks my path."
    ""

# game/script.rpy:824
translate french start_7895fe89:

    # m "Haha, no you won’t."
    m ""

# game/script.rpy:825
translate french start_9ceef5ea:

    # a pout "...I’m sorry?"
    a pout ""

# game/script.rpy:829
translate french start_2843da2c:

    # m "You’re not telling them a-{w=0.3}ny-{w=0.3}thing."
    m ""

# game/script.rpy:830
translate french start_181d97cb:

    # "She gestures with her finger to the tact of each syllable."
    ""

# game/script.rpy:831
translate french start_5136f9e6:

    # a troubled "Um..."
    a troubled ""

# game/script.rpy:832
translate french start_7136eebd:

    # extend " Why?"
    extend ""

# game/script.rpy:836
translate french start_ab3d84eb:

    # m "Because..."
    m ""

# game/script.rpy:838
translate french start_aa8e73a5:

    # "A bad feeling stirs up in my chest."
    ""

# game/script.rpy:839
translate french start_8635925e:

    # extend " Please, don’t tell me it’s gonna be the same thing as my classmates."
    extend ""

# game/script.rpy:840
translate french start_f63ce9eb:

    # "Is this because I acted rude?"
    ""

# game/script.rpy:841
translate french start_19a9b4df:

    # extend " I didn’t mean to."
    extend ""

# game/script.rpy:842
translate french start_55d665b9:

    # extend " Well, I never mean to."
    extend ""

# game/script.rpy:843
translate french start_94497614:

    # "Ah, I just can’t help it, can I?"
    ""

# game/script.rpy:844
translate french start_1e7c60f4:

    # extend " We just met, and I’ve already managed to mess everything up."
    extend ""

# game/script.rpy:845
translate french start_348ff52d:

    # extend " Damn it, damn it, damn it!"
    extend ""

# game/script.rpy:846
translate french start_ac9ebe88:

    # "I desperately search her face for signs of mockery."
    ""

# game/script.rpy:847
translate french start_36c91d83:

    # extend " But... weirdly, I can’t find any."
    extend ""

# game/script.rpy:851
translate french start_f0a3dee5:

    # m "I’ve been waiting for {b}you."
    m ""

# game/script.rpy:852
translate french start_5908e44a:

    # a woah "...Huh?"
    a woah ""

# game/script.rpy:853
translate french start_916686be:

    # m "Hehehe!"
    m ""

# game/script.rpy:854
translate french start_c2824638:

    # extend " Surprised?"
    extend ""

# game/script.rpy:855
translate french start_44b0148b:

    # "Of course I am!"
    ""

# game/script.rpy:857
translate french start_7a0e59a6:

    # "...No, wait."
    ""

# game/script.rpy:858
translate french start_9e235c0a:

    # extend " This has to be some stupid ruse."
    extend ""

# game/script.rpy:859
translate french start_82858276:

    # extend " I'm going to believe this girl and then she'll just laugh in my face about it."
    extend ""

# game/script.rpy:864
translate french start_1fc61003:

    # m "I'm serious."
    m ""

# game/script.rpy:865
translate french start_d10a467d:

    # extend " Ira told me about you."
    extend ""

# game/script.rpy:866
translate french start_fc7eef9d:

    # a woah "R-really?"
    a woah ""

# game/script.rpy:867
translate french start_61ad1bd4:

    # m "Yeah!"
    m ""

# game/script.rpy:868
translate french start_78daf776:

    # "Oh gosh, they talked about me?"
    ""

# game/script.rpy:869
translate french start_11f0c5ed:

    # extend " Wow..."
    extend ""

# game/script.rpy:870
translate french start_974dc25e:

    # "I’m shocked Marina is being as friendly as she is, considering the kind of description Ira could give..."
    ""

# game/script.rpy:871
translate french start_45dabb36:

    # "Wait, does this mean she is a friend of Ira's?"
    ""

# game/script.rpy:872
translate french start_4a221a7f:

    # extend " For some reason I never thought about her having any, at least not at school."
    extend ""

# game/script.rpy:873
translate french start_8755da55:

    # extend " That was really presumptuous of me."
    extend ""

# game/script.rpy:874
translate french start_44495e86:

    # "I wonder what Ira is like when she’s with friends."
    ""

# game/script.rpy:878
translate french start_33d81190:

    # m "I know you saw her yesterday."
    m ""

# game/script.rpy:879
translate french start_7ec7ab3a:

    # a sus "!..."
    a sus ""

# game/script.rpy:880
translate french start_ac888c0e:

    # m "I figured you’d want to report it, so I ran here as soon as classes ended!"
    m ""

# game/script.rpy:884
translate french start_8c17dfbd:

    # extend " I guess it’d be easier to catch you between lessons, but, haha..."
    extend ""

# game/script.rpy:887
translate french start_7a2223c2:

    # m "I got so caught up in all of those stupid rumours!"
    m ""

# game/script.rpy:888
translate french start_1e81755f:

    # extend " It kinda slipped my mind."
    extend ""

# game/script.rpy:889
translate french start_9c388ee0:

    # "She knows...?"
    ""

# game/script.rpy:891
translate french start_ad580f97:

    # m "But hey, what matters is that it all worked out!"
    m ""

# game/script.rpy:892
translate french start_5136f9e6_1:

    # a troubled "Um..."
    a troubled ""

# game/script.rpy:893
translate french start_7b68d4d5:

    # extend um " So why are you stopping me?"
    extend um ""

# game/script.rpy:896
translate french start_624f500b:

    # m "Aha."
    m ""

# game/script.rpy:897
translate french start_79eb252c:

    # extend " Well..."
    extend ""

# game/script.rpy:898
translate french start_69019a94:

    # "Marina looks around the empty corridor before lowering her voice."
    ""

# game/script.rpy:902
translate french start_1620885c:

    # m "If you tell them about yesterday, you'll make everything worse."
    m ""

# game/script.rpy:903
translate french start_25337883:

    # a concern "Huh?"
    a concern ""

# game/script.rpy:906
translate french start_4500893b:

    # m "Let’s not talk about this in front of the office, okay?"
    m ""

# game/script.rpy:907
translate french start_bf8a61f0:

    # extend " Come on, let’s go."
    extend ""

# game/script.rpy:908
translate french start_faad256c:

    # "She takes a step back and beckons me with her hand."
    ""

# game/script.rpy:909
translate french start_e3c08905:

    # extend " I’m not sure what she has in mind, but it doesn’t seem like a prank."
    extend ""

# game/script.rpy:910
translate french start_d61b8cec:

    # extend " Still..."
    extend ""

# game/script.rpy:911
translate french start_e6bee468:

    # a ehh "Wait!"
    a ehh ""

# game/script.rpy:913
translate french start_3b4094a8:

    # a troubled "I know Ira's probably fine, but..."
    a troubled ""

# game/script.rpy:914
translate french start_8c8cf58c:

    # extend concern " i-isn't it \nbetter to play it safe?"
    extend concern ""

# game/script.rpy:915
translate french start_77b04be5:

    # extend " The faster we share \nall we know with everyone, the-"
    extend ""

# game/script.rpy:920
translate french start_4522b6bc:

    # m "Quieeet, you!"
    m ""

# game/script.rpy:921
translate french start_bb8b2bf0:

    # extend " I just said that we shouldn’t talk about this stuff where the adults can hear!"
    extend ""

# game/script.rpy:923
translate french start_a33f76e9:

    # a ehh "Wah!"
    a ehh ""

# game/script.rpy:928
translate french start_04c72c6c:

    # "Marina grabs my hand and starts dragging me down the corridor."
    ""

# game/script.rpy:929
translate french start_51db41e8:

    # extend " She’s not exactly being quiet either!"
    extend ""

# game/script.rpy:930
translate french start_968327c4:

    # "All of my stumbled protests sound so weak they might as well be white noise to the other girl."
    ""

# game/script.rpy:931
translate french start_b4e7ac64:

    # "Yes, I spent half the day doubting whether I should report at all!"
    ""

# game/script.rpy:932
translate french start_1f3aa72c:

    # extend " So what?"
    extend ""

# game/script.rpy:933
translate french start_e1e4503c:

    # "I carefully examined my options and came to my own conclusion!"
    ""

# game/script.rpy:934
translate french start_874815b7:

    # extend " I deserve to see it though!"
    extend ""

# game/script.rpy:935
translate french start_2b37e19f:

    # extend " I deserve to testify!!"
    extend ""

# game/script.rpy:937
translate french start_a20cefa7_4:

    # "..."
    ""

# game/script.rpy:938
translate french start_5f9ae42f:

    # extend "But some part of me is relieved that the ultimate choice was made for me."
    extend ""

# game/script.rpy:939
translate french start_8a23056f:

    # extend " I mean, that silly gut feeling I thought I overcame with reason has come out on top."
    extend ""

# game/script.rpy:940
translate french start_0d4e8328:

    # "{cps=80}So there was something to it in the end!"
    ""

# game/script.rpy:941
translate french start_a0827b7f:

    # extend " So I was right, my heart was right!"
    extend ""

# game/script.rpy:943
translate french start_b2fc8187:

    # "{cps=80}Sure, I can’t actually know that, since I’m yet to hear what Marina has to say."
    ""

# game/script.rpy:944
translate french start_3cdb1b45:

    # extend " {cps=80}But this can’t be pure chance, can it?"
    extend ""

# game/script.rpy:945
translate french start_1b4fe8ef:

    # extend " {cps=80}And if it’s not, what does it actually hinge on?"
    extend ""

# game/script.rpy:946
translate french start_c1dfbc83:

    # "{cps=80}Did Marina show up because the world needed to stop me for the sake of something more important?"
    ""

# game/script.rpy:947
translate french start_3ee476cc:

    # extend " {cps=80}Or did Marina show up because I subconsciously wished for something, for anything to stop me?"
    extend ""

# game/script.rpy:948
translate french start_88c79c79:

    # "{cps=80}Whatever it was, I guess I don’t mind this after all."
    ""

# game/script.rpy:954
translate french start_0851bf71:

    # "Hm..."
    ""

# game/script.rpy:955
translate french start_3376fff9:

    # "I think I’ll stick to the grander narrative angle for the time being."
    ""

# game/script.rpy:956
translate french start_c023596b:

    # extend " The world bending itself to the will of some worthless gnat is a preposterous idea."
    extend ""

# game/script.rpy:957
translate french start_dfcecac3:

    # "But it wouldn’t be the first time for me, would it?"
    ""

# game/script.rpy:958
translate french start_2151481a:

    # "And the fact that the world, for any reason, has decided to guide me towards the right path..."
    ""

# game/script.rpy:959
translate french start_742abd3e:

    # extend " That’s so endlessly sweet."
    extend ""

# game/script.rpy:961
translate french start_0b4c476e:

    # "Down the stairs, to the lobby, to the coatroom."
    ""

# game/script.rpy:962
translate french start_44d1f5d3:

    # "I don’t resist anymore."
    ""

# game/script.rpy:963
translate french start_0c4e8a18:

    # extend " Marina drags me along, and I can feel my doubt turning to excitement."
    extend ""

# game/script.rpy:964
translate french start_b7bada14:

    # "This is definitely the right path."
    ""

# game/script.rpy:965
translate french start_0d19b88d:

    # extend " \nThis girl knows about Ira."
    extend ""

# game/script.rpy:966
translate french start_c73d37fd:

    # extend " \nI want to know more about Ira, too."
    extend ""

# game/script.rpy:967
translate french start_ddcfe061:

    # "The whole wide world wants me to know."
    ""
