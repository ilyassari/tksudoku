

from models import *
from views import root

# global sudo  mainwindow a taşıdım
# sudo = Cell.create_cells() #sözlük yapısı döner
# print(sudo)
# print(type(sudo))
# print(sudo['cells'])

# Cell.check_cells(sudo[cells])
'''
for cell in sudo['cells']:
    cell.find_value()
'''

''' terminale değerleri yazdırma
for i in range(1,9):
    for j in range(1,9):
        print((sudo['cells'][i*9+j]), end=' ')
    print()
'''

root.mainloop()  #ana ekranı çalıştır
# entry.mainloop()
