import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

def func(event):
    print("You hit return.")

root.bind('<Return>', func)

def onclick():
    print("You clicked the button")

button = tk.Button(root, text="click me", command=onclick)
button.pack()

root.mainloop()


# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("300x200")
#
# def func(event):
#     print("You hit return.")
#
# def onclick(event=None):
#     print("You clicked the button")
#
# root.bind('<Return>', onclick)
#
# button = tk.Button(root, text="click me", command=onclick)
# button.pack()
#
# root.mainloop()


# import tkinter as tk
#
# class Application(tk.Frame):
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("300x200")
#
#         tk.Frame.__init__(self, self.root)
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.root.bind('<Return>', self.parse)
#         self.grid()
#
#         self.submit = tk.Button(self, text="Submit")
#         self.submit.bind('<Button-1>', self.parse)
#         self.submit.grid()
#
#     def parse(self, event):
#         print("You clicked?")
#
#     def start(self):
#         self.root.mainloop()
#
#
# Application().start()
