from .bloodoath import BloodOath

class Cult:
    
    all = []

    def __init__(self, name, location, fy, slogan):
        self.name = name
        self.location = location
        self.fy = fy
        self.slogan = slogan
        Cult.all.append(self)
    
    def recruit_follower(self, follower, date):
        BloodOath(date, self, follower)

    @property
    def cult_followers(self):
        return [b.follower for b in BloodOath.all if b.cult == self]
    
    @property
    def oaths(self):
        return [b for b in BloodOath.all if b.cult == self]

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
    

    @property
    def average_age(self):
        total = 0
        for f in self.cult_followers:
            total += f.age
        return total / len(self.cult_followers)
    
    @property
    def my_followers_mottos(self):
        for f in self.cult_followers:
            print(f.life_motto)

    @classmethod
    def least_popular(cls):
        least_followers = 99999
        unpop_cult = ''
        for b in BloodOath.all:
            if b.cult.cult_population <= least_followers:
                least_followers = b.cult.cult_population
                unpop_cult = b.cult
        return unpop_cult.name
    
    @classmethod
    def most_common_location(cls):
        pass