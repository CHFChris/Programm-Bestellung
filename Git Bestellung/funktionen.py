import tkinter

window = tkinter.Tk()
window.title("Bestellungen")
window.geometry("600x400")

textentry = tkinter.Entry(window, width=50)
textentry.pack()

task_listbox = tkinter.Listbox(window, width=80, height=15)
task_listbox.pack()

window.mainloop()
