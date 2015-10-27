import sys

import random


ans = True



while ans:
   question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")

   answers = random.randint(1,8)

   if question == "quit":
     sys.exit()

   if question == "Am I cool?":
     print "Naw"

   elif answers == 1:
       print "Leave me alone yi badger"

   elif answers == 2:
       print "Yo Momma"

   elif answers == 3:
       print "Don't ask me man, I only work here"

   elif answers == 4:
       print "I don't know, why are you asking me?"

   elif answers == 5:
       print "Stop messing with Korean Jesus"

   elif answers == 6:
       print "OMG go away, you're so clingy"

   elif answers == 7:
       print "IT'S JOHN CENAAAAAA"

   elif answers == 8:
       print "Ask me that again & I'll rip off your arm and batter yir maw wi it"