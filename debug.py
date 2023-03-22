import ipdb
from lib import *

# test your code here
# e.g.

# f1 = Follower( 'Emiley', 31, 'Living the Dream' )
c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )
c2 = Cult('The Little Stinkers', 'Vermont', 1945, 'Help' )
c3 = Cult("Watchtower Society", "New York", 1888, "To fear God is not to")

f1 = Follower('Bryn', 27, 'May I ask a question?' )
f2 = Follower( 'Emiley', 31, 'Living the Dream' )
f3 = Follower('Kimberly', 31, 'Just do it')

b1 = BloodOath('1999-10-31', c1, f1)
b2 = BloodOath('2004-04-27', c1, f2)
b3 = BloodOath('2005-04-27', c2, f2)








print( "Mwahahaha!" )
ipdb.set_trace()