class Car:
    """ Родительский класс 'Сar' """

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'{self.name} топит {self.speed} км/ч')

    def look_police(self):
        if self.is_police:
            print(f'<<<<Шухер, драпаем отсюда!!!>>>>')
        else:
            print(f'Всё норм, это обычный {self.name}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=None):
        super().__init__(speed, color, name)
        self.is_police = is_police
        print(f'Объект {self.name} класса "TownCar" создан')

    def show_speed(self):
        print(f'Скорость {self.name} равна {self.speed}')
        if self.speed > 60:
            print(f'Внимание!!! Превышение скорости на {self.speed - 60} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=None):
        super().__init__(speed, color, name)
        self.is_police = is_police
        print(f'Объект {self.name} класса "SportCar" создан')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=None):
        super().__init__(speed, color, name)
        self.is_police = is_police
        print(f'Объект {self.name} класса "WorkCar" создан')

    def show_speed(self):
        print(f'Скорость {self.name} равна {self.speed}')
        if self.speed > 40:
            print(f'Внимание! Превышение скорости на {self.speed - 40} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police
        print('-->There the police!!!<--')


if __name__ == '__main__':
    opel_astra = TownCar(65, 'синий', 'opel')
    opel_astra.go()
    opel_astra.show_speed()
    opel_astra.turn('влево')
    opel_astra.stop()
    opel_astra.look_police()

    print('-'*50)

    lada = SportCar(170, 'sport_car', 'лада_седан')
    lada.go()
    lada.show_speed()
    lada.turn('влево')
    lada.stop()
    lada.look_police()

    print('-' * 50)

    reno = WorkCar(45, 'старый', 'logan')
    reno.go()
    reno.show_speed()
    reno.turn('со скрипом')
    reno.stop()
    reno.look_police()

    print('-' * 50)

    police = PoliceCar(90, 'спецмашина', 'патруль')
    police.go()
    police.show_speed()
    police.turn('на тебя')
    police.stop()
    police.look_police()

