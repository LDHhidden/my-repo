import tkinter as tk
import tkinter.messagebox as box

def click():
    print("클릭했습니다.")
    label.config(text=text.get("1.0",tk.END)) # text.get("1.0",tk.END) - 텍스트 위젯 메세지 가져오기
    box.showinfo("알림","클릭했습니다.") #box.showinfo(제목,메세지)

def click2():
    button2.config(text="성공입니다.",fg="blue", highlightbackground="green") # config - 위젯의 속성값을 변경
    label.config(text=entry.get()) # entry.get() - 엔트리 위젯 메시지 가져오기

# Tk 객체 생성 (앱의 기본 창)
root = tk.Tk()

root.title("채무 프그램") # title - 창 제목
root.geometry("500x500") # geometry - 창 사이즈
root.resizable(False,False) # resizeable(x,y) - 창 크기 변경 (기본값 - 창 크기 변경 가능)

label = tk.Label(root, text="라벨",width=10,height=5) # tk.Label - 라벨, 옵션(width - 넓이, height - 높이)
label.grid(row=0,column=2)

#frame1 = tk.Frame(root, relief="solid", bd=3,padx=15,pady=15) # tk.Frame - 공간, 레이아웃 설정
#frame1.pack(side="top", fill="x",expand=True)
button1 = tk.Button(root, text="버튼1",padx=10,pady=10,
                   highlightbackground="lightblue",
                   fg="red",command=click) # tk.Button - 버튼, 옵션(padx,pady - 여백크기, bg - 배경색, fg - 글자색) 단, macos에서는 bg를 쓰면 안됨 
button1.grid(row=0,column=0)
#button1.pack()             # command=함수이름 - 위젯이 어떤 동작을 했을 때 실행할 함수를 연결하는 기능

#frame2 = tk.Frame(root, relief="solid", bd=3,padx=15,pady=15)
#frame2.pack(side="top", fill="x",expand=True)
button2 = tk.Button(root, text="버튼2", command=click2)
button2.grid(row=0,column=1)
#button2.pack()

entry = tk.Entry(root,) # tk.Entry - 입력창(한줄만)
entry.insert(0,"엔트리 글자")
entry.grid(row=1,column=0) # .grid 배치할 때 용이하지만 pack과 함께 사용할 수 없다. 같이쓰고 싶다면 frame을 통해 따로 사용해야한다.
#entry.pack()

text = tk.Text(root, width=10, height=5)
text.insert(tk.END,"텍스트를 입력하세요") # tk.Text - 입력창(여러줄)
text.grid(row=1,column=1)
#text.pack()

# 창 실행
root.mainloop()
