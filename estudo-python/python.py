# passo 1 abrir o sistema da empresa
# Link sistema teste: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# passo 2 fazer login
# passo 3 importar base de dados dos produtos
# passo 4 cadastrar um produto 
# passo 5 repetir o passo 4 atr acabar tudo

import pyautogui
import time
pyautogui.PAUSE = 1
 # pyautogui.click
 # pyautogui.write
 # pyautogui.press

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=510, y=437)
time.sleep(2)
pyautogui.click(x=900, y=489)
time.sleep(1.5)
pyautogui.click(x=498, y=411)
pyautogui.write("josias")
time.sleep(1)
pyautogui.press("tab")
pyautogui.write("JD")
pyautogui.press("enter")