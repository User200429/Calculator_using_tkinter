import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("200x300")
root.resizable(False,False)

# Setting up a top frame
frame1 = tk.Frame(root,width=200,height=50,bg="lightgrey")
frame1.pack()
frame1.pack_propagate(False)
output_display = tk.Label(frame1,text="",bg="lightpink")
output_display.place(relx=.025,rely=0.1,relwidth=0.950,relheight=0.8)

#Setting up a bottom frame
frame2 = tk.Frame(root,width=200,height=250,bg="black")
frame2.pack(fill="both",expand=True)#fill="both",expand=True

# Action 

def clear():
    output_display.config(text = "")
def backspace():
    t =  output_display["text"]
    output_display.config(text =t[:-1])
def number_operators(n):
    t =  output_display.cget("text")
    output_display.config(text =t+str(n))
def answer():
    t = output_display.cget("text")
    try:
        result =eval(t)
        output_display.config(text =str(result))
    except:
        output_display.config(text ="ERROR")


# setting up buttons
b01 = tk.Button(frame2,text="Clear",command=clear,bg="green").grid(row = "0",column = "0",sticky = "nsew")
b02 = tk.Button(frame2,text="%",command= lambda:number_operators("%")).grid(row = 0,column = 1,sticky = "nsew")
b03 = tk.Button(frame2,text="<-",command= backspace).grid(row = 0,column = 2,sticky = "nsew")
b04 = tk.Button(frame2,text="/",command= lambda:number_operators("/")).grid(row = 0,column = 3,sticky = "nsew")

b11 = tk.Button(frame2,text="7",command= lambda:number_operators("7")).grid(row = 1,column = 0,sticky = "nsew")
b12 = tk.Button(frame2,text="8",command= lambda:number_operators("8")).grid(row = 1,column = 1,sticky = "nsew")
b13 = tk.Button(frame2,text="9",command= lambda:number_operators("9")).grid(row = 1,column = 2,sticky = "nsew")
b14 = tk.Button(frame2,text="*",command= lambda:number_operators("*")).grid(row = 1,column = 3,sticky = "nsew")

b21 = tk.Button(frame2,text="4",command= lambda:number_operators("4")).grid(row = 2,column = 0,sticky = "nsew")
b22 = tk.Button(frame2,text="5",command= lambda:number_operators("5")).grid(row = 2,column = 1,sticky = "nsew")
b23 = tk.Button(frame2,text="6",command= lambda:number_operators("6")).grid(row = 2,column = 2,sticky = "nsew")
b24 = tk.Button(frame2,text="-",command= lambda:number_operators("-")).grid(row = 2,column = 3,sticky = "nsew")

b31 = tk.Button(frame2,text="1",command= lambda:number_operators("1")).grid(row = 3,column = 0,sticky = "nsew")
b32 = tk.Button(frame2,text="2",command= lambda:number_operators("2")).grid(row = 3,column = 1,sticky = "nsew")
b33 = tk.Button(frame2,text="3",command= lambda:number_operators("3")).grid(row = 3,column = 2,sticky = "nsew")
b34 = tk.Button(frame2,text="+",command= lambda:number_operators("+")).grid(row = 3,column = 3,sticky = "nsew")

b31 = tk.Button(frame2,text="00",command= lambda:number_operators("00")).grid(row = 4,column = 0,sticky = "nsew")
b32 = tk.Button(frame2,text="0",command= lambda:number_operators("0")).grid(row = 4,column = 1,sticky = "nsew")
b33 = tk.Button(frame2,text=".",command= lambda:number_operators(".")).grid(row = 4,column = 2,sticky = "nsew")
b34 = tk.Button(frame2,text="=",command= answer).grid(row = 4,column = 3,sticky = "nsew")

# making the button take up space
total_row = 5
total_col= 4
for i in range(total_row):
    frame2.rowconfigure(i,weight = 1)
for i in range(total_col):
    frame2.columnconfigure(i,weight = 1)


root.mainloop()
