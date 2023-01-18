from datetime import datetime
import os
import time

import pyautogui
today = datetime.now()
print(f"{today.time()}")
if __name__ == '__main__':
    b = time.time()
    c = 0
    ls = [1,2,3,4,5,6]
    for i in ls:
        a = time.time()
        print(f"현재 시간 :{i}번째 {time.time()}")
        print(f"c의 값은 ----- {b-a}")
        os.mkdir(f"C:/Users/bitcamp/django-react/DjangoServer/team/{i}")
        time.sleep(i)
        time.sleep(0.5)
        time.sleep(0.5)
        for j in range(14):
            pyautogui.screenshot(f"C:/Users/bitcamp/django-react/DjangoServer/team/{i}/{j+1}.PNG")
            time.sleep(1)
        pyautogui.screenshot(f"C:/Users/bitcamp/django-react/DjangoServer/team/{i}/15.PNG")
        b = time.time()

