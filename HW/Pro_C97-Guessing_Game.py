# NO, there isn't any sneaky virus in this code.
# All you have to do is download the file and run it in your command line interpreter (like Powershell).
# If you don't know what that means, it's recommended that you don't download this file.

import time, random

again = True
num = random.randint(1, 200)
turns = 0
while again == True:
  try:
    inp = int(input("\nGuess my number! It is somewhere from 1 to 200:  "))
    if inp == num:
      print("You WON in just", str(turns), "turns!")
      while True:
        time.sleep(1)
        a = input("\nPlay again? (Y/N): ")
        if a == "N" or a == "No" or a == "n" or a == "no":
          print("Thanks for playing!")
          again = False
          time.sleep(2)
          break
        elif a == "Y" or a=="Yes" or a == "y" or a == "yes":
          print("Starting new game...")
          turns = 0
          num = random.randint(1, 20)
          time.sleep(3)
          break
        else:
          print("Invalid: Enter Yes/No, or Y/N.")
    elif inp > num:
      print("No, my number is smaller than", inp)
      turns = turns + 1
      time.sleep(2)
    elif inp < num:
      print("No, my number is larger than", inp)
      turns = turns + 1
      time.sleep(2)
  except:
    print("Enter a valid number!")
    turns = turns + 1
    time.sleep(2)
