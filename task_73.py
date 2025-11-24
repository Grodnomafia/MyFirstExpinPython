class Water:
   def __add__(self, other):
       if isinstance(other, Air):
           return Storm()
       elif isinstance(other, Fire):
           return Steam()
       elif isinstance(other, Earth):
           return Dirt()
class  Air:
    def __str__(self):
        return 'Воздух'
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        if isinstance(other,Fire):
            return Lighting()
        if isinstance(other,Earth):
            return Dust()


class Earth:
    def __add__(self, other):
        if isinstance(other, Air):
            return Lava()


class Fire:
    def __str__(self):
        return 'Огонь'
    def __add__(self, other):
        if isinstance(other,Earth):
            return Lava()
        if isinstance(other,Air):
            return Lighting()


class Storm:
    def __add__(self, other):
        if isinstance(other,Dirt):
            return Dust()
    def __str__(self):
        return 'Шторм'

class Steam:
    def __add__(self, other):
        if isinstance(other, Lighting):
            return Air()
    def __str__(self):
        return 'Пар'
class Dirt:
    def __add__(self, other):
        if isinstance(other,Storm):
            return Dust()
    def __str__(self):
        return 'Грязь'

class Lighting:
    def __add__(self, other):
        if isinstance(other,Steam):
            return Air()
    def __str__(self):
        return 'Молния'

class Dust:

    def __str__(self):
        return 'Пыль'

class Lava:

    def __str__(self):
        return 'Лава'
# ● Вода + Воздух = Шторм;
# ● Вода + Огонь = Пар;
# ● Вода + Земля = Грязь;
# ● Воздух + Огонь = Молния;
# ● Воздух + Земля = Пыль;
# ● Огонь + Земля = Лава.

water1 = Water()
air1 = Air()
print(water1+air1)
steam1 = Steam()
light1 = Lighting()
print(steam1 + light1)
dirt1 = Dirt()
storm1 = Storm()
print(dirt1 + storm1)
