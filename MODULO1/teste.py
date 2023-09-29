import pyautogui as py
import random
import time

time.sleep(5)

mensagens = ['oi pai', 'vamos trabalhar', 'teste 3', 'teste 4', 'teste 5', 'teste 6', 'teste 7']

for i in range(5):
    msg = random.choice(mensagens)
    py.typewrite(msg)
    py.press('enter')
    time.sleep(1)