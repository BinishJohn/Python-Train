for element in range(1, 10):
   print element

i = 0

while( i < 10 ):
   print i
   i +=1

states = { "KA" : "Karnataka" , "KL" : "Kerala" , "TN" : "Tamilnadu" ,"AP" : "Andrapredesh" , "UP" : "Utterpredesh" }

print states["KA"]

for abbrev , state in states.items():
  print abbrev , state

print states.get("KL")
print states.get("KK" ,"Abbrevation KK not available")

