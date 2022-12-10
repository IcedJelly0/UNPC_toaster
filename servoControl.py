with open('JSPythonLink.txt', 'r') as f:
    popToast = f.read(1)

while True:
    if popToast:
        print('Come Get YA toast')
    else:
        print('Zzzzzzz')