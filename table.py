from prettytable import PrettyTable

from proyekt.data import dt

x= PrettyTable()

x.field_names = ['Найменування товарної групи', 'Рік', 
'Товарообіг, тис.крб.(План)', 'Товарообіг, тис.крб.(Очіковане виконання)',
'Торгова скидка, %', 'Валовий доход, тис.крб.(План)', 'Валовий доход, тис.крб.(Очіковане виконання)']

for i in range(0, len(dt)):
    x.add_row([dt[i]])

def opentable():
    print('\nАНАЛІЗ ЗМІНИ ЦІН')
    print(x)