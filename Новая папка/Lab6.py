import time as tm
pause_int = 6 #sec
pause_str = '.'
print(f'\nPause by {pause_int} sec')
print(pause_str, end='')
for i in range(pause_int):
    tm.sleep(1)
    print(pause_str, end = '')
print()
