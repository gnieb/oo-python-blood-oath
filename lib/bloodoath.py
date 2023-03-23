class BloodOath:
    
    all = []

    def __init__(self, date, c_inst, f_inst):
        self.date = date
        self.cult = c_inst
        self.follower = f_inst
        BloodOath.all.append(self)

    @classmethod
    def first_oath(cls):
        earliest = 9999
        first_oath_f = ''
        for b in cls.all:
            if int(b.date) < earliest:
                earliest = b.date
                first_oath_f = b.follower
        return first_oath_f
        