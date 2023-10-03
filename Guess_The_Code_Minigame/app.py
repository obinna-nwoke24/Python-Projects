"""
Author: Obinna Jason Nwoke II
"""
import os
import sys

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from assets import guessthecode, backend

__name__ = "app.py"
WORKING_DIR = __file__.replace(__name__, "")

LEVEL = [x+1 for x in range(100)]
GAME_DB_FILE = WORKING_DIR + "assets\\game_db.json"
GAME_STATE_FILE = WORKING_DIR + "assets\\game_state.json "
game_state = backend.load(GAME_STATE_FILE)
game_state_list = [0, 1, 2]


def change_game_state(change_to: int = 0):
    """
    Changes the game state based on the value
    :param change_to:
    :return:
    """
    if change_to == 0:
        # 0 is running
        game_state['Running'] = True
        game_state['Paused'] = False
        game_state['Exited'] = False
    elif change_to == 1:
        # 1 is paused -- used for starting the game from the paused state
        game_state['Running'] = False
        game_state['Paused'] = True
        game_state['Exited'] = False
    elif change_to == 2:
        # 2 is exited -- does not save the last user or the paused level
        game_state['Running'] = False
        game_state['Paused'] = False
        game_state['Exited'] = True
        game_state['Last User'] = None
        game_state['Users Paused Level'] = None
    backend.update_json(game_state, GAME_STATE_FILE)


def run():
    """
    Runs the game
    :return:
    """
    finish_code = 0
    if game_state['Exited']:
        # if the current state is exited -- start a new game
        change_game_state(0)
        backend.update_json(game_state, GAME_STATE_FILE)
        user = input("What is your name: ")
        game_db = backend.load(GAME_DB_FILE)

        if user.upper() in game_db.keys():
            # if the user is in the database
            print("Welcome back %s" % user)
        else:
            # otherwise, add the new user
            game_db[user.upper()] = {"User": user.upper(), "High Score": 0}
            print("New User Added: %s" % user)
        for level in LEVEL:
            # levels are 1 to 100
            try:
                # get the returned finish code from the played level
                finish_code = guessthecode.generate_level(level=level)
            except ValueError:
                exit()
            if finish_code == 0:
                maximum = 0
                max_user = ""
                print("\nScore: Level %s" % (level - 1))
                if (level - 1) > game_db[user.upper()]['High Score']:
                    game_db[user.upper()]['High Score'] = level - 1
                    print("Your new high score: Level %s" % game_db[user.upper()]['High Score'])
                backend.update_json(game_db, GAME_DB_FILE)

                for u in game_db.keys():
                    if game_db[u]["High Score"] > maximum:
                        maximum = game_db[u]["High Score"]
                        max_user = game_db[u]["User"]
                print("High Score\n%s: Level %s" % (max_user, maximum))
                change_game_state(2)
                backend.update_json(game_state, GAME_STATE_FILE)
                break
            elif finish_code == 1:
                if level > game_db[user.upper()]['High Score']:
                    game_db[user.upper()]['High Score'] = level
                    backend.update_json(game_db, GAME_DB_FILE)
                print("Next Level!\n")
            elif finish_code == 2:
                change_game_state(finish_code)
                backend.update_json(game_state, GAME_STATE_FILE)
                break
            elif finish_code == 3:
                change_game_state(2)
                backend.update_json(game_state, GAME_STATE_FILE)
                maximum = 0
                max_user = ""
                print("\nScore: Level %s" % (level - 1))
                if (level - 1) > game_db[user.upper()]['High Score']:
                    game_db[user.upper()]['High Score'] = level - 1
                    print("Your new high score: Level %s" % game_db[user.upper()]['High Score'])
                backend.update_json(game_db, GAME_DB_FILE)

                for u in game_db.keys():
                    if game_db[u]["High Score"] > maximum:
                        maximum = game_db[u]["High Score"]
                        max_user = game_db[u]["User"]
                print("High Score\n%s: Level %s" % (max_user, maximum))
                change_game_state(2)
                backend.update_json(game_state, GAME_STATE_FILE)
                break

            elif finish_code == 'P':
                print("Pausing Game! Safe to resume later.")
                change_game_state(1)
                game_state['Last User'] = user.upper()
                game_state['Users Paused Level'] = level
                backend.update_json(game_state, GAME_STATE_FILE)
                break
    elif game_state['Paused']:
        user = game_state['Last User']
        start_level = game_state['Users Paused Level']
        change_game_state(0)
        backend.update_json(game_state, GAME_STATE_FILE)
        game_db = backend.load(GAME_DB_FILE)

        if user.upper() in game_db.keys():
            print("Resuming game for %s" % user)
        else:
            game_db[user.upper()] = {"User": user.upper(), "High Score": 0}
            print("New User Added: %s" % user)
        for level in range(start_level, (LEVEL[-1]+1)):
            try:
                finish_code = guessthecode.generate_level(level=level)
            except ValueError:
                exit()
            if finish_code == 0:
                maximum = 0
                max_user = ""
                print("\nScore: Level %s" % (level - 1))
                if (level - 1) > game_db[user.upper()]['High Score']:
                    game_db[user.upper()]['High Score'] = level - 1
                    print("Your new high score: Level %s" % game_db[user.upper()]['High Score'])
                backend.update_json(game_db, GAME_DB_FILE)

                for u in game_db.keys():
                    if game_db[u]["High Score"] > maximum:
                        maximum = game_db[u]["High Score"]
                        max_user = game_db[u]["User"]
                print("High Score\n%s: Level %s" % (max_user, maximum))
                change_game_state(2)
                backend.update_json(game_state, GAME_STATE_FILE)
                break
            elif finish_code == 1:
                if level > game_db[user.upper()]['High Score']:
                    game_db[user.upper()]['High Score'] = level
                    backend.update_json(game_db, GAME_DB_FILE)
                print("Next Level!\n")
            elif finish_code == 2:
                change_game_state(finish_code)
                backend.update_json(game_state, GAME_STATE_FILE)
                break
            elif finish_code == 3:
                change_game_state(2)
                backend.update_json(game_state, GAME_STATE_FILE)
                maximum = 0
                max_user = ""
                print("\nScore: Level %s" % (level - 1))
                if (level - 1) > game_db[user.upper()]['High Score']:
                    game_db[user.upper()]['High Score'] = level - 1
                    print("Your new high score: Level %s" % game_db[user.upper()]['High Score'])
                backend.update_json(game_db, GAME_DB_FILE)

                for u in game_db.keys():
                    if game_db[u]["High Score"] > maximum:
                        maximum = game_db[u]["High Score"]
                        max_user = game_db[u]["User"]
                print("High Score\n%s: Level %s" % (max_user, maximum))
                change_game_state(2)
                backend.update_json(game_state, GAME_STATE_FILE)
                break
            elif finish_code == 'P':
                print("Pausing Game! Safe to resume later.")
                change_game_state(1)
                game_state['Last User'] = user.upper()
                game_state['Users Paused Level'] = level
                backend.update_json(game_state, GAME_STATE_FILE)
                break


try:
    run()
except KeyboardInterrupt:
    change_game_state(2)
    backend.update_json(game_state, GAME_STATE_FILE)
    print("Stopped abruptly")
    exit()
