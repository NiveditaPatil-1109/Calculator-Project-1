from tkinter import *
import math as m

# some useful variables
font = ("Arial", 15, "bold")

# important functions

def back():
    ex=textfield.get()
    ex = ex[0:len(ex)-1]
    textfield.delete(0, END)
    textfield.insert(0,ex)



def clear():
    textfield.delete(0, END)


def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b["text"]
    print(text)

    if text == "=":
        ex = textfield.get()
        answer = eval(ex)
        textfield.delete(0,END)
        textfield.insert(0, answer)
        return
    

    textfield.insert(END,text)
# creating a window
window=Tk()
window.title("My Calculator")
window.geometry("320x300")

# text field
textfield = Entry(window, font=font, justify= RIGHT, bg="yellow")
textfield.pack(side=TOP, pady=10, fill=X, padx=10)

# buttons

ButtonFrame = Frame(window, bg= "orange")
ButtonFrame.pack(side=TOP)

# adding button
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn = Button(ButtonFrame, text=str(temp), font=font, width=5, relief= RAISED, bg= "powder blue", activebackground="violet")
        btn.grid(row=i, column=j, padx=4, pady=4)
        temp=temp+1
        btn.bind("<Button-1>", click_btn_function)

zeroBtn = Button(ButtonFrame, text="0", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
zeroBtn.grid(row=3, column=0, padx=3, pady=3)

dotBtn = Button(ButtonFrame, text=".", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
dotBtn.grid(row=3, column=1, padx=3, pady=3)

equalBtn = Button(ButtonFrame, text="=", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
equalBtn.grid(row=3, column=2, padx=3, pady=3)

plusBtn = Button(ButtonFrame, text="+", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
plusBtn.grid(row=0, column=3, padx=3, pady=3)

minusBtn = Button(ButtonFrame, text="-", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
minusBtn.grid(row=1, column=3, padx=3, pady=3)

multBtn = Button(ButtonFrame, text="*", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
multBtn.grid(row=2, column=3, padx=3, pady=3)

divideBtn = Button(ButtonFrame, text="/", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
divideBtn.grid(row=3, column=3, padx=3, pady=3)

backBtn = Button(ButtonFrame, text="<--", font=font, width=11, relief=RAISED, bg= "powder blue", activebackground="violet", command=back)
backBtn.grid(row=4, column=0, padx=3, pady=3, columnspan=2)

clearBtn = Button(ButtonFrame, text="c", font=font, width=11, relief=RAISED, bg= "powder blue", activebackground="violet", command= clear)
clearBtn.grid(row=4, column=2, padx=3, pady=3, columnspan=2)

# binding all Buttons

plusBtn.bind("<Button-1>", click_btn_function)
minusBtn.bind("<Button-1>", click_btn_function)
multBtn.bind("<Button-1>", click_btn_function)  
divideBtn.bind("<Button-1>", click_btn_function)
zeroBtn.bind("<Button-1>", click_btn_function)
dotBtn.bind("<Button-1>", click_btn_function)
equalBtn.bind("<Button-1>", click_btn_function)

def enterclick(event):
    print("hi")
    e = Event()
    e.widget = equalBtn
    click_btn_function(e)



window.bind("<Return>", enterclick)



# Scienific Mode

# Functions

scFrame= Frame(window, bg="orange")

sqrtBtn = Button(scFrame, text="√", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
sqrtBtn.grid(row=0, column=0, padx=4, pady=3)

powBtn = Button(scFrame, text="^", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
powBtn.grid(row=0, column=1, padx=4, pady=3)

factBtn = Button(scFrame, text="x!", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
factBtn.grid(row=0, column=2, padx=4, pady=3)

radBtn = Button(scFrame, text="toRad", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
radBtn.grid(row=0, column=3, padx=4, pady=3)

degBtn = Button(scFrame, text="toDeg", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
degBtn.grid(row=1, column=0, padx=4, pady=3)

sinBtn = Button(scFrame, text="sinꝋ", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
sinBtn.grid(row=1, column=1, padx=4, pady=3)

cosBtn = Button(scFrame, text="cosꝋ", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
cosBtn.grid(row=1, column=2, padx=4, pady=3)

tanBtn = Button(scFrame, text="tanꝋ", font=font, width=5, relief=RAISED, bg= "powder blue", activebackground="violet")
tanBtn.grid(row=1, column=3, padx=4, pady=3)

normalcalc = True

def calculate_sc(event):
    print("btn..")
    btn=event.widget
    text=btn["text"]
    print(text)
    ex=textfield.get()
    if text== "toDeg":
        print("cal degree")
        answer = str(m.degrees(float(ex)))
    elif text== "toRad":
        print("radian")
        answer = str(m.radians(float(ex)))
    elif text== "x!":
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text== "sinꝋ":
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text== "cosꝋ":
        answer = str(m.cos(m.radians(int(ex))))
    elif text== "tanꝋ":
        answer = str(m.tan(m.radians(int(ex))))
    elif text== "√":
        print("sqrt")
        answer = m.sqrt(int(ex))
    elif text== "^":
        print("pow")
        base,pow= ex.split(",")
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))



    textfield.delete(0, END)
    textfield.insert(0,answer)


def sc_click():
    global normalcalc
    if normalcalc:
        ButtonFrame.pack_forget()
        # add sc frame
        scFrame.pack(side= TOP, pady=10)
        ButtonFrame.pack(side= TOP)
        window.geometry("320x420")
        print("show sc")
        normalcalc= False
    else:
        print("show normal")
        scFrame.pack_forget()
        window.geometry("320x300")
        normalcalc =True






# end functions

# binding scientific buttons
sqrtBtn.bind("<Button-1>",calculate_sc)
powBtn.bind("<Button-1>",calculate_sc)
factBtn.bind("<Button-1>",calculate_sc)
radBtn.bind("<Button-1>",calculate_sc)
degBtn.bind("<Button-1>",calculate_sc)
sinBtn.bind("<Button-1>",calculate_sc)
cosBtn.bind("<Button-1>",calculate_sc)
tanBtn.bind("<Button-1>",calculate_sc)





menubar=Menu(window)
mode= Menu(menubar, font=10, tearoff=0)
mode.add_checkbutton(label="Scientific Calculator", command=sc_click)

menubar.add_cascade(label="Mode", menu=mode)

window.config(menu=menubar)






window.mainloop()