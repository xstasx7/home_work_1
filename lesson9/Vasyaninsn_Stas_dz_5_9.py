class Stationery:
    """Родительский класс 'Stationery'"""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title
        print('---Объект ручка класса создан---')

    def draw(self):
        print(f'"{self.title}" - написано ручкой')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title
        print('---Объект карандаш класса создан---')

    def draw(self):
        print(f'"{self.title}" - написано карандашом')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title
        print('---Объект маркер класса создан---')

    def draw(self):
        print(f'"{self.title}" - написано маркером')


if __name__ == '__main__':
    pen = Pen('Пишу как хочу')
    pen.draw()

    print('_'*30)

    pencil = Pencil('Ничего не пойму')
    pencil.draw()

    print('_' * 30)

    handle = Handle('Может потом пойму, главное получается!!!')
    handle.draw()
