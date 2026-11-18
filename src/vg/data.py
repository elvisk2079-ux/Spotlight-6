# -*- coding: utf-8 -*-
"""Grade-6 irregular verbs (Spotlight 6) grouped by the shape of the three forms.

33 verbs from Elena's grade-6 table, split into four groups:
  A-A-A  all three forms the same
  A-B-A  V3 = V1
  A-B-B  V2 = V3  (the big one)
  A-B-C  all three different

Verb tuple: (V1, V2, V3, ipa1, ipa2, ipa3, перевод,
             sentence (Past Simple, target form in *asterisks*), перевод предложения)
Only Past Simple is used in the sentences — this is grade 6, not ОГЭ.
Forms with alternatives are written "learnt/learned" (first = main, BrE).
In stories the gaps are written [[base|answer]], answer = V2 (Past Simple).
"""

SAY = {  # overrides where the speech synth reads the spelling wrongly
    "read": ("reed", "red", "red"),
}

GROUPS = [
 dict(
  id="01", pattern="A – A – A", example="put – put – put",
  title="Все три формы одинаковые",
  rule="Самая лёгкая группа: глагол совсем не меняется, <b>V1 = V2 = V3</b>. Это короткие слова на <b>-t</b> или <b>-d</b>.",
  tip="<b>read</b> пишется одинаково во всех трёх формах, а читается по-разному: [riːd] – [red] – [red].",
  verbs=[
   ("put","put","put","pʊt","pʊt","pʊt","класть, ставить",
    "I *put* my books on the desk last night.","Вчера вечером я положил книги на стол."),
   ("set","set","set","set","set","set","ставить, накрывать",
    "Mum *set* the table before dinner yesterday.","Вчера мама накрыла на стол перед ужином."),
   ("let","let","let","let","let","let","разрешать, позволять",
    "Dad *let* me watch a film last Saturday.","В прошлую субботу папа разрешил мне посмотреть фильм."),
   ("read","read","read","riːd","red","red","читать",
    "I *read* a funny book last weekend.","В прошлые выходные я прочитал весёлую книжку."),
  ],
  story_title="A Rainy Saturday",
  story="Last Saturday it rained all day. Mum [[set|set]] the table for breakfast and Dad [[let|let]] us stay at home. I [[read|read]] a funny book about pirates, and then I [[put|put]] it back on the shelf. It was a quiet, cosy day.",
 ),
 dict(
  id="02", pattern="A – B – A", example="run – ran – run",
  title="Первая и третья форма одинаковые",
  rule="В прошедшем времени (<b>V2</b>) гласная меняется, а третья форма снова как первая: <b>V3 = V1</b>.",
  tip="<b>become</b> = be + <b>come</b>, поэтому became – become, как come – came – come.",
  verbs=[
   ("run","ran","run","rʌn","ræn","rʌn","бежать, бегать",
    "Jack *ran* to school because he was late.","Джек бежал в школу, потому что опаздывал."),
   ("become","became","become","bɪˈkʌm","bɪˈkeɪm","bɪˈkʌm","становиться",
    "Last night it *became* very cold.","Вчера ночью стало очень холодно."),
  ],
  story_title="A Cold Evening",
  story="Yesterday the weather [[become|became]] very cold. After the match the boys [[run|ran]] all the way home to get warm.",
 ),
 dict(
  id="03", pattern="A – B – B", example="get – got – got",
  title="Вторая и третья форма одинаковые",
  rule="Самая большая группа: <b>V2 = V3</b>. Выучил вторую форму — знаешь сразу и третью. Внутри есть мини-семейки: <b>feel–felt, leave–left, mean–meant, learn–learnt</b> (короткий звук + t); <b>stand–stood, understand–understood</b>; <b>make–made, have–had, say–said</b>.",
  tip="<b>understand</b> = under + <b>stand</b>, поэтому understood, как stand – stood.",
  verbs=[
   ("get","got","got","ɡet","ɡɒt","ɡɒt","получать",
    "I *got* a new bike for my birthday last year.","В прошлом году я получил новый велосипед на день рождения."),
   ("make","made","made","meɪk","meɪd","meɪd","делать, готовить",
    "My sister *made* pancakes this morning.","Сегодня утром сестра приготовила блины."),
   ("have","had","had","hæv","hæd","hæd","иметь",
    "We *had* a great time at the zoo yesterday.","Вчера мы отлично провели время в зоопарке."),
   ("say","said","said","seɪ","sed","sed","говорить, сказать",
    "The teacher *said* “Good morning!” and smiled.","Учительница сказала «Доброе утро!» и улыбнулась."),
   ("tell","told","told","tel","təʊld","təʊld","рассказывать",
    "Granny *told* us a funny story last night.","Вчера вечером бабушка рассказала нам весёлую историю."),
   ("find","found","found","faɪnd","faʊnd","faʊnd","находить",
    "I *found* my lost keys under the sofa.","Я нашёл потерянные ключи под диваном."),
   ("hold","held","held","həʊld","held","held","держать",
    "The little girl *held* her mum's hand.","Девочка держала маму за руку."),
   ("sit","sat","sat","sɪt","sæt","sæt","сидеть",
    "We *sat* on the grass and had a picnic.","Мы сидели на траве и устроили пикник."),
   ("stand","stood","stood","stænd","stʊd","stʊd","стоять",
    "We *stood* in the queue for twenty minutes.","Мы стояли в очереди двадцать минут."),
   ("understand","understood","understood","ˌʌndəˈstænd","ˌʌndəˈstʊd","ˌʌndəˈstʊd","понимать",
    "I *understood* everything at the lesson.","Я понял всё на уроке."),
   ("think","thought","thought","θɪŋk","θɔːt","θɔːt","думать",
    "I *thought* the film was boring.","Я подумал, что фильм скучный."),
   ("feel","felt","felt","fiːl","felt","felt","чувствовать",
    "I *felt* very tired after the match.","После матча я чувствовал себя очень усталым."),
   ("leave","left","left","liːv","left","left","уходить, оставлять",
    "The bus *left* at eight o'clock.","Автобус ушёл в восемь часов."),
   ("mean","meant","meant","miːn","ment","ment","означать, значить",
    "The red light *meant* “stop”.","Красный свет означал «стоп»."),
   ("learn","learnt/learned","learnt/learned","lɜːn","lɜːnt","lɜːnt","учить, узнавать",
    "We *learnt* a lot of new words last week.","На прошлой неделе мы выучили много новых слов."),
  ],
  story_title="The School Trip",
  story="Last week our class [[have|had]] a school trip to the museum. On the bus Granny, our guide, [[tell|told]] us about old ships. At first I didn't [[understand|understood]] everything, but soon I [[feel|felt]] really interested. We [[stand|stood]] near a big model and [[think|thought]] about the sailors. I [[find|found]] a postcard in the shop and [[get|got]] it for my mum. In the end we all [[learn|learnt]] a lot, and the teacher [[say|said]] it was a wonderful day.",
 ),
 dict(
  id="04", pattern="A – B – C", example="write – wrote – written",
  title="Все три формы разные",
  rule="Все три формы разные. Часто третья форма (<b>V3</b>) оканчивается на <b>-n</b> или <b>-en</b>: take<b>n</b>, give<b>n</b>, broke<b>n</b>, writt<b>en</b>, know<b>n</b>, show<b>n</b>.",
  tip="<b>be</b> — самый особенный: в прошедшем времени <b>was</b> (я, он, она, оно) и <b>were</b> (ты, мы, вы, они).",
  verbs=[
   ("be","was/were","been","biː","wɒz","biːn","быть",
    "Yesterday the weather *was* sunny and warm.","Вчера погода была солнечной и тёплой."),
   ("do","did","done","duː","dɪd","dʌn","делать",
    "I *did* my homework after school.","После школы я сделал домашнюю работу."),
   ("go","went","gone","ɡəʊ","went","ɡɒn","идти, ехать",
    "We *went* to the cinema last Saturday.","В прошлую субботу мы ходили в кино."),
   ("see","saw","seen","siː","sɔː","siːn","видеть",
    "I *saw* a funny film last Sunday.","В прошлое воскресенье я посмотрел весёлый фильм."),
   ("take","took","taken","teɪk","tʊk","ˈteɪkən","брать",
    "We *took* a lot of photos on holiday.","На каникулах мы сделали много фотографий."),
   ("give","gave","given","ɡɪv","ɡeɪv","ˈɡɪvən","давать, дарить",
    "My friends *gave* me a nice present.","Друзья подарили мне хороший подарок."),
   ("know","knew","known","nəʊ","njuː","nəʊn","знать",
    "I *knew* the answer to the question.","Я знал ответ на вопрос."),
   ("break","broke","broken","breɪk","brəʊk","ˈbrəʊkən","ломать, разбивать",
    "Oops! I *broke* a cup this morning.","Ой! Сегодня утром я разбил чашку."),
   ("speak","spoke","spoken","spiːk","spəʊk","ˈspəʊkən","говорить (на языке)",
    "We *spoke* English all day at camp.","В лагере мы весь день говорили по-английски."),
   ("show","showed","shown","ʃəʊ","ʃəʊd","ʃəʊn","показывать",
    "My friend *showed* me his new bike.","Друг показал мне свой новый велосипед."),
   ("begin","began","begun","bɪˈɡɪn","bɪˈɡæn","bɪˈɡʌn","начинать(ся)",
    "The lesson *began* at nine o'clock.","Урок начался в девять часов."),
   ("write","wrote","written","raɪt","rəʊt","ˈrɪtən","писать",
    "Anna *wrote* a letter to her pen friend.","Аня написала письмо другу по переписке."),
  ],
  story_title="My Best Weekend",
  story="Last weekend was wonderful. On Saturday we [[go|went]] to the park and I [[see|saw]] my old friend there. We [[take|took]] funny photos and I [[give|gave]] him a small gift. In the evening my grandad [[show|showed]] me his old album. On Sunday the rain [[begin|began]] early, so I stayed at home, [[do|did]] my homework and [[write|wrote]] a story about dragons. It [[be|was]] a quiet but happy day.",
 ),
]

# "Все глаголы" page — all 33 verbs together, with a mixed Past Simple story.
ALL = dict(
  id="all", pattern="Все глаголы", example="33 глагола вместе",
  title="Все неправильные глаголы вместе",
  rule="Все <b>33</b> глагола из нашей таблицы в одном месте. Формы перемешаны — проверь, помнишь ли ты их без подсказки группы.",
  tip="Если глагол даётся трудно — вернись в его группу и потренируй отдельно, а потом снова приходи сюда.",
  story_title="One Busy Day",
  story="Yesterday was a busy day. In the morning I [[get|got]] up early, [[have|had]] breakfast and [[go|went]] to school. The lesson [[begin|began]] at nine. The teacher [[tell|told]] us a story and [[say|said]] a new rule, and at last I [[understand|understood]] it. At break my friend [[show|showed]] me a photo and I [[see|saw]] a funny cat on it. After school I [[do|did]] my homework, [[read|read]] a book and [[write|wrote]] a letter to my grandma. In the evening it [[become|became]] cold, so I [[put|put]] on a warm jumper and [[feel|felt]] happy and sleepy.",
)

