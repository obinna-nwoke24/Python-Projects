"""
Author: Obinna Jason Nwoke II
"""
import random


def generate_level(level: int = 1):
    # generate the level
    digits = 1
    range_ = [0, 9]
    tries = 10
    finish_code = 1

    print("Level %s" % level)

    if level < 3:
        # levels 1 - 2 -> 4 tries, 1 digit code, digits from 0 to 2
        tries = 4
        digits = 1
        range_ = [0, 3]
    elif level < 6:
        # levels 3 - 5 -> 8 tries, 2 digit code, digits from 0 to 5
        tries = 8
        digits = 2
        range_ = [0, 6]
    elif level < 10:
        # levels 6 - 9 -> 10 tries, 3 digit code, digits from 0 to 9
        tries = 10
        digits = 3
    elif level < 20:
        # levels 10 - 19 -> 15 tries, 4 digit code, digits from 0 to 9
        tries = 15
        digits = 4
    elif level < 50:
        # levels 20 - 49 -> 15 tries, 5 digit code, digits from 0 to 9
        tries = 15
        digits = 5
    # did not continue on from there... further development is needed

    # generate code
    code = ""
    while len(code) != digits:
        code = ""
        for x in range(digits):
            code += str(random.randint(range_[0], range_[1]))
    code = int(code)

    # user input for the code
    guess = input("The vault is locked. %s digit code. %s tries to guess the code. What is the code? " %
                  (len(str(code)), tries))
    if guess in ['q', 'Q']:
        print("Exiting Game")
        finish_code = 2
        return finish_code
    if guess in ['end', 'End', 'END']:
        print("Ending Game")
        finish_code = 3
        return finish_code
    elif guess in ['p', 'P']:
        finish_code = 'P'
        return finish_code

    guess = int(guess)

    # process
    while guess != code:
        hint = ""
        # high low hint
        if guess < code:
            hint += "Too low. "
        else:
            hint += "Too high. "

        try:
            # correct places hint
            correct_digits = 0
            for x in range(len(str(code))):
                if str(guess)[x] == str(code)[x]:
                    correct_digits += 1
            hint += "There are %s digits in the correct spot. " % correct_digits
        except IndexError:
            print("Your guess does not have the right amount of digits")
            print("Restarting level %s" % level)
            generate_level(level)

        try:
            # digits exist hint
            existing_digits = 0
            for x in range(len(str(code))):
                if str(guess)[x] in str(code):
                    existing_digits += 1
            hint += "You have %s existing digits. " % existing_digits
        except IndexError:
            print("Restarting level %s" % level)
            generate_level(level)

        tries -= 1
        if tries == 0:
            finish_code = 0
            break
        guess = input(hint + "%s tries remain. What is the code? " % tries)
        if guess in ['q', 'Q']:
            print("Exiting Game")
            finish_code = 2
            return finish_code
        if guess in ['end', 'End', 'END']:
            print("Ending Game")
            finish_code = 3
            return finish_code
        elif guess in ['p', 'P']:
            finish_code = 'P'
            return finish_code
        guess = int(guess)

    if finish_code == 0:
        print("Too many attempts! The vault stays locked. The code was %s" % code)
    elif finish_code == 1:
        print("You guessed the code correct! The vault is unlocked!")
    return finish_code
