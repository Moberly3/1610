# Naprogramujte třídu, která reprezentuje láhev a která má:
# 1 vlastnost kapacity v litrech a vlastnost, která určuje objem kapaliny v lahvi opět v litrech.
# 2 konstruktor, který umožní nastavit kapacitu lahve a nastaví, že je lahev prázdná.
# 3 metody, která umožní nastavit i získat objem v litrech tak, aby nikdy objem kapaliny v lahvi nepřekročil její kapacitu.
# 4 metodu pro vyprázdnění obsahu láhve.
# 5 metody, která umožní nastavit i získat objem kapaliny v mililitrech tak, aby nikdy objem kapaliny v lahvi nepřekročil její kapacitu.
# 6 mechanismus uzavření láhve tak, aby láhev mohla být ve dvou stavech: zavřená a otevřená.
# Ve stavu zavřená nelze měnit objem kapaliny ani láhev vyprázdnit a ve stavu otevřená to možné je.
# Nezapomeňte upravit předchozí metody tak, aby zohledňovali stav.


class Bottle:
    def __init__(self, capacity: float):
        self.capacity = capacity
        self.inside = 1
        self.is_open = True
        self.is_ml = True

    def get_empty(self):
         if self.is_open:
            self.inside = 0
            return self.inside

    def check_if_fits(self, inside):
        if self.capacity >= inside:
            self.inside = inside
            return self.inside
        else:
            return

    def get_to_ml(self):
        if self.is_ml:
            self.capacity * 1000
            self.inside * 1000
            return self.capacity, self.inside

    def get_close(self):
        if self.is_open:
            self.is_open = False
            return self.is_open
        else:
            self.is_open = True
            return self.is_open

Bottle1 = Bottle(1.0)
Bottle1.check_if_fits(2.0)
Bottle1.is_open()
Bottle1.get_empty()
Bottle1.get_to_ml()

