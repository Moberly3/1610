# Oživte následující zdrojový kód, který reprezentuje jednoduchý systém vstupu do školní budovy
#
# d = Dvere(zamceno=True)
# try:
#     d.otevrit()
#     print("Prosel jsem")
# except ZamceneDvereException as e:
#     print("Dvere jsou zamcene, nemuzes je otevrit")
from exceptions import ZamceneDvereException
from Dvere import Dvere

d = Dvere(zamceno=True)
try:
    d.otevrit()
    print("Prosel jsem")
except ZamceneDvereException as e:
    print("Dvere jsou zamcene, nemuzes je otevrit")
finally:
    d.otevrit()





