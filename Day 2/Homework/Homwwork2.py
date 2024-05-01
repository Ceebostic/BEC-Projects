#Where are you
place = (input("Are you in the forest or cave?:"))
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You can see the cave paintings!")
    elif action == "proceed in the dark":
        print("You stumble upon a hidden treasure!")
    else:
        pass  
else:
    pass  

attendees= int(input("enter number of attendees:"))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)