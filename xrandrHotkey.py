import keyboard, threading, os, subprocess

increaseHotkey = 'ctrl+shift+f4' # Declare increase hotkey
decreaseHotKey = 'ctrl+shift+f3' # Declare decrease hotkey
target = 'eDP' # Target display name from 'xrandr --vervose' commmand, e.g. HDMI-A-0. eDP

def getCurrentBrightness():
    currentBrightness = ""
    output = subprocess.check_output(["xrandr --verbose"], shell=True).decode('UTF-8').strip().split('\n')
    for idx, i in enumerate(output):
        text = i.replace('\t','')
        flag = text.find(target)
        if(flag == 0):
            raw = output[idx+5].split(':')
            currentBrightness = raw[1].strip()
            break
    return currentBrightness

def increaseEvent():
    currentBrightness = float(getCurrentBrightness())
    if(currentBrightness <= 1.0):
        os.system(f'xrandr --output {target} --brightness {currentBrightness+0.1}')

def decreaseEvent():
    currentBrightness = float(getCurrentBrightness())
    if(currentBrightness >= 0.2):
        os.system(f'xrandr --output {target} --brightness {currentBrightness-0.1}')

keyboard.add_hotkey(increaseHotkey, increaseEvent)
keyboard.add_hotkey(decreaseHotKey, decreaseEvent)

def th1():
    keyboard.wait()

threading.Thread(target=th1).start()