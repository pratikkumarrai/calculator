import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {num1} {operation} {num2} = {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x350")
root.configure(bg="#f2f2f2")  # Light gray background
root.resizable(False, False)

# Styles
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Heading
tk.Label(root, text="Simple Calculator", font=("Helvetica", 16, "bold"), fg="#333", bg="#f2f2f2").pack(pady=10)

# Input fields
tk.Label(root, text="Enter first number:", font=label_font, bg="#f2f2f2").pack()
entry_num1 = tk.Entry(root, font=entry_font, bg="#ffffff", fg="#000")
entry_num1.pack(pady=5)

tk.Label(root, text="Enter second number:", font=label_font, bg="#f2f2f2").pack()
entry_num2 = tk.Entry(root, font=entry_font, bg="#ffffff", fg="#000")
entry_num2.pack(pady=5)

# Operation selection
tk.Label(root, text="Select operation:", font=label_font, bg="#f2f2f2").pack()
operation_var = tk.StringVar()
operation_var.set("+")  # Set default value
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.config(font=entry_font, bg="#e6e6e6", fg="#000", width=10)
operation_menu.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", font=button_font, bg="#4CAF50", fg="white", command=calculate).pack(pady=15)

# Result display
result_label = tk.Label(root, text="", font=("Helvetica", 13), fg="#003366", bg="#f2f2f2")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()