class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other: 'Cell') -> 'Cell':
        return Cell(self.count + other.count)

    def __sub__(self, other: 'Cell') -> 'Cell':
        if self.count > other.count:
            return Cell(self.count - other.count)
        else:
            print(f'{self.count} - {other.count}: Разность меньше нуля')

    def __mul__(self, other: 'Cell') -> 'Cell':
        return Cell(self.count * other.count)

    def __truediv__(self, other: 'Cell') -> 'Cell':
        return Cell(self.count // other.count)

    def make_order(self, num_cells: int):
        num_rows, remainder = self.count // num_cells, self.count % num_cells
        return '\n'.join(['*' * num_cells] * num_rows + (['*' * remainder] if remainder else []))

    def __str__(self):
        return f'Количество ячеек клетки: {self.count}'


if __name__ == '__main__':
    cell_1 = Cell(15)
    print(cell_1)
    cell_2 = Cell(10)
    print(cell_2)

    print(f'Сложение: {cell_1 + cell_2}')
    print(f'Вычитание: {cell_1 - cell_2}')
    print(f'Вычитание: {cell_2 - cell_1}')
    print(f'Вычитание: {cell_2 - cell_2}')
    print(f'Умножение: {cell_1 * cell_2}')
    print(f'Деление: {cell_1 / cell_2}')
    print(f'Ячейки по рядам:\n{(cell_1 * cell_2).make_order(23)}')
