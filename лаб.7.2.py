import numpy as np
import matplotlib.pyplot as plt
import pylab


text = str(input("Народився бог на санях в лемківськім містечку Дуклі.Прийшли лемки у крисанях і принесли місяць круглий. Ніч у сніговій завії крутиться довкола стріх. У долоні у Марії місяць — золотий горіх"))

def count_letters():
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і','ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',]

    for i in range(0, len(alphabet)):
        xdata = [alphabet[i]]
        ydata = [text.count(alphabet[i])]
        pylab.bar(xdata, ydata)
    pylab.show()
count_letters()