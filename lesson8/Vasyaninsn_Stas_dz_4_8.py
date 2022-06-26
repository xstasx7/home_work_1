def val_checker(c):
    def _val_checker(func):
        def wrapper(*args):
            global num
            try:
                for num in args:
                    if num < 1:
                        raise ValueError
            except ValueError:
                return print(f'ValueError: wrong val {num}')
            return func(num)
        return wrapper
    return _val_checker


@val_checker(lambda c: c > 0)
def calc_cube(d):
    return d ** 3


if __name__ == '__main__':
    a = calc_cube(5)
    print(a)
    b = calc_cube(-5)
    print(b)


