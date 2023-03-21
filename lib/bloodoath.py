class BloodOath:
    
    all = []

    def __init__(self, date, cult, follower):
        self.initiation_date = date
        self.follower = follower
        self.cult = cult
        BloodOath.all.append(self)