from .bloodoath import BloodOath

class Cult:
    
    all = []

    def __init__(self, name, location, fy, slogan):
        self.name = name
        self.location = location
        self.fy = fy
        self.slogan = slogan
        Cult.all.append(self)
    
    def recruit_follower(self, follower, date = '2023-03-23'):
        BloodOath(date, self, follower)

    @property
    def cult_followers(self):
        return [b.follower for b in BloodOath.all if b.cult == self]
    
    @property
    def cult_population(self):
        return len(self.cult_followers)

    @classmethod
    def find_by_name(cls, string):
        for c in cls.all:
            if c.name == string:
                return c
        
    @classmethod
    def find_by_location(cls, string):
        return [c for c in cls.all if c.location == string]
    
    @classmethod
    def find_by_founding_year(cls, number):
        return [c for c in cls.all if c.fy == number]