while True:
    try: # the block of code below 'try' is being tested
        roomChoice = int(input("Which room would you like to book?: "))
        if isinstance(roomChoice, int) and roomChoice >= 0:  # if roomChoice is an positive int exit the loop
            break
    except ValueError as e: # following is what happens if there's a ValueError
        print(f'An {e} error occured! Input an integer!')