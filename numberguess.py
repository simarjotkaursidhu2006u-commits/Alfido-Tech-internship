import random
print("     NUMBER GUESSING GAME     ")
while(True):
 start=str(input("Press enter to start the game"))
 if (start==""):
   n=random.randint(1,100)
   a=int(input("Guess the number"))
   if(a==n):
      print(f"Computer's number={n}")
      print(f"Your number={a}") 
      print("It's a match you won!!")
   else:
      print(f"Computer's number={n}")
      print(f"Your number={a}")
      print("Better luck next time!")
 else:
   print("Press Enter!!")