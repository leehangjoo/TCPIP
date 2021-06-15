import tkinter as tk
def add_input():
    f = int(en_first.get())
    s = int(en_second.get())
    lbl_result.configure(text=f+s)

def enter_pressed(e):
    add_input()

w = tk.Tk()
w.title('Event Handling')

w.bind('<Return>',enter_pressed)

btn_add = tk.Button(w, text='더하기', command=add_input)
lbl_result = tk.Label(w, text='결과 출력')
en_first = tk.Entry(w)
en_second = tk.Entry(w)

#Grid 배치
lbl_result.grid(row=0,column=0,columnspan=2)
en_first.grid(row=1,column=0)
en_second.grid(row=1,column=1)
btn_add.grid(row=2,column=0,columnspan=2)

w.mainloop()

