#Импорт модулей
import tkinter
from tkinter import *
from random import randint
from PIL import ImageTk, Image
import threading
import winsound
import requests
import os
#Назначение переменных

Game_process = True
dinoX =156
coins = 0
y = 60
stones = []
cactosX = 0
cactos_spawnX = 400
pterodactel_spawnX = 800
pterodactel_X = 0
jumped = "None"
min_Y = 0
_exit_ = "None"
try:
    f = open("coins.txt","r")
    rec_coins = f.readline()
    f.close()
except FileNotFoundError:
    rec_coins = 0
#Движение птеродактеля
def pterodaktel_moving():
    global cactos_spawnX, y, min_Y, Game_process, rec_coins, coins, cactosX,pterodactel_spawnX,pterodactel_X
    if not Game_process:
        return
    if pterodactel_X > 0:
        pterodactel_X -= 2
        pterodaktel.place(x=pterodactel_X,y=20,width=42,height=26)
    if pterodactel_X < 0 or pterodactel_X == 0:
        pterodactel_X = pterodactel_spawnX + randint(0, 2000)
        pterodaktel.place(x=pterodactel_X,y=20,width=42,height=26)
    window.after(10,pterodaktel_moving)
#Анимации
def dino_animation():
    global dino_img1,dino_img2
    if dino.cget('image') == "pyimage1":
        dino.configure(image=dino_img2)
        dino.image=dino_img2
    else:
        dino.configure(image=dino_img1)
        dino.image=dino_img1
    window.after(200, dino_animation)
#Продолжение игры
def reply_game():
    global cactosX, cactos_spawnX, y, min_Y, Game_process,rec_coins,coins,pterodactel_X,pterodactel_spawnX
    if not Game_process:
        if coins > int(rec_coins):
            rec_coins = coins
        btn.place(x=9999, y=100, width=85, height=32)
        Game_process = True
        cactosX = cactos_spawnX
        cactos_moving()
        death()
        pterodactel_X = pterodactel_spawnX
        pterodaktel_moving()
#Обработка смерти
def death():
    global Game_process,coins
    if not Game_process:
        return
    if cactos.winfo_x() < dinoX:
        if cactos.winfo_x() > 90:
            if round(dino.winfo_y()+67) > 100:
                Game_process = False
                winsound.PlaySound(death_sound, winsound.SND_FILENAME)
                if coins > int(rec_coins):
                    f = open("coins.txt","w")
                    f.write(str(coins))
                    f.close()
                coins = 0
                btn.place(x=100, y=100, width=85, height=32)
    if pterodaktel.winfo_x() < dinoX:
        if pterodaktel.winfo_x() > 90:
            if round(dino.winfo_y() + 67) < 100:
                Game_process = False
                winsound.PlaySound(death_sound, winsound.SND_FILENAME)
                if coins > int(rec_coins):
                    f = open("coins.txt", "w")
                    f.write(str(coins))
                    f.close()
                coins = 0
                btn.place(x=100, y=100, width=85, height=32)
    window.after(10, death)
#Движения кактуса
def cactos_moving():
    global cactosX,cactos_spawnX,y,min_Y,Game_process,stones,coins
    coins +=1
    if not Game_process:
        return
    if cactosX > 0:
        cactosX -= 2
        cactos.place(x=cactosX, y=y+12, width=26, height=47)
    if cactosX < 0 or cactosX == 0:
        cactosX = cactos_spawnX + randint(0,300)
        cactos.place(x=cactosX, y=y+12, width=26, height=47)
    info.config(text = f"Очки:{coins} Рекорд:{rec_coins}")
    for stone in stones:
        stone.place(x=stone.winfo_x()-2,y=stone.winfo_y(),width=10,height=6)
        if stone.winfo_x() < 0:
            stone.place(x=400+randint(0,150), y=randint(123,140), width=10, height=6)
    window.update()
    window.after(10, cactos_moving)
#Обработка прыжка
def jump_th(funk_th):
    _exit_ = "None"
    global jumped, min_Y, Game_process, cactosX
    if not Game_process:
        return
    if jumped != "None":
        return
    min_Y = 10
    def jump():
        def sound():
            winsound.PlaySound(jump_sound, winsound.SND_FILENAME)
        global jumped,min_Y,Game_process,cactosX,_exit_
        sound_thread = threading.Thread(target=sound)
        sound_thread.setName("sound_process")
        sound_thread.start()
        min_Y = 10
        jumped = "True"
        while True:
            if min_Y < -70:
                jumped = "False"
            if y != 100 and jumped == "True":
                dino.place(x=100, y=y+min_Y, width=64, height=64)
                min_Y -= 0.009
            if y+min_Y < 100 and jumped == "False":
                dino.place(x=100, y=y+min_Y, width=64, height=64)
                min_Y += 0.009
            if round(y + min_Y) == y and jumped == "False":
                jumped = "None"
                break
            window.update()
    thread = threading.Thread(target=jump)
    thread.setName("jump_process")
    thread.start()


#Создание и настройка окна
window = tkinter.Tk()
window.geometry("400x140")
window.title("Python Дино")
window.resizable(width=False, height=False)
#Загрузка изображений
dino_img1 = ImageTk.PhotoImage(Image.open("images/dino.png"))
dino_img2 = ImageTk.PhotoImage(Image.open("images/dino1.png"))
cactos_img = ImageTk.PhotoImage(Image.open("images/dino_cactos.png"))
ground_img = ImageTk.PhotoImage(Image.open("images/ground.png"))
pterodaktel_img = ImageTk.PhotoImage(Image.open("images/pterodaktel.png"))
stone_img = ImageTk.PhotoImage(Image.open("images/stone.png"))
#Загрузка звука
death_sound = 'sounds/hitHurt.wav'
jump_sound = 'sounds/jump.wav'
#Создание объектов игры
dino = Label(window)
ground = Label(window,image=ground_img)
ground.place(x=0,y=119,width=717,height=23)
cactos = Label(window, image = cactos_img)
pterodaktel = Label(window,image=pterodaktel_img)
info = Label(window, text="None",font=("MS Sans Serif bold",10))
btn = Button(text="Начать занаво!",command=reply_game)
info.place(x=180,y=0,width=300,height=15)
cactos.place(x=cactos_spawnX,y=y+12,width=26,height=47)
dino.place(x=100,y=y,width=64,height=64)
pterodaktel.place(x=100,y=20,width=42,height=26)
#Бинды
window.bind("<space>",jump_th)
window.after(1000, cactos_moving)
window.after(1000, death)
window.after(1000, dino_animation)
window.after(1000, pterodaktel_moving)
#Создание камней
stone = ""
for i in range(3):
    stone = "stone"+str(i)
    stone = Label(window,image=stone_img)
    stones.append(stone)
    stone.place(x=randint(0,400),y=randint(123,140),width=10,height=6)
window.mainloop()
#Author Stepan4ek