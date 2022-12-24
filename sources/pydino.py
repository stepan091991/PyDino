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
urls_sounds = {
               "HitHurt":"https://downloader.disk.yandex.ru/disk/1b736f6d21d1928ba8f689f7c16c1df43cf6c83b53239b5d37c9615dbd117509/639dc42a/uVwh3DmYREoUvtDLAVplHFA9__RjlN48cb0VDWiB0SADatHXN7mOofpcI0qTKL31KdAlnbHKVK1fssrZ4U3_cA%3D%3D?uid=972608764&filename=hitHurt.wav&disposition=attachment&hash=&limit=0&content_type=audio%2Fx-wav&owner_uid=972608764&fsize=6705&hid=41258f36186b0a7a7b0a6649aa696d7b&media_type=audio&tknv=v2&etag=28fccef258adb085091e8d63cda984e7",
               "jump":"https://downloader.disk.yandex.ru/disk/d77a3885bb6c9684b24c93854390ffc86218831c624761bb57e8aeb625d408e8/639dc438/uVwh3DmYREoUvtDLAVplHFEdNNUl8YlZ79eJ0J8c5WlO9awEn2blCDCskX1LUg7o7uLrOuimMGO9MQG5HPk7KQ%3D%3D?uid=972608764&filename=jump.wav&disposition=attachment&hash=&limit=0&content_type=audio%2Fx-wav&owner_uid=972608764&fsize=3541&hid=6334ce3e118e7ef598dddd3fe3b33999&media_type=audio&tknv=v2&etag=a2602e00e19117bc15442397de2e26e2"
              }
urls = {""
        "dino":"https://downloader.disk.yandex.ru/disk/5d97283ce5d02855279dac0ff8f2343a928436d6696bbb999c980d146e2c8970/639dbf1b/uVwh3DmYREoUvtDLAVplHDrWJWfY5RkTPdVKziN9cGRl6vSIvS6DLAf4qf0enqux6sO47yM1tp_jvy83mSfuug%3D%3D?uid=972608764&filename=dino.png&disposition=attachment&hash=&limit=0&content_type=image%2Fpng&owner_uid=972608764&fsize=425&hid=ff9d77e077ff357e5deb7ef3b7b2a7db&media_type=image&tknv=v2&etag=7fafd228ad4c3f7c83ef7f27d262ae58",
        "dino1":"https://downloader.disk.yandex.ru/disk/c84a614e0823bfde3e2ba6e55e8cc892a706a11c9e48094e294d2a42473f4841/639dbf99/uVwh3DmYREoUvtDLAVplHM9HvxJIZjp0mUmTsV4ytDyhGZNXjIDmyTcwWQGZpPdsmUiip1UYgxv5R54tGNQk5Q%3D%3D?uid=972608764&filename=dino1.png&disposition=attachment&hash=&limit=0&content_type=image%2Fpng&owner_uid=972608764&fsize=448&hid=de4ba51153f2530cab15d7308bc8d702&media_type=image&tknv=v2&etag=ea09453b7ba336f5084480902eb87a2f",
        "dino_cactos":"https://downloader.disk.yandex.ru/disk/83fecfda97c419cee8248e31c733bd7bf1b2eb78256811b7b0dc30f0e2bba28f/639dbfbf/uVwh3DmYREoUvtDLAVplHMQICpef6rZc5FP18pSYY015sSU3TbdqeQ73M-Eom7sWwDRTFWEKlIXJthUOdguzdQ%3D%3D?uid=972608764&filename=dino_cactos.png&disposition=attachment&hash=&limit=0&content_type=image%2Fpng&owner_uid=972608764&fsize=426&hid=84cbf5c725cb5d65bf4f0b5a9140e986&media_type=image&tknv=v2&etag=d6b0ddf29e1987faa76ed8f2a4b0b719",
        "ground":"https://downloader.disk.yandex.ru/disk/c7db01b7ceb24accc7688563241fdc36894dfbe99ee31d01714a7749cac8b5d7/639dc011/uVwh3DmYREoUvtDLAVplHKI-j1SH5I98jfMZd-AiOPK6HvSAMqpTe7T3LghJac9McN4ifounoPWXzoruwJ6BHA%3D%3D?uid=972608764&filename=ground.png&disposition=attachment&hash=&limit=0&content_type=image%2Fpng&owner_uid=972608764&fsize=258&hid=3dcbed66065031001f6a6c8bbc46845a&media_type=image&tknv=v2&etag=02f22b4625d63964fca94d51f262cc30",
        "pterodaktel":"https://downloader.disk.yandex.ru/disk/ae6457c4a13f2d4c51e691f65c6867aef95c29505a95b1d169c42b445f54596a/639dc036/uVwh3DmYREoUvtDLAVplHIJ7OMzMdWhoolGtqJYXNOYu0cofbSIBCEnuIKtLXacQZtX8ydNktRZuXGuSMQLUZw%3D%3D?uid=972608764&filename=pterodaktel.png&disposition=attachment&hash=&limit=0&content_type=image%2Fpng&owner_uid=972608764&fsize=259&hid=20ca34132184265eb861adbcd2f43165&media_type=image&tknv=v2&etag=0e41514abe979084108c03fde2ae785e",
        "stone":"https://downloader.disk.yandex.ru/disk/5ef72e465eee0e9976d75a307e40c8f5e0c63bc66f5be9754f8cca8944ab99eb/639dc04f/uVwh3DmYREoUvtDLAVplHC0aWEYH6RktxGGlzprLFcl2fGCjdMiwOfNJhKJVfBIn61ECwBQfw_TxNEGKczzAZg%3D%3D?uid=972608764&filename=stone.png&disposition=attachment&hash=&limit=0&content_type=image%2Fpng&owner_uid=972608764&fsize=185&hid=772446801eb50491a62c7bcbc3146e2a&media_type=image&tknv=v2&etag=0e2ea9c332f84ae37c47a7966df3bfbd"
        }
if not os.path.isdir("images"):
    os.makedirs("images")
    for img in urls:
        print(f"Загрузка {img}.png")
        p = requests.get(urls[img])
        out = open(f"images/{img}.png", "wb")
        out.write(p.content)
        out.close()
else:
    print("Файлы изображений существуют!")
if not os.path.isdir("sounds"):
    os.makedirs("sounds")
    for sound in urls_sounds:
        print(f"Загрузка {sound}.wav")
        p = requests.get(urls_sounds[sound])
        out = open(f"sounds/{sound}.wav", "wb")
        out.write(p.content)
        out.close()
else:
    print("Файлы звуков существуют!")
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