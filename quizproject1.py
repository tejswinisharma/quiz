print("Welcome to my computer quiz")

playing = input("do you want play? ")
score =0
if playing.lower() != "yes":
    quit()
print("So lets play!")
answer = input(" Who was the first Indian woman to become a pilot? ")
if answer.lower() =="captain prem mathur":
     print("correct")
     score = score+1
else:
     print("incorrect")
answer = input("Who was the first Indian to become the president of the UN General Assembly? ")
if answer.lower() =="vijaya lakshmi pandit":
     print("correct")
     score = score+1
else:
     print("incorrect")
answer = input(" Which language was thought to be spoken by Buddha?  ")
if answer.lower() =="pali":
     print("correct")
     score = score+1
else:
     print("incorrect")
     answer = input(" Who is known as the missile woman of India? ")
if answer.lower() =="tessy thomas":
     print("correct")
     score = score+1
else:
     print("incorrect")
answer = input(" Who was the first Indian woman to win the Ashoka Chakra? ")
if answer.lower() =="neerja bhanot":
     print("correct")
     score = score+1
else:
     print("incorrect")
print("You got" + str(score)+"score")
print("you got" + str((score/4)*100) +"%")
