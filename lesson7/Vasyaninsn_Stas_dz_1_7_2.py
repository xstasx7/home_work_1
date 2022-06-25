#   скрипт 'Vasyaninsn_Stas_dz_1_7_2' принимает название проекта из консоли и удаляет его
import os
import sys
import shutil

def delete_project():

    if os.path.exists(str(sys.argv[1])):
        shutil.rmtree(str(sys.argv[1]))

    return print('Удалил структуру проекта')


delete_project()
