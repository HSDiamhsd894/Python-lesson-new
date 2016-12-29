from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you three questions about your love life."
print "Do you like Danny %s?" % user_name
likes = raw_input(prompt)

print "When did you know her %s?" % user_name
time = raw_input(prompt)

print "Do you want to marry her %s?" % user_name
marry = raw_input(prompt)

print "Why do you want to marry her %s?" % user_name
reason = raw_input(prompt)
print """
Alright, so you said %r about liking Danny.
You first met and knew her %r. That's been long enough to know a person.
And you said %r about marrying her. Hope she says yes to that.
The reason you gave about Q3 is %r.
""" % (likes, time, marry, reason )