def thesaurus(*name):
    """
    Принимает в качестве аргументов имена и возвращает словарь,
    в котором ключи — первые буквы имён, а значения — списки,
    содержащие имена, начинающиеся с соответствующей буквы
    :param name: name
    :return: dict(str : [list])
    """
    names = {}
    for i in name:
        key = i[0].capitalize()
        if key not in names:
            names[key] = []
        names[key].append(i)
    print(names)


thesaurus("Юля", "Наташа", 'Макс', "Аня", "Нина", "Маруся")
