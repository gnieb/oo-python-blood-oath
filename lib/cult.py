from .bloodoath import BloodOath

class Cult:
    
    all = []
    
    def __init__(self, name, city, founding_year, slogan):
        self.name = name
        self.city = city
        self.fy = founding_year
        self.slogan = slogan
        Cult.all.append(self)

    @property
    def oaths(self):
        return [o for o in BloodOath.all if o.cult == self]
    
    @property
    def followers(self):
        return [o.follower for o in self.oaths]

    def recruit_follower(self, follower, date = '2023-03-23'):
        return BloodOath(date, follower, self)
    
    @property
    def cult_population(self):
        return len(self.followers)
    
    @classmethod
    def find_by_name(cls, str):
        for c in Cult.all:
            if c.name == str:
                return c
            else:
                return None
            
    @classmethod
    def find_by_location(cls, city):
        return [c for c in Cult.all if c.city == city ]
    
    @classmethod
    def find_by_founding_year(cls, year):
        for c in Cult.all:
            if c.fy == year:
                return c
            else:
                return None
            
    @property
    def average_age(self):
        total = 0
        for c in Cult.all:
            total += c.age