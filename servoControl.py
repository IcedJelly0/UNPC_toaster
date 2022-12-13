import time
# import keyboard
# e = 0
# while True:
#     if keyboard.is_pressed("up arrow"):
#         e += 1
#     if keyboard.is_pressed("down arrow"):
#         e += -1
#     if keyboard.is_pressed("right arrow"):
#         e += 5
#     if keyboard.is_pressed("left arrow"):
#         e += -5
#     print(e)
#     time.sleep(0.05)

while True:
    f = open('JSPythonLink.txt', 'r')
    popToast = f.read(1)
    if popToast == '1':
        
        print('Come Get YA toast')
    if popToast == '0':
        print('Zzzzzzz')
    f.close()
    time.sleep(0.1)