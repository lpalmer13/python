question_1 = input('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ')
if question_1.lower() == 'match':
    question_2 = input('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ')
    if question_2.lower() == 'run':
        question_2_option_1 = input('You run and the bear starts chasing after you all the way out of the forest. You get back to your jeep, get in and drive off before the bear catches you. Do you DRIVE BACK HOME, or DRIVE TO YOUR CABIN? ')
        question_2_option_1 = input('You drive back home and make it back safely. ')
        if question_2_option_1.lower() == 'drive back home':
                question_2_option_1 = print('You drive back home and make it back safely. ')
        elif question_2_option_1.lower == 'drive to your cabin':
            question_2_option_1 = print('You drive up to your cabin safely and stay the night. ')
        else:
            print("Only type 'DRIVE BACK HOME' or 'DRIVE TO YOUR CABIN'. ")
    elif question_2.lower() == "hide":
        question_2_option_2 = input('You hide behind the tree and find a can of bear spray. Do you CLIMB THE TREE, or do you SPRAY THE BEAR with the bear spray? ')
        if question_2_option_2.lower == 'climb the tree':
            question_2_option_2 = print('You climb the tree and the bear happens to step on the can of bear spray. That causes the can to explode and the bear gets covered in bear spray. Then the bear runs away back into the forest. Then you climb back down the tree, and you decide to head back home for the night. ')
        elif question_2_option_2.lower == 'spray the bear':
            question_2_option_2 = print("You pick up the can of bear spray, the bear comes towards you, and you spray the bear's face with a bunch of bear spray. Then the bear runs away from you back into the forest. Then you decide to drive back home for the night. ")
        else:
            print("Only type 'CLIMB THE TREE' or 'SPRAY THE BEAR'. ")
    else:
        print("Only type 'RUN' or 'HIDE'. ")
elif question_1.lower() == 'flashlight':
    question_2 = input('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ')
    if question_2.lower() == 'follow':
        question_2_option_1 = print('You follow the noise and you see a large grizzly bear nearby. The bear sees you and starts coming towards you. Do you RUN, or HIDE behind a tree. ')
        if question_2_option_1.lower() == 'run':
            question_2_option_1 = print('You run and the bear starts chasing after you all the way out of the forest. You get back to your jeep, get in and drive off before the bear catches you. Then you decide drive back home for the night. ')
        elif question_2_option_1.lower() == 'hide':
            question_2_option_1 = print("You hide behind a tree and find a can of bear spray. You pick up the can of bear spray, and when the bear comes towards you, you spray the bear's face with a bunch of bear spray, and the bear runs away for you back into the forest. Then you decide to drive back home for the night. ")
        else:
            print("Only type 'RUN' or 'HIDE'.")
    elif question_2.lower() == 'look':
        question_2_option_2 = input('You look in the trees for the thing that made that noise, and as you are walking around you happen to find a can of bear spray. Then immediatly you see a large grizzly bear nearby. The bear sees you and starts coming towards you. Do you CLIMB A TREE, or do you SPRAY THE BEAR with the bear spray? ')
        if question_2_option_2.lower() == 'climb a tree':
            question_2_option_2 = print('You climb a tree and the bear happens to step on the can of bear spray. That causes the can to explode and the bear gets covered in bear spray. Then the bear runs away back into the forest. Then you climb back down the tree, and you decide to head back home for the night. ')
        elif question_2_option_2.lower() == 'spray the bear':
            question_2_option_2 = print("You pick up the can of bear spray, the bear comes towards you, and you spray the bear's face with a bunch of bear spray. Then the bear runs away from you back into the forest. Then you decide to drive back home for the night. ")
        else:
            print("You can only type 'CLIMB A TREE' or 'SPRAY THE BEAR'. ")
    else:
        print("Only type 'FOLLOW' or 'LOOK'. ")
else:
    print("Only type 'MATCH' or 'Flashlight'. ")
    