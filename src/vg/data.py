# -*- coding: utf-8 -*-
"""Grade-6 irregular verbs (Spotlight 6) grouped by ONE sound alternation each,
the same way as the Irregular-verbs-groups trainer — not by the A-B-C shape.

33 verbs from Elena's grade-6 table. Each group = one kind of alternation
(e.g. [iː]→[e]; -ought; i–a–u; V3 = V1 + en …). Some groups have a single verb —
that's fine, just like 'find' or 'wear' stand alone in the big trainer.

Verb tuple (11 fields):
  (V1, V2, V3, ipa1, ipa2, ipa3, перевод,
   sent1, tr1, sent2, tr2)
Two Past Simple sentences per verb (target form in *asterisks*) so the
"choose"/"fill" drills have ~2 items per verb (5 verbs → 10 sentences).
Only Past Simple is used — this is grade 6.
Forms with alternatives are written "learnt/learned" (first = main, BrE).
In stories the gaps are written [[base|answer]], answer = V2 (Past Simple).
A group gets a story only when it has 3+ verbs.
"""

SAY = {  # overrides where the speech synth reads the spelling wrongly
    "read": ("reed", "red", "red"),
}

GROUPS = [
 dict(
  id="01", pattern="A – A – A", example="put – put – put",
  title="Все три формы одинаковые",
  rule="Глагол совсем не меняется: <b>V1 = V2 = V3</b>. Обычно это короткие слова на <b>-t</b> или <b>-d</b>.",
  tip="<b>read</b> пишется одинаково во всех трёх формах, а читается по-разному: [riːd] – [red] – [red].",
  verbs=[
   ("put","put","put","pʊt","pʊt","pʊt","класть, ставить",
    "I *put* my books on the desk last night.","Вчера вечером я положил книги на стол.",
    "She *put* sugar in her tea this morning.","Сегодня утром она положила сахар в чай."),
   ("set","set","set","set","set","set","ставить, накрывать",
    "Mum *set* the table before dinner yesterday.","Вчера мама накрыла на стол перед ужином.",
    "The teacher *set* us easy homework on Friday.","В пятницу учитель задал нам лёгкое домашнее задание."),
   ("let","let","let","let","let","let","разрешать, позволять",
    "Dad *let* me watch a film last Saturday.","В прошлую субботу папа разрешил мне посмотреть фильм.",
    "Mum *let* us play outside after lunch.","После обеда мама разрешила нам поиграть на улице."),
   ("read","read","read","riːd","red","red","читать",
    "I *read* a funny book last weekend.","В прошлые выходные я прочитал весёлую книжку.",
    "We *read* an interesting text in class yesterday.","Вчера на уроке мы прочитали интересный текст."),
  ],
  story_title="A Rainy Saturday",
  story="Last Saturday it rained all day. Mum [[set|set]] the table for breakfast and Dad [[let|let]] us stay at home. I [[read|read]] a funny book about pirates, and then I [[put|put]] it back on the shelf. It was a quiet, cosy day.",
 ),
 dict(
  id="02", pattern="[iː] → [e]", example="feel – felt – felt",
  title="Долгий [iː] становится кратким [e]",
  rule="Долгий звук <b>[iː]</b> укорачивается до <b>[e]</b>, и в конце появляется <b>-t</b>. <b>V2 = V3</b>: feel → felt, leave → left, mean → meant.",
  tip="<b>meant</b> звучит [ment], коротко, а не [miːnt].",
  verbs=[
   ("feel","felt","felt","fiːl","felt","felt","чувствовать",
    "I *felt* very tired after the match.","После матча я чувствовал себя очень усталым.",
    "She *felt* happy when she won the game.","Она почувствовала себя счастливой, когда выиграла игру."),
   ("leave","left","left","liːv","left","left","уходить, оставлять",
    "The bus *left* at eight o'clock.","Автобус ушёл в восемь часов.",
    "We *left* home early in the morning.","Мы вышли из дома рано утром."),
   ("mean","meant","meant","miːn","ment","ment","означать, значить",
    "The red light *meant* “stop”.","Красный свет означал «стоп».",
    "I didn't know what the new word *meant*.","Я не знал, что означает новое слово."),
  ],
  story_title="A Tiring Monday",
  story="Last Monday I [[feel|felt]] very tired at school. After the last lesson my friends and I [[leave|left]] the building together. On the way home someone said a new English word, but I didn't know what it [[mean|meant]].",
 ),
 dict(
  id="03", pattern="→ [ɔːt]", example="think – thought – thought",
  title="Превращается в -ought [ɔːt]",
  rule="<b>V2 = V3</b> и оканчиваются на <b>-ought</b> [ɔːt]: think → thought. Так же меняются buy → bought, bring → brought, catch → caught.",
  tip="Буквы <b>-ough-</b> здесь читаются просто [ɔː], а <b>t</b> на конце — [t].",
  verbs=[
   ("think","thought","thought","θɪŋk","θɔːt","θɔːt","думать",
    "I *thought* the film was boring.","Я подумал, что фильм скучный.",
    "She *thought* about the answer for a minute.","Она думала над ответом минуту."),
  ],
 ),
 dict(
  id="04", pattern="-n → -t", example="learn – learnt – learnt",
  title="В конце появляется -t",
  rule="<b>V2 = V3</b>: к глаголу просто добавляется <b>-t</b>. learn → learnt. Так же: build → built, send → sent.",
  tip="В британском английском чаще <b>learnt</b>, в американском — <b>learned</b>. Оба варианта верные.",
  verbs=[
   ("learn","learnt/learned","learnt/learned","lɜːn","lɜːnt","lɜːnt","учить, узнавать",
    "We *learnt* a lot of new words last week.","На прошлой неделе мы выучили много новых слов.",
    "He *learnt* to ride a bike last summer.","Прошлым летом он научился кататься на велосипеде."),
  ],
 ),
 dict(
  id="05", pattern="-ind → -ound", example="find – found – found",
  title="-ind превращается в -ound",
  rule="Звук <b>[aɪ]</b> меняется на <b>[aʊ]</b>: f<b>ind</b> → f<b>ound</b>. <b>V2 = V3</b>.",
  tip="Запомни глазами: f<b>ind</b> → f<b>ound</b> → f<b>ound</b>.",
  verbs=[
   ("find","found","found","faɪnd","faʊnd","faʊnd","находить",
    "I *found* my lost keys under the sofa.","Я нашёл потерянные ключи под диваном.",
    "She *found* a nice shell on the beach.","Она нашла красивую ракушку на пляже."),
  ],
 ),
 dict(
  id="06", pattern="-ay/-ake → -aid/-ade", example="say – said – said",
  title="-ay / -ake превращается в -aid / -ade",
  rule="<b>V2 = V3</b>, гласная становится короткой: say → said, make → made.",
  tip="<b>said</b> читается [sed], а не [seɪd].",
  verbs=[
   ("say","said","said","seɪ","sed","sed","говорить, сказать",
    "The teacher *said* “Good morning!” and smiled.","Учительница сказала «Доброе утро!» и улыбнулась.",
    "He *said* goodbye and ran to the bus.","Он попрощался и побежал к автобусу."),
   ("make","made","made","meɪk","meɪd","meɪd","делать, готовить",
    "My sister *made* pancakes this morning.","Сегодня утром сестра приготовила блины.",
    "We *made* a snowman in the garden yesterday.","Вчера мы слепили снеговика в саду."),
  ],
 ),
 dict(
  id="07", pattern="A – B – B", example="get – got – got",
  title="Вторая и третья форма одинаковые (смешанные)",
  rule="Большая «смешанная» группа: <b>V2 = V3</b>, но у каждого глагола <b>своё</b> чередование — have → had, get → got, sit → sat, hold → held, tell → told, stand → stood, understand → understood.",
  tip="<b>understand</b> = under + <b>stand</b>, поэтому understood, как stand → stood.",
  verbs=[
   ("have","had","had","hæv","hæd","hæd","иметь",
    "We *had* a great time at the zoo yesterday.","Вчера мы отлично провели время в зоопарке.",
    "I *had* eggs for breakfast this morning.","Сегодня утром я ел яйца на завтрак."),
   ("get","got","got","ɡet","ɡɒt","ɡɒt","получать",
    "I *got* a new bike for my birthday last year.","В прошлом году я получил новый велосипед на день рождения.",
    "She *got* a good mark in the test yesterday.","Вчера она получила хорошую оценку за контрольную."),
   ("sit","sat","sat","sɪt","sæt","sæt","сидеть",
    "We *sat* on the grass and had a picnic.","Мы сидели на траве и устроили пикник.",
    "He *sat* next to me at the concert.","На концерте он сидел рядом со мной."),
   ("hold","held","held","həʊld","held","held","держать",
    "The little girl *held* her mum's hand.","Девочка держала маму за руку.",
    "He *held* the door open for me.","Он придержал для меня дверь."),
   ("tell","told","told","tel","təʊld","təʊld","рассказывать",
    "Granny *told* us a funny story last night.","Вчера вечером бабушка рассказала нам весёлую историю.",
    "The teacher *told* us to be quiet.","Учитель сказал нам вести себя тихо."),
   ("stand","stood","stood","stænd","stʊd","stʊd","стоять",
    "We *stood* in the queue for twenty minutes.","Мы стояли в очереди двадцать минут.",
    "A tall tree *stood* near our house.","Возле нашего дома стояло высокое дерево."),
   ("understand","understood","understood","ˌʌndəˈstænd","ˌʌndəˈstʊd","ˌʌndəˈstʊd","понимать",
    "I *understood* everything at the lesson.","Я понял всё на уроке.",
    "She *understood* the rule very quickly.","Она очень быстро поняла правило."),
  ],
  story_title="The School Concert",
  story="Last week we [[have|had]] a school concert. We [[get|got]] to the hall early and [[sit|sat]] in the front row. My little sister [[hold|held]] my hand because she was nervous. A teacher [[stand|stood]] on the stage and [[tell|told]] everyone the rules. At first I didn't [[understand|understood]] the words of the first song, but soon I really enjoyed it.",
 ),
 dict(
  id="08", pattern="A – B – A", example="run – ran – run",
  title="Третья форма возвращается к первой",
  rule="В Past Simple (<b>V2</b>) гласная меняется, а третья форма снова как первая: <b>V3 = V1</b>.",
  tip="<b>become</b> = be + <b>come</b>, поэтому became – become, как come – came – come.",
  verbs=[
   ("run","ran","run","rʌn","ræn","rʌn","бежать, бегать",
    "Jack *ran* to school because he was late.","Джек бежал в школу, потому что опаздывал.",
    "The dog *ran* after the ball in the park.","В парке собака бежала за мячом."),
   ("become","became","become","bɪˈkʌm","bɪˈkeɪm","bɪˈkʌm","становиться",
    "Last night it *became* very cold.","Вчера ночью стало очень холодно.",
    "The sky *became* dark before the storm.","Перед грозой небо стало тёмным."),
  ],
 ),
 dict(
  id="09", pattern="i – a – u", example="begin – began – begun",
  title="Музыкальная тройка i – a – u",
  rule="Гласная меняется по порядку: <b>i → a → u</b>. begin → began → begun. Так же: drink → drank → drunk, sing → sang → sung, swim → swam → swum.",
  tip="Три формы — три разные гласные: <b>i</b>, <b>a</b>, <b>u</b>.",
  verbs=[
   ("begin","began","begun","bɪˈɡɪn","bɪˈɡæn","bɪˈɡʌn","начинать(ся)",
    "The lesson *began* at nine o'clock.","Урок начался в девять часов.",
    "The film *began* when we sat down.","Фильм начался, когда мы сели."),
  ],
 ),
 dict(
  id="10", pattern="i – o – i + en", example="write – wrote – written",
  title="V2 с «o», V3 = V1 + en",
  rule="В <b>V2</b> появляется «o», а <b>V3</b> похожа на V1, но с <b>-en</b>: write → wrote → written. Так же: drive → drove → driven, ride → rode → ridden.",
  tip="В <b>written</b> две «t»: wri-<b>tt</b>-en.",
  verbs=[
   ("write","wrote","written","raɪt","rəʊt","ˈrɪtən","писать",
    "Anna *wrote* a letter to her pen friend.","Аня написала письмо другу по переписке.",
    "I *wrote* my name at the top of the page.","Я написал своё имя наверху страницы."),
  ],
 ),
 dict(
  id="11", pattern="-ew – -own", example="know – knew – known",
  title="V2 на -ew, V3 на -own",
  rule="<b>V2</b> оканчивается на <b>-ew</b> [uː], а <b>V3</b> на <b>-own</b>: know → knew → known. Так же: grow → grew → grown, throw → threw → thrown.",
  tip="В <b>knew</b> буква <b>k</b> не читается: [njuː].",
  verbs=[
   ("know","knew","known","nəʊ","njuː","nəʊn","знать",
    "I *knew* the answer to the question.","Я знал ответ на вопрос.",
    "She *knew* the way to the museum.","Она знала дорогу к музею."),
  ],
 ),
 dict(
  id="12", pattern="– o – o + en", example="speak – spoke – spoken",
  title="V2 с «o», V3 = V2 + en",
  rule="В <b>V2</b> появляется звук <b>[əʊ]</b> («o»), а <b>V3 = V2 + -en</b>: break → broke → broken, speak → spoke → spoken.",
  tip="Третью форму легко получить: просто добавь <b>-en</b> ко второй форме.",
  verbs=[
   ("break","broke","broken","breɪk","brəʊk","ˈbrəʊkən","ломать, разбивать",
    "Oops! I *broke* a cup this morning.","Ой! Сегодня утром я разбил чашку.",
    "He *broke* his pencil during the test.","Он сломал карандаш во время контрольной."),
   ("speak","spoke","spoken","spiːk","spəʊk","ˈspəʊkən","говорить (на языке)",
    "We *spoke* English all day at camp.","В лагере мы весь день говорили по-английски.",
    "The teacher *spoke* slowly and clearly.","Учитель говорил медленно и чётко."),
  ],
 ),
 dict(
  id="13", pattern="V3 = V1 + (e)n", example="take – took – taken",
  title="Третья форма = первая + -en",
  rule="<b>V2</b> у всех разная, а <b>V3</b> образуется из первой формы с <b>-n / -en</b>: take → took → taken, give → gave → given, see → saw → seen.",
  tip="Запомни хвостик <b>-n</b> в третьей форме: take<b>n</b>, give<b>n</b>, see<b>n</b>.",
  verbs=[
   ("take","took","taken","teɪk","tʊk","ˈteɪkən","брать",
    "We *took* a lot of photos on holiday.","На каникулах мы сделали много фотографий.",
    "She *took* an apple from the bowl.","Она взяла яблоко из вазы."),
   ("give","gave","given","ɡɪv","ɡeɪv","ˈɡɪvən","давать, дарить",
    "My friends *gave* me a nice present.","Друзья подарили мне хороший подарок.",
    "The waiter *gave* us the menu.","Официант дал нам меню."),
   ("see","saw","seen","siː","sɔː","siːn","видеть",
    "I *saw* a funny film last Sunday.","В прошлое воскресенье я посмотрел весёлый фильм.",
    "We *saw* a rainbow after the rain.","После дождя мы увидели радугу."),
  ],
  story_title="A Day with Friends",
  story="Last Sunday I [[see|saw]] all my friends at Tom's party. We [[take|took]] a lot of funny photos together. Before I went home, I [[give|gave]] Tom a small present for his birthday.",
 ),
 dict(
  id="14", pattern="Особые", example="go – went – gone",
  title="Глаголы-одиночки: учим целиком",
  rule="Эти глаголы ни на кого не похожи — их просто запоминаем: be → was/were → been, do → did → done, go → went → gone, show → showed → shown.",
  tip="<b>be</b> — самый особенный: в прошедшем <b>was</b> (я, он, она, оно) и <b>were</b> (ты, мы, вы, они).",
  verbs=[
   ("be","was/were","been","biː","wɒz","biːn","быть",
    "Yesterday the weather *was* sunny and warm.","Вчера погода была солнечной и тёплой.",
    "The children *were* happy at the party.","Дети были счастливы на празднике."),
   ("do","did","done","duː","dɪd","dʌn","делать",
    "I *did* my homework after school.","После школы я сделал домашнюю работу.",
    "She *did* the washing-up after dinner.","После ужина она помыла посуду."),
   ("go","went","gone","ɡəʊ","went","ɡɒn","идти, ехать",
    "We *went* to the cinema last Saturday.","В прошлую субботу мы ходили в кино.",
    "They *went* to the seaside in summer.","Летом они ездили на море."),
   ("show","showed","shown","ʃəʊ","ʃəʊd","ʃəʊn","показывать",
    "My friend *showed* me his new bike.","Друг показал мне свой новый велосипед.",
    "The guide *showed* us the old castle.","Экскурсовод показал нам старый замок."),
  ],
  story_title="A Busy Weekend",
  story="Last weekend [[be|was]] really busy. On Saturday I [[do|did]] all my homework in the morning. Then we [[go|went]] to the park, and there my friend [[show|showed]] me his new skateboard.",
 ),
]

# "Все глаголы" page — all 33 verbs together, with a mixed Past Simple story.
ALL = dict(
  id="all", pattern="Все глаголы", example="33 глагола вместе",
  title="Все неправильные глаголы вместе",
  rule="Все <b>33</b> глагола из нашей таблицы в одном месте. Чередования перемешаны — проверь, помнишь ли ты формы без подсказки группы.",
  tip="Если глагол даётся трудно — вернись в его группу и потренируй отдельно, а потом снова приходи сюда.",
  story_title="One Busy Day",
  story="Yesterday was a busy day. In the morning I [[get|got]] up early, [[have|had]] breakfast and [[go|went]] to school. The lesson [[begin|began]] at nine. The teacher [[tell|told]] us a story and [[say|said]] a new rule, and at last I [[understand|understood]] it. At break my friend [[show|showed]] me a photo and I [[see|saw]] a funny cat on it. After school I [[do|did]] my homework, [[read|read]] a book and [[write|wrote]] a letter to my grandma. In the evening it [[become|became]] cold, so I [[put|put]] on a warm jumper and [[feel|felt]] happy and sleepy.",
)
