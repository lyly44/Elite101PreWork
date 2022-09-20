import random 
from random import randint

def greeting():
  print("Hello! My name is charles the chatter :) ")
  name = input("What's your name? ")
  print("It's a pleasure to meet you, " + name + "!")

def numberGame():
    userNum = input("choose a number from 1-100! ")
    userNumber = int(userNum)
    print("The objective of the game is to see whether my number or your number is larger!")
    whoWin = input("Do you think you'll beat me?? ")
    yesWin = {"Yes", "Why wouldn't I", "of course", "I'll win for sure", "Ye"}
    noWin = {"Nah", "No", "I don't think so", "I doubt it", "of course not"}

  # Use StackoverFlow to debug, the comparsion of an input to multiple possibilities. https://stackoverflow.com/questions/6838238/comparing-a-string-to-multiple-items-in-python
    if whoWin in yesWin: 
      print("\nYou're confident! I'm getting anxious to see who'll win :o")
  
    elif whoWin in noWin: 
      print("\nWhere's your confidence? Believe in yourself! ")
  
    else: 
      print("\nHmmm, let's see who'll win. ")
    
    chatNum = random.randint(1,100)
    if userNumber > chatNum: 
      print("While you chose your number, mine was " + str(chatNum))
      print("You won~ you just got lucky today :( ")
  
    elif userNumber < chatNum:
      print("While you chose your number, mine was " + str(chatNum))
      print("you lost! My luck is pretty good today :) ")
     
    elif userNumber == chatNum:
      print("While you chose your number, mine was " + str(chatNum))
      print("Wow! That's unbelieveable :o We chose the same number!! ")    


def buildProfile(): 
  print("let's get to know each other! I'll ask you a few questions, then summarize it at the end :) ")
  favMusic = input("what's your favorite song? ")
  print("Wow! I'll make sure to listen to " + favMusic)
  myfavSongs = ["Keshi-Angel", "Seventeen-bout you", "CIX-Wave", "Mj Apanay-Time machine(feat. Aren Park)"]
  print("My favorite song is " + random.choice(myfavSongs))
  favColor = input("What's your favorite color? ")
  print("Really? I love " + favColor + " too!")
  favlocation = input("Where would you want to visit one day?  " )
  print("Wow! I really wanna visit " + favlocation ) 
  print("\nIt was so nice to get to know you! I learned that your favorite location is " + favlocation + " as well as your favorite song which is " + favMusic + " and favorite color  is " + favColor)



greeting()
uc = " "
while uc != 3:
  userChoice = int(input("\nWould you like to play a number game(1), or build a profile(2) or stop talking to me (3)? "))
  if userChoice == 1:
    numberGame()

  elif userChoice == 2: 
    buildProfile()
    
  elif userChoice ==3: 
    print("Thank you for talking to me! ")
    quit()
  else: 
    print("Choose from 1, 2, 3! ")


