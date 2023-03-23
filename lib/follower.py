from .bloodoath import BloodOath

class Follower:
    
    all = []

    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        Follower.all.append(self)

    @property
    def cults(self):
        return [b.cult for b in BloodOath.all if b.follower == self]

    def join_cult(self, date, cult_inst):
        BloodOath(date, cult_inst, self )
    
    @classmethod
    def of_a_certain_age(cls, integer):
        return [f for f in cls.all if f.age > integer]
