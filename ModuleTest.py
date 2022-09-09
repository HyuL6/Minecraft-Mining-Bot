####################
## Module Testing ##

import MiningBot_Utilities
import pyautogui as pt
from time import sleep
import keyboard

def _moveCharacter(key_press, duration, action = 'walking'):
    if action == 'walking':
        pt.keyDown(key_press)
        sleep(duration)
        pt.keyUp(key_press)

        print("Moved the character for {} seconds.".format(str(duration)))

    
    elif action == 'dashing':
        pt.keyDown(MiningBot_Utilities.DASH_KEY)
        pt.keyDown(key_press)
        sleep(duration)
        pt.keyUp(key_press)
        pt.keyUp(MiningBot_Utilities.DASH_KEY)

        print("Moved the character for {} seconds.".format(str(duration)))
    
    return 0

def testKeyboardCtrl():
    print("---------------Keyboard contral test starts:---------------")
    input("1. Please open a text editor (Notebook, GoogleDocs, Word, etc.). When you are done, go back to the terminal press ENTER to continue.")
    print("2. Please left click on the input line so that your text editor is ready to accept inputs. Leave the cursor there and press SHIFT directly.")
    finished = False
    while not finished:
        if keyboard.is_pressed("shift"):
            cursor_position = pt.position()
            print("SHIFT pressed! Cursor positions recorded: {}.".format(cursor_position))
            finished = True
    
    input("3. Feel free to move the cursor around. Go back to the terminal and Press ENTER. You should see the following line being typed in your text editor:")
    pt.moveTo(cursor_position)
    pt.leftClick(duration= 0.2)
    pt.write("#This is typed by the bot!!")
    print("  #This is typed by the bot!! Congratulations if you see this!")
    print("4. Please check system preference if the test is NOT passed and restart the test.")
    print("---------------Keyboard contral test finished.---------------")

def testMinecraftMouse():

    sleep(3)
    _moveCharacter('w', 2, action= 'dashing')
    _moveCharacter('num4', MiningBot_Utilities.TURN_TIME)
    _moveCharacter('w', 2)




def main():
    print(pt.size())

    print(pt.position())
    sleep(1)

    initial_pos = pt.position()
    print(initial_pos)

    #move the mouse
    #.moveTo(X, Y, time_takes_to_move_cursor_in_seconds)
    pt.moveTo(200, 200, 0.1)

    #move the mouse relative to the current position
    pt.moveRel(500, 500, 0.1) # This will move the cursor to the position (700, 700)
    print(pt.position())

    #click
    #.click(X, Y, number_of_clicks, duration, button = "left")
    # other clicks include .doubleClick, .leftClick, .rightClick. etc.

    # pt.click(234, 372, 1 , 0.2, button= "left")

    # .mouseDown(X, Y, button =) + .mouseUp(X, Y, button =) hold down the button and "drag"
    # pt.mouseDown(100, 100, button = "left")
    # pt.moveTo(500, 100, duration = 0.1)
    # pt.mouseUp(500, 100, button = "left")

    # ！ Or, we can use .dragRel(X, Y, duration, button)

    #.scroll(verticle_pixels)
    #pt.moveTo(initial_pos)
    #pt.scroll(200)
    #print(pt.position())


    ## Keyboard functions
    # type keyboard
    pt.moveTo(initial_pos)
    pt.leftClick(duration= 0.2)
    pt.write("#This is typed by the bot!!")
    pt.press("enter")
    pt.write("#Another line typed by the bot!!")
    #This is typed by the bot!!
    #Another line typed by the bot!!

    # Screenshot
    # pt.screenshot(<path/>"myscreenshot.png")

    # Locate graphic on the screen
    # chat_bar = pt.locateOnScreen("images/B_group_icon.png", confidence = 0.8)
    # print("Target found! The position is: {0}".format(chat_bar))
    # if chat_bar is not None:
    #     goto_chat_bar = pt.center(chat_bar)
    #     print("Target found! The center position is: {0}".format(goto_chat_bar))
    #     goto_chat_bar_X, goto_chat_bar_Y = goto_chat_bar[0]/2, goto_chat_bar[1]/2
    #     # !! wait, wtf?
    #     pt.click(goto_chat_bar_X, goto_chat_bar_Y, duration= 0.2)
    #     pt.moveTo(100, 100, duration= 0.1)

    # else:
    #     print("Target not found!")


    return 0


if __name__ == '__main__':
    testMinecraftMouse()