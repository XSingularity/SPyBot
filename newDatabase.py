import cPickle

myFollowers = []

#New database
with open('myFollowers.pickle', 'wb') as fWrite:
    cPickle.dump(myFollowers, fWrite)

with open('myFollowers.pickle', 'rb') as fLoad:
    newFollowers = cPickle.load(fLoad)

for z in newFollowers:
    print z
