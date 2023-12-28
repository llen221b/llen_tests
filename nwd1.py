a = int(input('Cześć! Proszę podać liczbę \n'))
b = int(input('Bardzo dobrze! Proszę podać jeszcze jedną \n'))

while a != b:
    if a > b:
        a = a-b
    else:
        b = b-a
print('nwd =', a)
