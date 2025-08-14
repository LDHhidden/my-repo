import tkinter as tk
from tkinter import ttk, messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calc")
        self.resizable(False, False)
        self.expression = tk.StringVar(value="")

        # Display
        style = ttk.Style(self)
        style.configure("TButton", padding=8, font=("SF Pro", 14))
        style.configure("Display.TEntry", padding=10, font=("SF Pro", 22))

        entry = ttk.Entry(self, textvariable=self.expression, justify="right",
                          style="Display.TEntry", width=16)
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=(8, 0))
        entry.focus()

        # Buttons layout
        buttons = [
            ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("÷", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("−", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("(", 5, 2), (")", 5, 3),
            ("=", 6, 0, 4)
        ]

        for item in buttons:
            text, r, c, cs = (item + (1,))[:4]
            btn = ttk.Button(self, text=text, command=lambda t=text: self.on_press(t))
            btn.grid(row=r, column=c, columnspan=cs, sticky="nsew", padx=6, pady=6)

        # Grid weights
        for i in range(7):
            self.rowconfigure(i, weight=1)
        for j in range(4):
            self.columnconfigure(j, weight=1)

        # Keyboard bindings
        self.bind("<Key>", self.on_key)
        self.bind("<Return>", lambda e: self.on_press("="))
        self.bind("<BackSpace>", lambda e: self.on_press("⌫"))
        self.bind("<Escape>", lambda e: self.on_press("C"))

    def on_key(self, event):
        allowed = "0123456789+-*/().%"
        mapping = {"/": "÷", "*": "×", "-": "−"}
        ch = event.char
        if ch in mapping:
            self.on_press(mapping[ch])
        elif ch in allowed:
            self.expression.set(self.expression.get() + ch)

    def on_press(self, char):
        if char == "C":
            self.expression.set("")
        elif char == "⌫":
            self.expression.set(self.expression.get()[:-1])
        elif char == "=":
            try:
                expr = (self.expression.get()
                        .replace("×", "*").replace("÷", "/").replace("−", "-"))
                # Safe-ish eval: no names, no builtins
                result = eval(expr, {"__builtins__": None}, {})
                self.expression.set(str(result))
            except Exception:
                messagebox.showerror("Error", "식이 올바르지 않습니다.")
        else:
            self.expression.set(self.expression.get() + char)

if __name__ == "__main__":
    Calculator().mainloop()
