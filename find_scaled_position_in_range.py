import getDetectorMatrix
import Methods as methods
from numpy import loadtxt, sum
from os.path import join, exists

# метод находит позицию с наилучшим паараметром 
# параметры:
#   start_position: начальная позици
#   end_positon:    конечная позиция
#   path:           путь до папки с файлами для обработки
#   data_format:    формат файлов которые используем
#
#
# возращает позицию

def find_scaled_position_in_range(start_position, end_positon, path, data_format):

    spectre_fileName = "{}" + data_format
    path_fileName = join(path, spectre_fileName)
    method_ansers = []
    n = 0
    while(exists(path_fileName.format(n))):
        file = open(path_fileName.format(n))
        mass = loadtxt(file)
        file.close()
        getDetectorMatrix.spectrum_preparation(mass)
        mass = sum(mass, 0).dot(1 / len(mass))
        
        # вычисление парметра 
        method_ansers.append(methods.integral_method(mass))
        n += 1

    result = method_ansers.index(max(method_ansers))
    result = start_position + result * ((end_positon - start_position) / n)
    return result


