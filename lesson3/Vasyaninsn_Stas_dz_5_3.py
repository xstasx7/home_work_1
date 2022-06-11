from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag=True):
    """
    Возвращает n шуток, сформированных из трех случайных
    слов, взятых из трёх списков (по одному из каждого)
    :param n: number of jokes
    :param flag: True(repeat jokes); False(don't repeat jokes)
    :return: list[str]
    """
    for i in range(n):
        random_nouns = choice(nouns)
        random_adverbs = choice(adverbs)
        random_adjectives = choice(adjectives)
        jokes = f"{random_nouns} {random_adverbs} {random_adjectives}"
        if flag == False:
            jokes_d_rep = jokes.split()
            for a in nouns:
                for fun_a in jokes_d_rep:
                    if a == fun_a:
                        nouns.remove(a)

            for b in adverbs:
                for fun_b in jokes_d_rep:
                    if b == fun_b:
                        adverbs.remove(b)

            for c in adjectives:
                for fun_c in jokes_d_rep:
                    if c == fun_c:
                        adjectives.remove(c)
            print(jokes_d_rep)
        elif flag == True:
            jokes_rep = jokes.split()
            print(jokes_rep)


get_jokes(n=3, flag=False)
