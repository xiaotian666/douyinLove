from tkinter import *
from tkinter import messagebox


def closewindow():
    messagebox.showinfo(title="警告",message="不要关闭，好好回答")
    # print("1")
    return 


def closeallwindow():
    window.destroy()


def love():
    love = Toplevel(window)
    love.geometry("300x100+520+200")
    love.title("好巧，我也是！")
    lable = Label(love,text="好巧，我也是",font=("微软雅黑",15))
    lable.pack()
    btn = Button(love,text="确定",width=10,height=2,command = closeallwindow)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW",closelove)

def closelove():
    return

# def closenolove():

def nolove():
    # print("2")
    no_love = Toplevel(window)
    no_love.geometry("300x100+520+200")
    no_love.title("再考虑考虑呗！")
    lable = Label(no_love,text="再考虑考虑呗！",font=("微软雅黑",15))
    lable.pack()
    btn = Button(no_love,text="好的",width=10,height=2,command = no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW",closenolove)

def closenolove():
    # messagebox.showinfo("再考虑一下呗！","再考虑一下呗！")
    nolove()

window = Tk()

window.title("小姐姐你喜欢我吗？")
window.geometry("400x430+500+200")
window.protocol("WM_DELETE_WINDOW",closewindow)

lable = Label(window,text="hey,小姐姐",font=("微软雅黑",13),fg = "red")
lable.grid(row = 0,column = 0)

lable1 = Label(window,text="你喜欢我吗？",font = ("微软雅黑",18))
lable1.grid(row = 1,column = 1,sticky = E)

photo = PhotoImage(file="./biu.png")
imagelable = Label(window,image=photo)
imagelable.grid(row = 2,columnspan = 2)

butt = Button(window,text="喜欢",width = 15,height = 2,command = love)
butt.grid(row = 3,column = 0,sticky = W)

butt1 = Button(window,text="不喜欢",width = 10,command = nolove)
butt1.grid(row = 3,column = 1,sticky = E)

window.mainloop()