import pyautogui as pag
import keyboard as kb
import time
import random

t = 0
k = 300
listx = [850, 1067, 1187]

while True:
    if kb.is_pressed("p"):
        for i in range(1, k):
            time.sleep(2.5)
            pag.mouseDown(x=1076, y=703, button='left')
            pag.mouseUp(x=1076, y=703, button='left')
            time.sleep(0.2)
            #кнопка1(диско)

            pag.mouseDown(x=1105, y=757, button='left')
            pag.mouseUp(x=1105, y=757, button='left')
            time.sleep(0.2)
            #кнопка2(режим)

            pag.mouseDown(x=957, y=680, button='left')
            pag.mouseUp(x=957, y=680, button='left')
            time.sleep(0.1)
            #сундук

            time.sleep(9)
            #ожидание

            for j in range(1, 43):
                d = random.randrange(1, 11, 1)
                x1 = random.choice(listx)
                if x1 == 850:
                    y1 = 970
                elif x1 == 1067:
                    y1 = 951
                elif x1 == 1187:
                    y1 = 950
                if d == 1 or d == 10:
                    pag.mouseDown(x1, y1, button='left')
                    pag.mouseUp(x1, y1, button='left')
                    time.sleep(0.51)
                    pag.mouseDown(x=987, y=600, button='left')
                    pag.mouseUp(x=967, y=607, button='left')
                    time.sleep(3.4)
                    #1

                elif d == 2 or d == 11:
                    pag.mouseDown(x1, y1, button='left')
                    pag.mouseUp(x1, y1, button='left')
                    time.sleep(0.52)
                    pag.mouseDown(x=947, y=601, button='left')
                    pag.mouseUp(x=947, y=601, button='left')
                    time.sleep(3.6)
                    #2

                elif d == 3:
                    pag.mouseDown(x1, y1, button='left')
                    pag.mouseUp(x1, y1, button='left')
                    time.sleep(0.46)
                    pag.mouseDown(x=975, y=800, button='left')
                    pag.mouseUp(x=975, y=800, button='left')
                    time.sleep(3.5)
                    #3

                elif d == 4:
                    pag.mouseDown(x1, y1, button='left')
                    pag.mouseUp(x1, y1, button='left')
                    time.sleep(0.45)
                    pag.mouseDown(x=936, y=809, button='left')
                    pag.mouseUp(x=936, y=809, button='left')
                    time.sleep(3.3)
                    #4

                elif d == 5:
                    pag.mouseDown(x1, y1, button='left')
                    pag.mouseUp(x1, y1, button='left')
                    time.sleep(0.41)
                    pag.mouseDown(x=946, y=513, button='left')
                    pag.mouseUp(x=946, y=513, button='left')
                    time.sleep(3.4)
                    #5

                elif d == 6:
                    pag.mouseDown(x1, y1, button='left')
                    pag.mouseUp(x1, y1, button='left')
                    time.sleep(0.423)
                    pag.mouseDown(x=972, y=513, button='left')
                    pag.mouseUp(x=972, y=513, button='left')
                    time.sleep(4.2)
                    #6

                elif d == 7:
                    pag.mouseDown(x1, y1, button='left')
                    pag.mouseUp(x1, y1, button='left')
                    time.sleep(0.49)
                    pag.mouseDown(x=940, y=808, button='left')
                    pag.mouseUp(x=940, y=808, button='left')
                    time.sleep(3.1)
                    #7

                elif d == 8:
                    pag.mouseDown(x1, y1, button='left')
                    pag.mouseUp(x1, y1, button='left')
                    time.sleep(0.481)
                    pag.mouseDown(x=1117, y=575, button='left')
                    pag.mouseUp(x=1117, y=575, button='left')
                    time.sleep(3.4)
                    #8

                elif d == 9:
                    pag.mouseDown(x1, y1, button='left')
                    pag.mouseUp(x1, y1, button='left')
                    time.sleep(0.432)
                    pag.mouseDown(x=804, y=578, button='left')
                    pag.mouseUp(x=804, y=578, button='left')
                    time.sleep(3.8)
                    #9

            #вариации ходов
            t = t + 1
            print(t)
            pag.mouseDown(x = 952, y = 947, button='left')
            pag.mouseUp(x = 952, y = 947, button='left')
            time.sleep(8)
            kb.release("p")
            #выход
    elif kb.is_pressed("o"):
        print(pag.position())
        time.sleep(0.15)
        kb.release("o")
        # берёт позиции
