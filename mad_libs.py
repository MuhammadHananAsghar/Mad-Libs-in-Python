# Mad Libs In Python By Muhammad Hanan Asghar
import time
print("-------------------------------")
print("     The Magic Computers       ")
print("-------------------------------")
print("")
story = [
         "Today, every student has a computer small enough to fit into his {}. ",
         "He can solve any math problem by simply pushing the computer's little {}. ",
         "Computer can add, multiply, divide and {}. ",
         "They can also {} better than a human. ",
         "Some computer's are {}. ",
         "Others have a/an {} seen that shows all kinds of {} and {} figures."
]
inp = input("[*] Start Game (s) : ")
if inp == "s":
  print("Starting.....")
  time.sleep(1)
  noun = input("[+] Enter Noun : ")
  pluralnoun = input("[+] Enter Plural Noun : ")
  verbone = input("[+] Enter Verb(PRESENT TENSE) : ")
  verbtwo = input("[+] Enter Verb(PRESENT TENSE) : ")
  partofbody = input("[+] Enter Part of Body (PLURAL) : ")
  adjective = input("[+] Enter Adjective : ")
  pluralnountwo = input("[+] Enter Plural Noun : ")
  adjectivetwo = input("[+] Enter Adjective : ")
  one = story[0].format(noun)
  two = story[1].format(pluralnoun)
  three = story[2].format(verbone)
  four = story[3].format(verbtwo)
  five = story[4].format(partofbody)
  six = story[5].format(adjective,pluralnountwo,adjectivetwo)
  story = [i for i in [one,two,three,four,five,six]]
  story = "\n".join(story)
  print("")
  print("-------------------------------")
  print("     The Magic Computers       ")
  print("-------------------------------")
  print("")
  print(story)
  print("")
else:
  print("Enter Correct Character")
