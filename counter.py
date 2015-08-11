#Counter provided rapid library for tally

from collections import *

def occurence():
  cnt = Counter()
  print type(cnt)
  words = ['red','blue','red','white','blue','black','red','black','blue','red']
  for index , word in enumerate(words):
    print index , " : "  ,word
    cnt[word] = cnt[word] + 1
  print cnt
  print Counter(words).most_common(2)
  words_new = cnt.elements()
  for index, elem in enumerate(words_new):
     print index, " : " , elem 

if __name__ == '__main__' :
  occurence()

