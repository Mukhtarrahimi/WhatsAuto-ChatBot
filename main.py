import pyautogui
from time import sleep
from random import choice, uniform

messages = ["hello!", "hi", "I am robot", "Rahimi"]

x_click = 410
y_click = 986

num_messages = 4

for i in range(num_messages):
    sleep(uniform(0.5, 2))  
    pyautogui.click(x_click, y_click) 
    message = choice(messages) 
    pyautogui.write(message, interval=0.05)
    pyautogui.press("enter")  
