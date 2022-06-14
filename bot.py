import pyautogui as pag
import keyboard as kb
import time
import random

t = 0
k = 300
list1buttons = {'850': '970', '1067': '951', '1187': '950'}
positions = {'987': '600', '947': '601', '975': '800', '936': '809', '946': '513', '972': '513', '940': '808',
             '1117': '575', '804': '578'}

def transformation():
    a = str(pag.position())
    b = a.replace('Point', '')
    elements = b[1:-1].split(",")
    mytuple = tuple(elements)
    x2 = mytuple[0]
    y2 = mytuple[1].replace(' ', '')
    x2 = int(x2.replace('x=', ''))
    y2 = int(y2.replace('y=', ''))
    print(f'{x2}, {y2}')
    print(pag.pixel(x2, y2))
    time.sleep(0.15)
    kb.release("i")
    # преоброзование Point(x,y) в x и y

def click1(x, y):
    pag.mouseDown(x, y, button='left')
    pag.mouseUp(x, y, button='left')

def exit():
    click1(x=952, y=947)
    time.sleep(8)

def start():
    time.sleep(2.5)
    click1(x=1076, y=703)
    time.sleep(0.2)
    # кнопка1(диско)
    click1(x=1105, y=757)
    time.sleep(0.2)
    # кнопка2(режим)
    click1(x=957, y=680)
    time.sleep(0.1)
    # сундук
    time.sleep(9)
    # ожидание

def play():
    start()
    for j in range(1, 100):
        if pag.pixel(944, 948) == (255, 255, 255) and pag.pixel(966, 946) == (255, 255, 255) \
                and pag.pixel(1005, 944) == (104, 187, 255) and pag.pixel(923, 946) == (104, 187, 255):
            exit()
            break
        #проверка на кнопку
        l1 = []
        k1 = random.choice(tuple(list1buttons.items()))
        for x in list(k1):
            a = x
            l1.append(a)
        x1 = l1[0]
        y1 = l1[1]

        l2 = []
        k2 = random.choice(tuple(positions.items()))
        for x in list(k2):
            a1 = x
            l2.append(a1)
        x3 = l2[0]
        y3 = l2[1]
        click1(int(x1), int(y1))
        time.sleep(random.randint(40, 50)/100)
        click1(int(x3), int(y3))
        time.sleep(random.randint(330, 360)/100)

while True:
    if kb.is_pressed("p"):
        kb.release("p")
        for i in range(1, k):
            play()
            t = t+1
            print(t)
    elif kb.is_pressed("o"):
        print(pag.position())
        time.sleep(0.15)
        kb.release("o")
    elif kb.is_pressed("i"):
        transformation()
