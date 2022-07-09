class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)


    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i.isdigit():
                b = i.zfill(2)
                my_date.append(b)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Все нормально'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


if __name__ == '__main__':
    days = Data('30 - 11 - 2022')
    print(days)
    print(Data.valid(11, 11, 2022))
    print(days.valid(11, 13, 2011))
    print(Data.extract('11 - 11 - 2011'))
    print(days.extract('11 - 11 - 2020'))
    print(Data.valid(1, 11, 2000))
    print(type(days))
