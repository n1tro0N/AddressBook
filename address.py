import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning


root = Tk()
root.geometry('1920x1080')
root.config(bg= '#292929')
datas = []

def add():
	global datas
	if Name.get(). strip() == "" or Number.get().strip() == "" or address.get(1.0, "end-1c") == "":
		showwarning(title="Error", message="Enter value")
	else:
		datas.append([Name.get(),Number.get(),address.get(1.0, "end-1c")])
		update_book()

		table.insert('', tkinter.END, values=(Name.get(),Number.get(),address.get(1.0, "end-1c")))


def view():
	Name.set(datas[int(select.curselection()[0])][0])
	Number.set(datas[int(select.curselection()[0])][1])
	address.delete(1.0,"end")
	address.insert(1.0, datas[int(select.curselection()[0])][2])


def delete():
	print(table.delete(table.focus()))
	del datas[int(select.curselection()[0])]
	update_book()


def reset():
	Name.set('')
	Number.set('')
	address.delete(1.0,"end")


def update_book():
	select.delete(0,END)
	for n,p,a in datas:
		select.insert(END, n)


Name = StringVar()
Number = StringVar()

frame = Frame()
frame.pack(pady=10)

frame1 = Frame()
frame1.pack()

frame2 = Frame()
frame2.pack(pady=10)

Label(frame, text = 'Name: ', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable = Name,width=50).pack()

Label(frame1, text = 'Number: ', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable = Number,width=50).pack()

Label(frame2, text = 'Address: ', font='arial 12 bold').pack(side=LEFT)
address = Text(frame2,width=37,height=10)
address.pack()

Button(root,text="Add          ",font="arial 12 bold",command=add, bg='#ffd700').place(x= 100, y=270)
Button(root,text="View         ",font="arial 12 bold",command=view, bg='#ffd700').place(x= 100, y=310)
Button(root,text="Delete      ",font="arial 12 bold",command=delete, bg='#ffd700').place(x= 100, y=350)
Button(root,text="Reset       ",font="arial 12 bold",command=reset, bg='#ffd700').place(x= 100, y=390)

scroll_bar = Scrollbar(root, orient=VERTICAL, bg='black')
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200,y=260)

table_frame = tkinter.Frame(root)
table_frame.place(relx=0.22,rely= 0.30,relwidth=0.60,relheight=0.3)
table = ttk.Treeview(table_frame, selectmode=tkinter.BROWSE, columns=('Name', 'Number', 'Address'))

X_Scroller = tkinter.Scrollbar(table, orient=tkinter.HORIZONTAL, command=table.xview)
Y_Scroller = tkinter.Scrollbar(table, orient=tkinter.VERTICAL, command=table.yview)
X_Scroller.pack(side=tkinter.BOTTOM, fill=tkinter.X)
Y_Scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

table.config(yscrollcommand=Y_Scroller.set, xscrollcommand=X_Scroller.set)

table.heading('Name', text='Name', anchor=tkinter.CENTER)
table.heading('Number', text='Number', anchor=tkinter.CENTER)
table.heading('Address', text='Address', anchor=tkinter.CENTER)

table.column('#0', width=0, stretch=tkinter.NO)
table.column('#1', width=200, stretch=tkinter.NO)
table.column('#2', width=200, stretch=tkinter.NO)


table.place(relx=0,y=0, relheight=1, relwidth=1)


root.mainloop()