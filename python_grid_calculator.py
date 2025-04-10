import tkinter as tk
root = tk.Tk()
root.title("calculator")
root.geometry("200x300")
root.resizable(False,False)

frame1 = tk.Frame(root,height=50,bg="lightgrey")
frame1.pack(fill="both")
frame1.pack_propagate()
display = tk.Label(frame1,text="",bg="lightpink")
display.place(relx = 0.025,rely=.1,relwidth=.95,relheight=.8)

frame2 = tk.Frame(root,height=200)
frame2.pack(expand=True,fill="both")

def action(c):
    current = str(display["text"])
    if c == "Clear":
        display["text"]=""
    elif c == "<-":
        display["text"]=current[:-1]
    elif c == "=":
        try:
            result = eval(current)
            display["text"]=result
        except:
            display["text"] ="Error"
    else:
        display["text"] = current + str(c)

button = [
    ["Clear","<-","%","/"],
    ["7","8","9","*"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["00","0",".","="]
]
for r,row in enumerate(button):
    for c,coumn in enumerate(row):
        if coumn == "":
            continue
        else:
            b = tk.Button(frame2,text = coumn,command = lambda cik = str(coumn) : action(cik)).grid(row=r,column=c,sticky="snew")
total_row = len(button)
total_col = len(button[0])
for i in range(total_row):
    frame2.rowconfigure(i,weight=1)
for i in range(total_col):
    frame2.columnconfigure(i,weight=1)
root.mainloop()
