from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo

root = Tk()
root.geometry("700x500")
root.title('Викторина "Основы HTML"')

canvas = Canvas(root, width=300, height=375)
girl = PhotoImage(file="девушка1.png")
canvas.create_image(30, 0, anchor=NW, image=girl)
canvas.place(x=350, y=140)

vopros = StringVar()
text = Label(textvariable=vopros, font="30")

start = Label(text="Начать викторину?", font="30")
start.place(x=150, y=50)

count = StringVar()
num_vop = Label(textvariable=count, font="30", bg="pink")


def button_true():  # если верно
    showinfo(title="Верно!", message="Вы ответили правильно.")
    vvod.delete(0, END)
    count_num()
    voprossy()


def button_false():  # если неверно или ошибка
    s = vvod.get()
    if s == "" or s == " " or s.isdigit() == False:
        showerror(title="Ошибка", message="Поле ответа пустое или введена не цифра. Введите цифру ответа.")
        vvod.delete(0, END)
        voprossy()
    else:
        showerror(title="Неверно!", message="Вы ответили неверно.")
        vvod.delete(0, END)
        count_num()
        voprossy()


def start_vic():
    start.place_forget()
    beg.place_forget()
    text.place(x=100, y=50)
    ans1.place(x=200, y=100)
    ans2.place(x=300, y=100)
    ans3.place(x=200, y=150)
    ans4.place(x=300, y=150)
    vvod.place(x=100, y=200)
    btn.place(x=150, y=250)
    num_vop.place(x=100, y=10)
    count.set("1")
    voprossy()


def count_num(): # номер вопроса
    global num
    s = num_vop.cget('text')
    num = int(s)
    num += 1
    count.set(str(num))


def voprossy(): # вопросы
    s = num_vop.cget('text')
    count = int(s)
    if count == 1:
        vopros.set("С помощью какого тега в HTML задаются ссылки?")
        t1.set("1. <a>")
        t2.set("2. <hr>")
        t3.set("3. <br>")
        t4.set("4. <h1>")
    if count == 2:
        vopros.set("Как называется верхнее меню сайта?")
        t1.set("1. footer")
        t2.set("2. main")
        t3.set("3. head")
        t4.set("4. header")
    if count == 3:
        vopros.set("Где размещён основной контент?")
        t1.set("1. body")
        t2.set("2. footer")
        t3.set("3. main")
        t4.set("4. header")
    if count == 4:
        vopros.set("С помощью чего подключают стили документу HTML?")
        t1.set("1. css")
        t2.set("2. json")
        t3.set("3. py")
        t4.set("4. html")
    if count == 5:
        vopros.set("Какой тег отвечает за заголовки?")
        t1.set("1. <h1>")
        t2.set("2. <a>")
        t3.set("3. &nbsp")
        t4.set("4. <div>")
    if count == 6:
        vopros.set("Какой тег пишется в начале документа?")
        t1.set("1. <head>")
        t2.set("2. <html>")
        t3.set("3. <body>")
        t4.set("4. <meta>")
    if count == 7:
        vopros.set("Как прописываются классы в css?")
        t1.set("1. .class")
        t2.set("2. class")
        t3.set("3. href")
        t4.set("4. div class")
    if count == 8:
        vopros.set("С помощью чего указывается путь для изображения?")
        t1.set("1. alt")
        t2.set("2. img")
        t3.set("3. src")
        t4.set("4. scr")
    if count == 9:
        vopros.set("С помощью какого тега создается маркированный список?")
        t1.set("1. <li>")
        t2.set("2. <ul>")
        t3.set("3. <img>")
        t4.set("4. <div>")
    if count == 10:
        vopros.set("Как обозначается закрывающий тег параграфа?")
        t1.set("1. </div>")
        t2.set("2. </html>")
        t3.set("3. </h1>")
        t4.set("4. </p>")


def cheek():  # проверка
    ans = vvod.get()
    s = num_vop.cget('text')
    count = int(s)
    if count == 1:
        if ans == "1":
            button_true()
        else:
            button_false()
    if count == 2:
        if ans == "4":
            button_true()
        else:
            button_false()
    if count == 3:
        if ans == "3":
            button_true()
        else:
            button_false()
    if count == 4:
        if ans == "1":
            button_true()
        else:
            button_false()
    if count == 5:
        if ans == "1":
            button_true()
        else:
            button_false()
    if count == 6:
        if ans == "2":
            button_true()
        else:
            button_false()
    if count == 7:
        if ans == "1":
            button_true()
        else:
            button_false()
    if count == 8:
        if ans == "3":
            button_true()
        else:
            button_false()
    if count == 9:
        if ans == "2":
            button_true()
        else:
            button_false()
    if count == 10:
        if ans == "4":
            button_true()
            conetc()
        else:
            button_false()
            conetc()


def conetc():
    text.place_forget()
    ans1.place_forget()
    ans2.place_forget()
    ans3.place_forget()
    ans4.place_forget()
    btn.place_forget()
    num_vop.place_forget()
    vvod.place_forget()
    con.place(x=100, y=50)
    spr.place(x=150, y=100)


def openfile():
    txtarea.place(x=20, y=150)
    f = open("справка.txt", 'r', encoding="utf-8")
    data = f.read()
    txtarea.insert(END, data)
    f.close()


beg = Button(text="Начать", font="30", command=start_vic, bg="pink")
beg.place(x=200, y=100)
t1 = StringVar()
ans1 = Label(textvariable=t1, font="30")

t2 = StringVar()
ans2 = Label(textvariable=t2, font="30")

t3 = StringVar()
ans3 = Label(textvariable=t3, font="30")

t4 = StringVar()
ans4 = Label(textvariable=t4, font="30")

vvod = Entry(root, width=30, font="30")

btn = Button(text="Ответить", font="30", command=cheek, bg="pink")

con = Label(text="Спасибо за прохождение викторины!", font="30")
spr = Button(text="Ответы и пояснения", font="30", width="20", bg="pink", command=openfile)

txtarea = Text(root, width=50, height=20)

root.mainloop()
