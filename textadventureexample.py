#!/usr/bin/python
from time import sleep # this allows us to sleep a function in seconds

def game_start(): # Start of the game
    print('Welcome to a text based adventure made by Groguard') # Start filling in the beginning of  your story here
    sleep(3) # You can add a sleep between messages to slow the text down if you want
    print("You wake up in a dungeon and a giant troll is walking towards you.")
    sleep(3) # You can add a sleep between messages to slow the text down if you want
    print("There are 2 weapons near you on the ground, a sword, a bow, and a quiver of arrows.")
    sleep(3) # You can add a sleep between messages to slow the text down if you want
    weapon = raw_input("Which one would you like to choose? sword/bow:") # get input from the player to see what they want to do
    if weapon == 'sword': # if the weapon chosen is the sword, we call the sword function
        sword() # calling the sword function
    elif weapon == 'bow': # if the weapon chosen is the bow, we call the bow function
        bow() # calling the bow_arrow function
    else: # if the player enters something other than sword or bow
        print("Please try again. There seemed to be a problem with what you entered.")
        game_start()
    
def sword(): # if the users picks sword this is what will happen next
    print("You pick up the sword.") # Add what you would to happen here
    sleep(3)
    fightTroll = raw_input("You fight the troll, or run away? fight/run:") # get input from the player to see what they want to do
    if fightTroll == "fight":
        print('You draw your sword and charge at the troll and drive your sword right through him. You exit the cave.')
        sleep(3)
        stage_2() # call the stage_2 function to continue the story
    elif fightTroll == "run":
        print("You run as fast as you can around the troll and exit the cave.")
        sleep(3) 
        stage_2() # call the stage_2 function to continue the story
    else: # if the player enters something other than fight or run
        print("Please try again. There seemed to be a problem with what you entered.")
        sword()
        
def bow(): # if the user picks bow_arrow this is what will happen next
    print("You pick up the bow and quiver")
    sleep(3)
    fightTroll = raw_input("You fight the troll or run away? fight/run:")
    if fightTroll == "fight":
        print("You raise you bow and draw your arrow back! You release your arrow sending it straight through the troll! You exit the cave.")
        sleep(3)
        stage_2() # call the stage_2 function to continue the story
    elif fightTroll == "run"
        print("You run as fast as you can around the troll and exit the cave.")
        sleep(3)
        stage_2() # call the stage_2 function to continue the story
    else:
        print("Please try again. There seemed to be a problem with what you entered.")
        bow()
    
def stage_2():
        print('You made it out of the cave, but there are other creatures around, so you should find shelter fast!')
        sleep(3)
        print("You look around to see if you can find anything near you that might help.")
        sleep(3)
        print("You see some type of tree fort off to your left, and you see smoke coming from what looks like a camp fire to your right.")
        sleep(3)
        treeorfire = raw_input("Would you like to head to the tree fort or the smoke? fort/smoke:")
        if treeorfire == "fort":
            tree_fort()
        elif treeorfire == "smoke":
            fire_smoke()
        else:
            print("Please try again. There seemed to be a problem with what you entered.")
            stage_2()
            
def tree_fort():
    print("You're making your way through the jungle when you decide to sit for a moment to take a break.")
    sleep(3)
    print("You glance around the area to see if you can find some water. Just over a small hill you see a small stream.")
    sleep(3)
    print("As you approach the stream you notice a man just oposite of you getting some water as well.")
    
def fire_smoke():            
    print("You're making your way through the jungle when you decide to sit for a moment to take a break.")
    sleep(3)
    print("You glance around the area to see if you can find some water. Just over a small hill you see a small stream.")
    sleep(3)
    print("After your break you continue on in the direction of the smoke.")
    
game_start() # call the game_start function to start the adventure