import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import io
from PIL import Image
import requests
from tkinter import messagebox
import os
import json
import pandas as pd
import plotly.express as px

ctk.CTkLabel(app, text="Crypto Wallet", font=("Arial", 24, "bold")).pack(pady=10)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Crypto Wallet")
app.geometry("1100x900")
search_entry = ctk.CTkEntry(app, placeholder_text="Search for a coin...")
search_entry.pack(pady=5)
search_entry.bind("<KeyRelease>", search_coin)

search_results = tk.Listbox(app, height=6, width=40)
search_results.pack()
summary_label = ctk.CTkLabel(app, text="Wallet Summary Loading...", font=("Arial", 16))
summary_label.pack(pady=10)
search_results.bind("<<ListboxSelect>>", select_coin)
coin_logo = ctk.CTkLabel(app, text="")
coin_logo.pack()
coin_info = ctk.CTkLabel(app, text="Select a coin to view details", font=("Arial", 14))
coin_info.pack(pady=5)
amount_entry = ctk.CTkEntry(app, placeholder_text="Amount")
amount_entry.pack(pady=2)
price_entry = ctk.CTkEntry(app, placeholder_text="Buy Price")
price_entry.pack(pady=2)
add_button = ctk.CTkButton(app, text="Add Coin", command=add_coin)
add_button.pack(pady=5)
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)
ctk.CTkLabel(app, text="Sort By:", font=("Arial", 12)).pack(pady=5)


sort_names = {
    "name": "Coin Name",
    "current_price": "Current Price",
    "amount": "Amount",
    "profit": "Profit / Loss",
    "change_24h": "24h Change"
}

sort_menu = ctk.CTkOptionMenu(app, values=list(sort_names.keys()), variable=sort_option, command=lambda x: update_table())
sort_menu.pack()

columns = ("Coin", "Amount", "Buy Price", "Current Price", "Profit", "24h Change", "Total")
table = ttk.Treeview(app, columns=columns, show="headings", height=10)
for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor=tk.CENTER, width=120)
table.pack(pady=10)


ctk.CTkButton(button_frame, text="Add Coin", command=add_coin).grid(row=0, column=0, padx=5)
ctk.CTkButton(button_frame, text="Delete", command=delete_coin).grid(row=0, column=1, padx=5)
ctk.CTkButton(button_frame, text="Update Prices", command=update_prices).grid(row=0, column=2, padx=5)
ctk.CTkButton(button_frame, text="Pie Chart", command=show_pie_chart).grid(row=0, column=3, padx=5)


portfolio = []
coin_list = []
selected_coin = {}
sort_option = tk.StringVar(value="name")

def load_portfolio():
    global portfolio
    if os.path.exists("wallet.json"):
        with open("wallet.json", "r") as f:
            portfolio = json.load(f)

def save_portfolio():
    with open("wallet.json", "w") as f:
        json.dump(portfolio, f)

def update_table():
    for row in table.get_children():
        table.delete(row)

    sorted_data = sorted(portfolio, key=lambda x: x.get(sort_option.get(), 0), reverse=True)

    for item in sorted_data:
        current_price = item.get("current_price", 0)
        profit = item.get("profit", 0)
        change_24h = item.get("change_24h", 0)
        total_value = item["amount"] * current_price

        table.insert("", tk.END, values=(
            item["name"],
            f"{item['amount']:.4f}",
            f"${item['buy_price']:.2f}",
            f"${current_price:.2f}",
            f"${profit:.2f}",
            f"{change_24h:.2f}%",
            f"${total_value:.2f}"
        ))

def update_summary():
    if not portfolio:
        summary_label.configure(text="Wallet is empty.")
        return

    total_value = sum(item.get("amount", 0) * item.get("current_price", 0) for item in portfolio)
    total_profit = sum(item.get("profit", 0) for item in portfolio)
    change_24h = sum(item.get("change_24h", 0) * item.get("amount", 0) for item in portfolio)

    summary_label.configure(text=f"Total Wallet Value: ${total_value:.2f} | 24h Change: {change_24h:.2f} | Net P/L: ${total_profit:.2f}")

def show_pie_chart():
    if not portfolio:
        messagebox.showinfo("Empty Wallet", "No data available for pie chart.")
        return

    df = pd.DataFrame([{
        "Coin": item["name"],
        "Value": item["amount"] * item.get("current_price", 0)
    } for item in portfolio])

    fig = px.pie(df, names="Coin", values="Value", title="Portfolio Distribution", hole=0.4)
    fig.update_layout(title_font=dict(size=22), font=dict(size=14))
    fig.show()        

def update_prices():
    fetch_coins()
    for item in portfolio:
        for coin in coin_list:
            if coin["id"] == item["id"]:
                item["current_price"] = coin["current_price"]
                item["profit"] = (coin["current_price"] - item["buy_price"]) * item["amount"]
                item["change_24h"] = coin["price_change_percentage_24h"]
                break
    save_portfolio()
    update_table()



def fetch_coins():
    global coin_list
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "per_page": 250,
        "page": 1,
        "price_change_percentage": "24h"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        coin_list = response.json()
    except Exception as e:
        print(f"Error fetching coins: {e}")
def select_coin(event):
    selection = search_results.curselection()
    if not selection:
        return
    coin_name = search_results.get(selection[0])
    for coin in coin_list:
        if coin["name"] == coin_name:
            selected_coin.clear()
            selected_coin.update(coin)
            display_coin_info()
            break

def display_coin_info():
    coin_info.configure(
        text=f"{selected_coin['name']} ({selected_coin['symbol'].upper()})\n"
             f"Price: ${selected_coin['current_price']:.2f} | "
             f"24h: {selected_coin['price_change_percentage_24h']:.2f}%"
    )
    
    img_data = requests.get(selected_coin['image']).content
    img = Image.open(io.BytesIO(img_data)).resize((40, 40))
    img_tk = ctk.CTkImage(light_image=img, dark_image=img, size=(40, 40))
    coin_logo.configure(image=img_tk)

def add_coin():
    if not selected_coin:
        messagebox.showinfo("Select Coin", "Please choose a coin first.")
        return
    try:
        amount_text = amount_entry.get()
        price_text = price_entry.get()
        if not amount_text or not price_text:
            messagebox.showwarning("Missing Input", "Please enter both amount and price.")
            return
        amount = float(amount_text)
        buy_price = float(price_text)
    except:
        messagebox.showerror("Invalid Input", "Amount and Price must be numeric.")
        return


    coin_id = selected_coin["id"]
    for item in portfolio:
        if item["id"] == coin_id:
            item["amount"] += amount
            item["buy_price"] = (item["buy_price"] + buy_price) / 2
            break
    else:
        portfolio.append({
            "id": coin_id,
            "name": selected_coin["name"],
            "amount": amount,
            "buy_price": buy_price,
            "logo": selected_coin["image"]
        })

    save_portfolio()

def delete_coin():
    selected = table.focus()
    if not selected:
        messagebox.showinfo("No Selection", "Please select a coin to delete.")
        return
    index = int(table.index(selected))
    del portfolio[index]
    save_portfolio()
    update_table()



def search_coin(event):
    keyword = search_entry.get().lower()
    search_results.delete(0, tk.END)
    found = False
    for coin in coin_list:
        if keyword in coin["name"].lower() or keyword in coin["symbol"].lower():
            search_results.insert(tk.END, coin["name"])
            found = True
    if not found:
        search_results.insert(tk.END, "No matching coins found")

     
fetch_coins()
load_portfolio()
update_table()
update_summary()
app.mainloop()

