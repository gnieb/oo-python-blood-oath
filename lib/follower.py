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

    @property
    def my_cults_slogans(self):
        for c in self.cults:
            print(c.slogan)

    @classmethod
    def most_active(cls):
        cult_count = 0
        most_cults = ''
        for b in BloodOath.all:
            if len(b.follower.cults) > cult_count:
                cult_count = len(b.follower.cults)
                most_cults = b.follower.name

        return most_cults
            
#####skip######
    @classmethod
    def top_ten(cls):
        pass        