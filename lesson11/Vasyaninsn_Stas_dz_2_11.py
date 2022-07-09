class Division_Null:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except:
            return f"Деление на ноль NO"


if __name__ == '__main__':
    div = Division_Null(10, 100)
    print(Division_Null.divide_by_null(15, 0))
    print(Division_Null.divide_by_null(15, 7))
    print(div.divide_by_null(150, 0))

