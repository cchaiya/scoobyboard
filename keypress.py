import keyboard
def myClick():
    if key.is_pressed('w'):
       print('w')
    elif key.is_pressed('s'):
       print('s')
    elif key.is_pressed('k'):
       print('k')
    elif key.is_pressed('i'):
       print('i')
    elif key.is_pressed('q'):
       print("quit")
       quit()
    else:
       print("error")
