import os
from pathlib import Path as P

def make_stat(any_directory):
    stat_of_folder = {
        100: 0,
        1000: 0,
        10000: 0,
        100000: 0
    }
    any_pth = P.cwd()

    for file in os.listdir(fr'{any_pth}\{any_directory}'):
        if os.stat(fr'{any_pth}\{any_directory}\{file}').st_size <= 100:
            stat_of_folder[100] += 1
        elif os.stat(fr'{any_pth}\{any_directory}\{file}').st_size <= 1000:
            stat_of_folder[1000] += 1
        elif os.stat(fr'{any_pth}\{any_directory}\{file}').st_size <= 10000:
            stat_of_folder[10000] += 1
        else:
            stat_of_folder[100000] += 1


    return stat_of_folder


if __name__ == '__main__':
    directory = input('Please enter directory: ')
    print(make_stat(directory))

