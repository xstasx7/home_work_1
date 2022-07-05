
import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        a = ''
        for i in range(len(self.matrix)):
            a = a + '\t'.join(map(str, self.matrix[i])) + '\n\t'
        return f"\t{a}\t"

    def __add__(self, other):
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


if __name__ == '__main__':
    m1 = [[1, 2], [3, 4], [5, 6]]
    m2 = [[11, 21, 41], [-3, 41, -5], [51, -1, 61]]
    m3 = [[11, 21], [-31, 41], [51, 61], [25, 26]]
    e = Matrix(m1)
    b = Matrix(m2)
    c = Matrix(m3)

    print(e)
    print(b)
    print(c)

    d = e + b
    print('\td')
    print(d)
    print(type(d))
