# Crypto-Wallet-app
-	A real-time crypto wallet tracker application using Python.

GitHub Repository
The source code for this project is available on GitHub:
“https://github.com/eyupokudan/Crypto-Wallet-app” 
Identification
Name: Eyup Ensar Okudan
P-number: P476460
Course code: IY499
Declaration of Own Work
I confirm that this assignment is my own work.  
Where I have used external code or sources, I have cited them appropriately.
 Introduction 
In this project, I enable people to track their cryptocurrencies from a single place. People who are interested in cryptocurrencies usually trade on multiple exchanges because not every coin is available on every exchange or even if it is, people divide their money into different exchanges to reduce investment risk. Thanks to this application, they will be able to track all their cryptocurrency assets from a single place, see their total assets, profit and loss.
The application is based on Python, CustomTkinter framework was used. It has dark theme, coin search, coin adding-deleting, live price tracking, etc. I get live coin data through CoinGecko API. I also added a pie chart for visual impression. I tried to make the application as useful and functional as possible while creating it.
I think I created an application that will make people's job easier. I also think that I developed my knowledge base in Python thanks to this project. This is a first for me, my first project, my first effort. I hope you like it.


Features of the Application
- Real-time cryptocurrency tracking using CoinGecko API  
- Add coins to your portfolio with amount and buy price  
- View current value, 24h change, and net profit/loss  
- Pie chart visualisation of wallet distribution  
- Sort coins by name, amount, profit, price, or 24h change  
- Simple and modern GUI with dark theme  
- Persistent data saving in `wallet.json`  
- Input validation and error handling

Installation
To run the game, make sure you have Python installed on your system.
Required Libraries:
- `customtkinter`  
- `requests`  
- `pillow`  
- `pandas`  
- `plotly`
Install all with:
```bash
pip install customtkinter requests pillow pandas plotly
How it Works
-You can search for a coin using its name or symbol
-Select the coin from the list to view details and price
-Enter how much you bought and at what price, then click Add Coin
-Your portfolio will show all coins added, current value, and profit
-Click Update Prices to refresh values from the API
-Click Pie Chart to see wallet distribution
Project Structure
app.py: Main application file
wallet.json: Stores your saved crypto data
readme.txt: Project documentation
Error Handling
Checks if amount and price inputs are empty or non-numeric
Warns if no coin is selected
Displays error messages if API fails or no match is found
File Handling
Loads existing wallet data on start
Automatically saves changes to wallet.json
JSON is structured and readable for grading
Functions and Methods Used
add_coin(): Adds selected coin
delete_coin(): Removes selected coin
update_prices(): Fetches live prices
search_coin(): Filters coin list
select_coin(): Chooses coin from list
update_table(), update_summary(), show_pie_chart()
GUI elements for interaction using CustomTkinter
Libraries Used
customtkinter: GUI
requests: API handling
pillow: Image/logo display
pandas: Data handling
plotly: Pie chart visualisation
Testing
Manual testing done for:
-Coin addition/removal
-Price updates
-Chart display
-Sorting
-Empty inputs and edge cases

