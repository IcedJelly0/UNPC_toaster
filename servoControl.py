import time

while True:
    f = open('JSPythonLink.txt', 'r')
    popToast = f.read(1)
    if popToast == '1':
        print('Come Get YA toast')
    if popToast == '0':
        print('Zzzzzzz')
    f.close()
    time.sleep(0.1)