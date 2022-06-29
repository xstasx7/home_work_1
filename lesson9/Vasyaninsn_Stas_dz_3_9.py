class Worker:
    """Класс 'Worker'"""

    __income = {
        'wage': 150000,
        'bonus%': 25
    }

    def __init__(self, name, surname, position):
        print('__Экземпляр класса "Worker" создан__')
        self.name = name
        self.surname = surname
        self.position = position
        self.income = self.__income


class Position(Worker):
    """Дочерний класс 'Position' наследован от 'Worker'"""

    def get_full_name(self):
        print(f'Имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f"Доход в месяц {self.income['wage']}$ + премия {self.income['wage']//100*25}$")


if __name__ == '__main__':
    stas = Position('Stanislav', 'Vasyanin', 'Director of directions')
    stas.get_full_name()
    stas.get_total_income()
    print(f'{stas.name} is {stas.position}')
