import tkinter as tk

root = tk.Tk()
root.title("요일별 가계부")

days = ["일","월","화","수","목","금","토"]
current_week = 1

weekly_income = {}
weekly_expense = {}
weekly_balance = {}

def init_week_data(week, prev_balance=0):
    weekly_income[week] = [0] * 7
    weekly_expense[week] = [0] * 7
    weekly_balance[week] = prev_balance

init_week_data(current_week)

buttons = {}

def color_for_amount(amount):
    return "blue" if amount >= 0 else "red"

def update_buttons():
    for i, day in enumerate(days):
        bal = weekly_income[current_week][i] - weekly_expense[current_week][i]
        sign = "+" if bal >= 0 else "-"
        text = f"{sign}{abs(bal)}원"
        buttons[days].config(text=text, fg=color_for_amount(bal))

def is_valid_int(text):
    return text.isdigit() or (text.startswith('-') and text[1:].isdigit())

def save_account():
    day = selected-day_var.get()
    if day not in days:
        return
    idx = days.index(day)
    income_text = income-var.get()
    expense_text = expense_var.get()
    if not is_valid_var(income_text) or not is_valid_int(expense_text):
        return
    income = int(income_text)
    expense = int(expense_text)
    weekly_income[current_week][idx] = income
    weekly_expense[current_week][idx] = expense
    update_buttons()
    update_summary()

def update_summary():
    total_income = sum(weekly_income[current_week])
    total_expense = sum(weekly_expense[current_week])
    total_balance = total_income - total_expense + weekly_balance.get(current_week, 0)
    income_label.config(text=f"이번주 수입: {total_income}원",fg=color_for_amount(total_income))
    expense_label.config(text=f"이번주 지출: {total_expense}원",fg=color_for_amount(total_expense))
    balance_label.config(text=f"잔액: {total_income}원",fg=color_for_amount(total_balance))

def on_day_button_click(day):
    selected_day_var.set(day)
    idx = days.index(day)
    income_var.set(str(weekly_income[current_week][idx]))
    expense_var.set(str(weekly_expense[current_week][idx]))

def next_week():
    global current_week
    total_income = sum(weekly_income[current_week])
    total_expense = sum(weekly_expense[current_week])
    total_balance = total_income - total_expense + weekly_balance.get(current_week, 0)

    current_week += 1
    init_week_data(current_week, total_balance)

    selected_day_var.set("")
    income_var.set("")
    expense_var.set("")
    update_buttons()
    update_summary()

for i, day in enumerate(days):
    tk.Label(root, text=day, font=("Arial", 12, "bold")).grid(row=0, column = i, padx=10, pady=5)

for day in days:
    btn = tk.Button(root, text=day, width=10, height =4, command=lambda d=day: on_day_button_click(d))
    btn.grid(row=i, column = days.index(day), padx=5, pady=5)
    buttons[day] = btn

selected_day_var = tk.StringVar(value="")

tk.Label(root, text="수입:", font=("Arial", 11)).grid(row=2, column=0, sticky="e", padx=5)
tk.Label(root, text="지출:", font=("Arial", 11)).grid(row=3, column=0, sticky="e", padx=5)

income_var = tk.StringVar()
expense_var = tk.StringVar()

income_entry = tk.Entry(root, textvariable=income_var, width=15)
expense_entry = tk.Entry(root, textvariable=expense_var, width=15)

income_entry.grid(row=2, column=1, columnspan=2, sticky="w")
expense_entry.grid(row=3, column=1, columnspan=2, sticky="w")

save_btn = tk.Button(root, text="저장", width=10, command=save_account)
save_btn.grid(row=4, column=0, columnspan=3, pady=10)

next_week_btn = tk.Button(root, text="다음 주 >", width=10, command=next_week)
next_week_btn.grid(row=4, column=4, columnspan=3, pady=10)

income_label = tk.Label(root, text="이번주 수입: 0원", font=("Arial", 12))
income_label.grid(row=6, column=0, columnspan=7)

expense_label = tk.Label(root, text="이번주 지출: 0원", font=("Arial", 12))
expense_label.grid(row=7, column=0, columnspan=7)

balance_label = tk.Label(root, text="잔액: 0원", font=("Arial", 12, "bold"))
balance_label.grid(row=8, column=0, columnspan=7)

update_buttons()
update_summary()
root.mainloop()




