import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Simple Calculator")


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")


entry1 = tk.Entry(root, width=20)
entry2 = tk.Entry(root, width=20)
operator_var = tk.StringVar()
operator_var.set("Addition")  # Default operation
operator_menu = tk.OptionMenu(root, operator_var, "Addition", "Subtraction", "Multiplication", "Division")
calculate_button = tk.Button(root, text="Calculate", command=calculate)
result_label = tk.Label(root, text="Result: ")


entry1.pack(pady=10)
entry2.pack(pady=10)
operator_menu.pack(pady=10)
calculate_button.pack(pady=10)
result_label.pack(pady=10)


root.mainloop()
