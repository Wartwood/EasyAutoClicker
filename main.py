import keyboard
import mouse
import time

click = False


def set_clicker():
    global click
    if click:
        click = False
        print('\nClicker trying to inactivate \n')
    else:
        click = True
        print('\nClicker trying to activate \n')


keyboard.add_hotkey('Alt + Q', set_clicker)

clickSpeed = float(input('Input the speed, please. You can input s (seconds) or ms (milliseconds): '))
clickButton = input('Input the mouse button. (right or left), or can exit by typing "exit": ')
print('Click "Alt + Q" to start autoclicker!')
while True:
    if clickButton != 'exit':
        if click:
            if clickButton == 'left':
                print(f'Start clicking with right button with speed: {clickSpeed}\n')
                mouse.double_click(button='left')
            elif clickButton == 'right':
                print(f'Start clicking with right mouse button with speed: {clickSpeed}\n')
                mouse.double_click(button='right')
            else:
                clickButton = input('Input error! Retype button, please! (left or right)').lower()
                try:
                    mouse.double_click(button=clickButton)
                except:
                    clickButton = input('Input error! Retype button, please! (left or right)').lower()
            time.sleep(clickSpeed)
    else:
        print('Bye-Bye!')
        break
