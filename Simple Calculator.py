import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("330x380")
root.resizable(False, False)
root.configure(bg="#2c3e50")  # Dark gray-blue background

# Calculator variables
display_text = "0"
first_number = 0
operation = ""
waiting_for_number = True

def update_display():
    """Update the calculator display"""
    display_label.config(text=display_text)

def button_click(number):
    global display_text, waiting_for_number

    if waiting_for_number or display_text == "0":
        display_text = str(number)
        waiting_for_number = False
    else:
        display_text += str(number)

    update_display()

def operation_click(op):
    global first_number, operation, waiting_for_number, display_text

    if operation != "" and not waiting_for_number:
        calculate_now()

    first_number = float(display_text)
    operation = op
    waiting_for_number = True

def calculate_now():
    global display_text, first_number, operation

    try:
        second_number = float(display_text)

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "×":
            result = first_number * second_number
        elif operation == "÷":
            if second_number == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                click_clear()
                return
            result = first_number / second_number

        if result == int(result):
            display_text = str(int(result))
        else:
            display_text = str(round(result, 8))

        update_display()

    except:
        messagebox.showerror("Error", "Invalid calculation!")
        click_clear()

def click_equals():
    global operation, waiting_for_number

    if operation == "":
        return

    calculate_now()
    operation = ""
    waiting_for_number = True

def click_clear():
    global display_text, first_number, operation, waiting_for_number
    display_text = "0"
    first_number = 0
    operation = ""
    waiting_for_number = True
    update_display()

def click_backspace():
    global display_text, waiting_for_number

    if len(display_text) > 1:
        display_text = display_text[:-1]
    else:
        display_text = "0"
        waiting_for_number = True

    update_display()

# Button handlers
def click_0(): button_click(0)
def click_1(): button_click(1)
def click_2(): button_click(2)
def click_3(): button_click(3)
def click_4(): button_click(4)
def click_5(): button_click(5)
def click_6(): button_click(6)
def click_7(): button_click(7)
def click_8(): button_click(8)
def click_9(): button_click(9)
def click_dot(): button_click(".")
def click_plus(): operation_click("+")
def click_minus(): operation_click("-")
def click_multiply(): operation_click("×")
def click_divide(): operation_click("÷")

# Display
display_label = tk.Label(root, text="0", font=("Arial", 20),
                         bg="#ecf0f1", fg="#2c3e50", width=15, height=2,
                         relief="sunken", anchor="e")
display_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5,
                   sticky="ew")

# Row 1: C, ⌫, (empty), ÷
tk.Button(root, text="C", command=click_clear, width=5, height=2,
          font=("Arial", 14), bg="#e74c3c", fg="white").grid(row=1, column=0, padx=2, pady=2)
tk.Button(root, text="⌫", command=click_backspace, width=5, height=2,
          font=("Arial", 14), bg="#e67e22", fg="white").grid(row=1, column=1, padx=2, pady=2)
tk.Label(root, text="", width=5, height=2, bg="#2c3e50").grid(row=1, column=2, padx=2, pady=2)
tk.Button(root, text="÷", command=click_divide, width=5, height=2,
          font=("Arial", 14), bg="#34495e", fg="white").grid(row=1, column=3, padx=2, pady=2)

# Row 2
tk.Button(root, text="7", command=click_7, width=5, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=2, column=0, padx=2, pady=2)
tk.Button(root, text="8", command=click_8, width=5, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=2, column=1, padx=2, pady=2)
tk.Button(root, text="9", command=click_9, width=5, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=2, column=2, padx=2, pady=2)
tk.Button(root, text="×", command=click_multiply, width=5, height=2,
          font=("Arial", 14), bg="#34495e", fg="white").grid(row=2, column=3, padx=2, pady=2)

# Row 3
tk.Button(root, text="4", command=click_4, width=5, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=3, column=0, padx=2, pady=2)
tk.Button(root, text="5", command=click_5, width=5, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=3, column=1, padx=2, pady=2)
tk.Button(root, text="6", command=click_6, width=5, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=3, column=2, padx=2, pady=2)
tk.Button(root, text="-", command=click_minus, width=5, height=2,
          font=("Arial", 14), bg="#34495e", fg="white").grid(row=3, column=3, padx=2, pady=2)

# Row 4
tk.Button(root, text="1", command=click_1, width=5, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=4, column=0, padx=2, pady=2)
tk.Button(root, text="2", command=click_2, width=5, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=4, column=1, padx=2, pady=2)
tk.Button(root, text="3", command=click_3, width=5, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=4, column=2, padx=2, pady=2)
tk.Button(root, text="+", command=click_plus, width=5, height=2,
          font=("Arial", 14), bg="#34495e", fg="white").grid(row=4, column=3, padx=2, pady=2)

# Row 5
tk.Button(root, text="0", command=click_0, width=12, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=5, column=0, columnspan=2, padx=2, pady=2, sticky="ew")
tk.Button(root, text=".", command=click_dot, width=5, height=2,
          font=("Arial", 14), bg="#95a5a6").grid(row=5, column=2, padx=2, pady=2)
tk.Button(root, text="=", command=click_equals, width=5, height=2,
          font=("Arial", 14), bg="#27ae60", fg="white").grid(row=5, column=3, padx=2, pady=2)

# Initialize display
update_display()

# Info message
messagebox.showinfo("Simple Calculator",
                    "Calculator is ready!\n\n"
                    "✅ Continuous calculation supported!\n"
                    "Example: 4 + 5 + 3 = 12\n"
                    "Enjoy!")

# Start the calculator
root.mainloop()
