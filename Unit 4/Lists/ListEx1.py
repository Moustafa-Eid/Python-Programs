import random
names = ['Christopher','James','Zubin','Timothy','Palmer']
actions = ['hates','kills','bullied','despises','befriends']
random = [random.randint(0,4),random.randint(0,4),random.randint(0,4)]

print ("%s %s %s." % (names[random[0]],actions[random[1]],names[random[2]]))