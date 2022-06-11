def num_translate(key):
    """переводит числительные от 0 до 10 c английского на русский язык"""
    lange = {"zero": "ноль", "one": "один", "two": "два", "free": "три",
             "four": "четыре", "five": "пять", "six": "шесть", "seven": "семь",
             "eight": "восемь", "nine": "девять", "ten": "десять"}
    if key in lange:
        mean = lange.get(key)
    else:
        mean = None
    print(f'"{mean}"')


num_translate("nine")
