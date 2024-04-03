from pynput.keyboard import Key, Controller,Listener
import time
keyboard = Controller()
keyMap = {}

keys=[]
def on_press(key):
    string = str(key).replace("'","")

    if string not in keyMap:
        startTime = time.time()
        keyMap[string] = startTime
        print("press===time==="+string +"================" + str(keyMap[string]))
    # insertSql = "insert into keyslog (key,startTime,endTime,time, "


def on_release(key):
    endTime = time.time()
    global keys
    string = str(key).replace("'","")
    print(keyMap[string])
    print("press===time===" + str(keyMap[string] - endTime))
    del keyMap[string]
    keys.append('\r'+string)
    main_string = "".join(keys)
    print(main_string)
    if len(main_string)>15:
      with open('D:\keys.txt', 'a') as f:
          f.write(main_string)
          keys= []
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()