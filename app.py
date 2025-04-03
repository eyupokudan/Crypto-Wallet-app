import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
import io
from PIL import Image
import requests

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
search_results.bind("<<ListboxSelect>>", select_coin)
coin_logo = ctk.CTkLabel(app, text="")
coin_logo.pack()
coin_info = ctk.CTkLabel(app, text="Select a coin to view details", font=("Arial", 14))
coin_info.pack(pady=5)
portfolio = []
coin_list = []
selected_coin = {}
sort_option = tk.StringVar(value="name")

def load_portfolio():
    pass

def save_portfolio():
    pass
import requests
import json

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

def search_coin(event):
    keyword = search_entry.get().lower()
    search_results.delete(0, tk.END)
    for coin in coin_list:
        if keyword in coin["name"].lower() or keyword in coin["symbol"].lower():
            search_results.insert(tk.END, coin["name"])
     


app.mainloop()

