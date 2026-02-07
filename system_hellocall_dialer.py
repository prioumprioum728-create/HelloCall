import tkinter as tk
from tkinter import messagebox

class DialerApp:
    def __init__(self, master):
        self.master = master
        master.title("HelloCall Dialer")
        master.geometry("250x350")
        master.resizable(False, False)
        
        self.number_var = tk.StringVar()
        
        # Display entry
        self.entry = tk.Entry(master, textvariable=self.number_var, font=("Helvetica", 20), justify="center")
        self.entry.grid(row=0, column=0, columnspan=3, pady=20)
        
        # Dialer buttons
        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('0', 4, 1)
        ]
        
        for (text, row, col) in buttons:
            b = tk.Button(master, text=text, width=5, height=2, font=("Helvetica", 15),
                          command=lambda t=text: self.add_number(t))
            b.grid(row=row, column=col, padx=5, pady=5)
        
        # Call and Backspace buttons
        call_btn = tk.Button(master, text="Call", width=5, height=2, font=("Helvetica", 15), bg="green", fg="white",
                             command=self.call_number)
        call_btn.grid(row=4, column=0, padx=5, pady=5)
        
        back_btn = tk.Button(master, text="⌫", width=5, height=2, font=("Helvetica", 15), bg="red", fg="white",
                             command=self.backspace)
        back_btn.grid(row=4, column=2, padx=5, pady=5)
        
    def add_number(self, num):
        current = self.number_var.get()
        self.number_var.set(current + num)
        
    def backspace(self):
        current = self.number_var.get()
        self.number_var.set(current[:-1])
        
    def call_number(self):
        number = self.number_var.get()
        if number:
            messagebox.showinfo("Calling", f"Dialing {number}...")
            # Here you would integrate real call logic for Android APK
        else:
            messagebox.showwarning("Error", "Enter a number first!")

# Run the app
root = tk.Tk()
app = DialerApp(root)
root.mainloop()
