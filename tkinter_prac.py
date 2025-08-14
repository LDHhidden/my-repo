import tkinter as tk

root=tk.Tk()
root.geometry("500x500")
"""
tk.Label(root, text="위").pack(side="top")
tk.Label(root, text="아래").pack(side="bottom")
tk.Label(root, text="왼쪽").pack(side="left")
tk.Label(root, text="오른쪽").pack(side="right")"""

tk.Label(root, text="이름").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)
tk.Label(root, text="나이").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)
root.mainloop()

