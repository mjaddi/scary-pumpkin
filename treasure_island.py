print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input("You begin at a fork in the road. Do you want to go left or right?\n ").lower()

if direction == "left":
    swim_or_wait = input("You walk till you reach a lake. Would you like to swim across or wait? Please type swim or wait.\n ").lower()
    if swim_or_wait == "wait":
        colored_doors =input("You wait for 3 days before 3 colored doors appear. Which door will you enter through? Please select Red, Yellow or Blue.\n ").lower()
        if colored_doors == "yellow":
            print("Congratulations!!! You found the treasure!")
            print("YOU WIN!!!")
        elif colored_doors == "red":
            print("You fall into a pit of fire.")
            print("GAME OVER!!!")
        elif colored_doors == "blue":
            print("You encounter a magical beast and get eaten by it.")
            print("GAME OVER!!!")
        else:
            print("GAME OVER!!!")
    else:
        print("You got attacked by an enormous trout.")
        print("GAME OVER!!!")
else:
    print("You fell into a hole with spikes in it.")
    print("GAME OVER!!!")
