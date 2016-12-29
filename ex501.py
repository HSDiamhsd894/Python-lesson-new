name= 'Zed A. Shaw'
age= 35 # not a lie
height= 74*2.54 # cm
weight= 180*0.45 # kg
eyes= 'Blue'
teeth= 'White'
hair= 'Bronw'
print "Let's talk about %r." % name
print "He's %r cm tall." % height
print "He's %r kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth
# this line is tricky, try to get it exactly right
print "If i add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)
