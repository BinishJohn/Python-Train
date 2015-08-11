import random

months = ['jan','feb','march','april','may','june','july']
for index,month in enumerate(months):
  print index , " : " , month
print "Shuffling : "
random.shuffle(months)
for index,month in enumerate(months):
  print index , " : " , month

print "Choice :" + str(random.choice(months))
print "Sample :" + str(random.sample(months,2))
print "Random Interger : " + str(random.randint(1,10))
print "Random Even Integer : " + str(random.randrange(0,101,2))
