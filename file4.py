import tkinter as tk
from tkinter import messagebox

def bmi_calc(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_classify(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "obesity"

def main():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = bmi_calc(weight, height)
        category = bmi_classify(bmi)
        result_label.config(text=f"Your BMI is {bmi:.2f}. You are {category}.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for weight and height.")

# Create the main application window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")

# Create and place the labels and entry widgets
tk.Label(root, text="Enter weight of the person (kg):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter height of the person (m):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to generate BMI
generate_button = tk.Button(root, text="Generate BMI", command=main)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
