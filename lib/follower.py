from .bloodoath import BloodOath

class Follower:
    
    all = []

    def __init__(self, name, age, string):
        self.name = name
        self.age = age
        self.life_motto = string
        Follower.all.append(self)

    @property
    def oaths(self):
        return [o for o in BloodOath.all if o.follower == self]
    
    @property
    def cults(self):
        return [o.cult for o in self.oaths]
    

    def join_cult(self, cult_inst, date = '2023-03-22'):
        return BloodOath(date, cult_inst, self)
    
    @classmethod
    def of_a_certain_age(cls, age):
        return [f for f in Follower.all if f.age >= age]

    @property
    def my_cults_slogans(self):
        for c in self.cults:
            print(c.slogan)
    
    @classmethod
    def most_active(cls):
        most_cults = 0
        found_follower = ''
        for f in cls.all:
            if len(f.cults) > most_cults:
                most_cults = len(f.cults)
                found_follower = f.name
        return found_follower

            

    
    @classmethod
    def top_ten():
        pass
