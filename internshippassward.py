import random
import string
print("PASSWORD GENERATION")
type=int(input("enter the type of password:-\nPress 1 for digits\nPress 2 for characters\nPress 3 for charcters + digits\nPress 4 for digits + charcters + puntuation"))
length=int(input("Enter the length of your password"))
password=''

def digit():
   global length,password
   while(length>0): 
     a=random.randint(0,9)
     password+=str(a)
     length-=1
   print("Generated password:-",password)

def char():
   global length,password
   while(length>0):
      a=random.choice("abcdefghijklmnopqrstuvwxyz")
      password+=a
      length-=1
   print("Generated password:-",password)
def chardig():
   global length,password
   while(length>0):
      a=random.choice(string.ascii_letters + string.digits)
      password+=a
      length-=1
   print("Generated password:-",password)
def chardigpun():
   global length,password
   while(length>0):
      a=random.choice(string.ascii_letters + string.digits + string.punctuation)
      password+=a
      length-=1
   print("Generated password:-",password)
if(type==1):
    digit()
elif(type==2):
   char()
elif(type==3):
   chardig()
elif(type==4):
   chardigpun()
else:
   print("Please enter a valid type!")