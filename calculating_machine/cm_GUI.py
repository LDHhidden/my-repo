import tkinter as tk
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "test.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

def insert_name():
    text=name_entry.get()
    print(type(text))
    cursor.execute("INSERT INTO users (username) VALUES (?);", [text])
    connection.commit()
    connection.close()

root = tk.Tk()
root.title("채무계산기")
root.geometry("500x500")
root.resizable(True,True)

# 이름 입력 레이아웃
name_frame = tk.Frame(root,relief="solid", bd=3, padx=15, pady=15)
name_frame.pack(side="top",fill="x")

name_label = tk.Label(name_frame,text="이름 :")
name_label.grid(row=0,column=0)

name_entry = tk.Entry(name_frame,)
name_entry.grid(row=0,column=1)

name_btn = tk.Button(name_frame, text="이름입력",command=insert_name)
name_btn.grid(row=0,column=2)

# 숫자 입력창 레이아웃
num_en_fram = tk.Frame(root, relief="solid", bd=3, padx=15,pady=15)
num_en_fram.pack(side="top", fill="x")

num_entry = tk.Entry(num_en_fram,)
num_entry.grid(row=0, column=0)

# 숫자 버튼 레이아웃
num_btn_frame = tk.Frame(root, relief="solid", bd=3, padx=15, pady=150)
num_btn_frame.pack(side="top", fill="x")

num_btn = tk.Button(num_btn_frame, text="1")
num_btn.grid(row=0,column=0)
root.mainloop()