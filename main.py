################
## Main Logic ##
import MiningBot
import MiningBot_Utilities
import pyautogui as pt
from time import sleep

def main():
    sleep(3)
    moving_bot = MiningBot.MiningBot()
    moving_bot._moveCharacter(key_press = 'w', duration = 3)
    moving_bot._turn('left')
    moving_bot._moveCharacter(key_press = 'w', duration = 3)
    
    return 0


if __name__ == '__main__':
    main()