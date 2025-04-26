import tkinter as tk

def click(event):
    """Handles button clicks and updates the entry field."""
    global calculation

    text = event.widget.cget("text")

    if text == "C":
        calculation = ""
        entry.delete(0, tk.END)
    elif text == "=":
        try:
            result = eval(calculation) # Be cautious with eval() in real-world applications
            entry.delete(0, tk.END)
            entry.insert(0, result)
            calculation = str(result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
            calculation = ""
    elif text == "%":
        try:
            current_value = float(entry.get())
            percentage = current_value / 100
            entry.delete(0, tk.END)
            entry.insert(0, percentage)
            calculation = str(percentage)
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
            calculation = ""
    elif text in ["+", "-", "*", "/"]:
        if calculation and calculation[-1] in ["+", "-", "*", "/"]:
            calculation = calculation[:-1] + text # Replace the last operator
        else:
            calculation += text
        entry.insert(tk.END, text)
    elif text == ".":
        if "." not in entry.get():
            entry.insert(tk.END, text)
            calculation += text
    elif text.isdigit():
        entry.insert(tk.END, text)
        calculation += text

def main():
    global entry, calculation
    window = tk.Tk()
    window.title("Dheer's calculator")
    window.configure(bg="#222222")

    calculation = "" # String to store the calculation

    # Entry field for displaying numbers and results
    entry = tk.Entry(window, width=18, borderwidth=5, font=("Arial", 24), justify='right',
                     bg="#333333", fg="white", highlightbackground="#333333", highlightcolor="#333333", insertbackground="white")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

    button_font = ("Arial", 20)
    button_bg = "#444444"
    button_fg = "white"
    special_button_bg = "#555555"
    equal_button_bg = "#666666"

    buttons_data = [
        {"text": "C", "bg": special_button_bg},
        {"text": "%", "bg": special_button_bg},
        {"text": "/", "bg": special_button_bg},
        {"text": "*", "bg": button_bg},
        {"text": "7", "bg": button_bg},
        {"text": "8", "bg": button_bg},
        {"text": "9", "bg": button_bg},
        {"text": "-", "bg": button_bg},
        {"text": "4", "bg": button_bg},
        {"text": "5", "bg": button_bg},
        {"text": "6", "bg": button_bg},
        {"text": "+", "bg": button_bg},
        {"text": "1", "bg": button_bg},
        {"text": "2", "bg": button_bg},
        {"text": "3", "bg": button_bg},
        {"text": "=", "bg": equal_button_bg},
        {"text": "0", "bg": button_bg, "columnspan": 2},
        {"text": ".", "bg": button_bg},
        {"text": "", "bg": window["bg"]}
    ]

    row_val = 1
    col_val = 0

    for button_info in buttons_data:
        text = button_info["text"]
        bg_color = button_info["bg"]
        columnspan = button_info.get("columnspan", 1)

        button = tk.Button(window, text=text, padx=25, pady=25, font=button_font,
                           bg=bg_color, fg=button_fg, borderwidth=0, relief="flat", command=lambda t=text: click_handler(t)) # Use command
        button.grid(row=row_val, column=col_val, columnspan=columnspan, padx=5, pady=5, sticky="nsew")

        col_val += columnspan
        if col_val > 3:
            col_val = 0
            row_val += 1

        if text != "0" and text != "":
            if col_val > 3:
                col_val = 0
                row_val += 1

    for i in range(5):
        window.grid_rowconfigure(i, weight=1)
        window.grid_columnconfigure(i, weight=1)

    window.mainloop()

def click_handler(text):
    """Handles button clicks and updates the entry field."""
    global calculation

    if text == "C":
        calculation = ""
        entry.delete(0, tk.END)
    elif text == "=":
        try:
            result = eval(calculation) # Be cautious with eval() in real-world applications
            entry.delete(0, tk.END)
            entry.insert(0, result)
            calculation = str(result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
            calculation = ""
    elif text == "%":
        try:
            current_value = float(entry.get())
            percentage = current_value / 100
            entry.delete(0, tk.END)
            entry.insert(0, percentage)
            calculation = str(percentage)
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
            calculation = ""
    elif text in ["+", "-", "*", "/"]:
        if calculation and calculation[-1] in ["+", "-", "*", "/"]:
            calculation = calculation[:-1] + text # Replace the last operator
        else:
            calculation += text
        entry.insert(tk.END, text)
    elif text == ".":
        if "." not in entry.get():
            entry.insert(tk.END, text)
            calculation += text
    elif text.isdigit():
        entry.insert(tk.END, text)
        calculation += text

if __name__ == "__main__":
    main()