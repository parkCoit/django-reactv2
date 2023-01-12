from datetime import datetime
import os
import time

import pyautogui
today = datetime.now()
print(f"{today.time()}")
if __name__ == '__main__':


    ls = [1,2,3,4,5,6]
    for i in ls:
        print(f"현재 시간 :{i}번째 {datetime.now().time()}")
        os.mkdir(f"C:/Users/bitcamp/django-react/DjangoServer/team/{i}")
        print(f"현재 시간 디렉토리 만들고 :{i}번째 {datetime.now().time()}")
        time.sleep(i)
        print(f"현재 시간 slepp 첫 번째 :{i}번째 {datetime.now().time()}")
        time.sleep(0.5)
        print(f"현재 시간 slepp 두 번째 :{i}번째 {datetime.now().time()}")
        time.sleep(0.5)
        print(f"현재 시간 slepp 세 번째 :{i}번째 {datetime.now().time()}")
        for j in range(14):
            print(f"loop 시간 :{i}번째 {datetime.now().time()}")
            pyautogui.screenshot(f"C:/Users/bitcamp/django-react/DjangoServer/team/{i}/{j+1}.PNG")
            time.sleep(1)
        pyautogui.screenshot(f"C:/Users/bitcamp/django-react/DjangoServer/team/{i}/15.PNG")
