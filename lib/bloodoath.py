class BloodOath:
    
    all = []

    def __init__(self, date, c_inst, f_inst):
        self.date = date
        self.cult = c_inst
        self.follower = f_inst
        BloodOath.all.append(self)
        