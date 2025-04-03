import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox


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

def search_coin(event):
    keyword = search_entry.get().lower()
    search_results.delete(0, tk.END)
    for coin in coin_list:
        if keyword in coin["name"].lower() or keyword in coin["symbol"].lower():
            search_results.insert(tk.END, coin["name"])
     


app.mainloop()

