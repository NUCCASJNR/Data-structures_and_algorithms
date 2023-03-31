import tkinter as tk

window = tk.Tk()
window.title("My first GUI")
window.geometry("300x300")
l = tk.Label(window, text="Hello, world!", bg="green", font=("Arial", 12), width=15, height=2)
l.pack()
window.mainloop()